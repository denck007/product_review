from django.utils.text import slugify
from rest_framework import serializers

from .models import Brand, Product, Review, Store, Tag


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "product",
            "slug",
            "get_absolute_url",
        )

    def create(self, validated_data):
        validated_data["product"] = validated_data["product"].strip()
        slug = slugify(validated_data["product"])
        product = Product.objects.filter(slug=slug, user=validated_data["user"]).first()
        if product is None:
            product = Product.objects.get_or_create(**validated_data, slug=slug)[0]
        return product


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "brand",
            "slug",
            "get_absolute_url",
        )

    def create(self, validated_data):
        validated_data["brand"] = validated_data["brand"].strip()
        slug = slugify(validated_data["brand"])
        brand = Brand.objects.filter(slug=slug, user=validated_data["user"]).first()
        if brand is None:
            brand = Brand.objects.get_or_create(**validated_data, slug=slug)[0]
        return brand


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            "id",
            "store",
            "slug",
            "get_absolute_url",
        )

    def create(self, validated_data):
        validated_data["store"] = validated_data["store"].strip()
        slug = slugify(validated_data["store"])
        store = Store.objects.filter(slug=slug, user=validated_data["user"]).first()
        if store is None:
            store = Store.objects.get_or_create(**validated_data, slug=slug)[0]
        return store


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
        slug = slugify(validated_data.name)
        tag = Tag.objects.get_or_create(**validated_data, slug=slug)
        return tag


class ReviewSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    product = ProductSerializer()
    store = StoreSerializer()
    brand = BrandSerializer()

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
        user = validated_data["user"]

        product_serializer = ProductSerializer(data=validated_data["product"])
        if product_serializer.is_valid():
            validated_data["product"] = product_serializer.save(user=user)

        brand_serialzier = BrandSerializer(data=validated_data["brand"])
        if brand_serialzier.is_valid():
            validated_data["brand"] = brand_serialzier.save(user=user)

        store_serialzier = StoreSerializer(data=validated_data["store"])
        if store_serialzier.is_valid():
            validated_data["store"] = store_serialzier.save(user=user)

        tags_raw = validated_data.pop("tags")
        tags = [Tag.objects.get_or_create(name=tag["name"].strip(), user=user)[0] for tag in tags_raw]

        review = Review.objects.create(**validated_data)

        for tag in tags:
            review.tags.add(tag)

        return review
