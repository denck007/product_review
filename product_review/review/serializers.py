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


class ReviewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Review
        fields = (
            "id",
            "product",
            "brand",
            "tags",
            "score",
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
        tags_data = validated_data.pop("tags")

        tags = []
        for tag_data in tags_data:
            tags.append = Tag.objects.get_or_create(**tag_data)
        review = Review.objects.create(tags=tags, **validated_data)

        return review
