from django.utils.text import slugify
from rest_framework import serializers

from .models import Review, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
        )

    def create(self, validated_data):
        print(f"TagSerializer: {validated_data=}")
        slug = slugify(validated_data.name)
        tag = Tag.objects.get_or_create(**validated_data, slug=slug)
        return tag

class ReviewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "product",
            "brand",
            "tags",
            "rating",
            "notes",
            "store",
            "price",
            "product_url",
            "created_at",
            "get_absolute_url",
            "get_image",
            "get_thumbnail",
        )

    def create(self, validated_data):
        tags = validated_data.pop("tags")
        review = Review.objects.create(**validated_data)

        for tag in tags:
            review.tags.add(tag)

        return review
