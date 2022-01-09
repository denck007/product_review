from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, authentication, permissions, mixins, filters
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response


from .models import Review, Tag
from .serializers import ReviewSerializer, TagSerializer


class ReviewModelViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    paginate_by = 10
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["product", "tags__name", "notes", "brand", "store"]
    search_fields = ["product", "tags__name", "notes", "brand", "store"]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).all()

    def create(self, request):

        tags_data = request.data.pop("tags")
        tags = [Tag.objects.get_or_create(name=tag, user=request.user)[0] for tag in tags_data]
        request.data["tags"] = []

        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(user=request.user, tags=tags)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                import sys

                exc_info = sys.exc_info()
                print(exc_info)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user).all()
