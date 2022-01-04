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
    def get_object(self, review_id):
        try:
            return Review.objects.get(pk=review_id)
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, review_id, format=None):
        review = self.get_object(review_id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)


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


class ReviewsListing(ModelViewSet):
    serializer_class = ReviewSerializer(many=True)
