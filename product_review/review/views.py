from django.contrib.auth.models import User
from django.db.models import Q
from django.http.response import Http404

from rest_framework import serializers, status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import Review, Tag
from .serializers import ReviewSerializer, TagSerializer


class ReviewDetailList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        reviews = Review.objects.filter(user=request.user).all()[:10]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetailByTagList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, tag_slug, format=None):
        reviews = Review.objects.filter(user=request.user).filter(tags__slug__in=[tag_slug]).all()[:10]
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewDetail(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, review_id, format=None):
        review = self.get_object(review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def post(self, request, format=None):

        tags_data = request.data.pop("tags")
        tags = [Tag.objects.get_or_create(name=tag["name"], user=request.user)[0] for tag in tags_data]
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


class TagDetail(APIView):
    def get_object(self, tag_slug):
        try:
            return Tag.objects.get(slug=tag_slug)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, tag_slug, format=None):
        tag = self.get_object(tag_slug)
        serializer = TagSerializer(tag)
        return Response(serializer.data)


class TagList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        tags = Tag.objects.filter(user=request.user)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)


class ReviewsListing(ModelViewSet):
    serializer_class = ReviewSerializer(many=True)
