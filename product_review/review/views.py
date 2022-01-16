import sys
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, authentication, permissions, mixins, filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response


from .models import Brand, Product, Review, Store, Tag
from .serializers import ReviewSerializer, TagSerializer, ProductSerializer, StoreSerializer, BrandSerializer


class ModelViewSet_User(ModelViewSet):
    ###################### Fields to populate
    # model =
    # serializer_class =
    # filterset_fields = [
    #    "product",
    # ]
    # search_fields = [
    #    "product",
    # ]
    ######################

    # Common fields
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    paginate_by = 10
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).all()

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                exc_info = sys.exc_info()
                print(exc_info)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewModelViewSet(ModelViewSet_User):
    model = Review
    serializer_class = ReviewSerializer
    filterset_fields = ["product__product", "tags__name", "tags__slug", "notes", "brand__brand", "store__store"]
    search_fields = ["product__product", "tags__name", "notes", "brand__brand", "store__store"]


class ProductModelViewSet(ModelViewSet_User):
    model = Product
    serializer_class = ProductSerializer
    filterset_fields = [
        "product",
    ]
    search_fields = [
        "product",
    ]


class StoreModelViewSet(ModelViewSet_User):
    model = Store
    serializer_class = StoreSerializer
    filterset_fields = [
        "store",
    ]
    search_fields = [
        "store",
    ]


class BrandModelViewSet(ModelViewSet_User):
    model = Brand
    serializer_class = BrandSerializer
    filterset_fields = [
        "brand",
    ]
    search_fields = [
        "brand",
    ]


class ReviewDetailByTagList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, tag_slug, format=None):
        reviews = Review.objects.filter(user=request.user).filter(tags__slug__in=[tag_slug]).all()[:10]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class TagModelViewSet(ModelViewSet):
    serializer_class = TagSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    paginate_by = 1000

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user).all()
