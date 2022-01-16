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
        slug = slugify(validated_data.product)
        product = Product.objects.get_or_create(**validated_data, slug=slug)
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
        slug = slugify(validated_data.brand)
        brand = Brand.objects.get_or_create(**validated_data, slug=slug)
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
        slug = slugify(validated_data.store)
        store = Store.objects.get_or_create(**validated_data, slug=slug)
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

        product_name = validated_data["product"]["product"].strip()
        product = Product.objects.get_or_create(product=product_name, user=user)[0]
        validated_data["product"] = product

        brand_name = validated_data["brand"]["brand"].strip()
        if brand_name == "":
            brand = None
        else:
            brand = Brand.objects.get_or_create(brand=brand_name, user=user)[0]
        validated_data["brand"] = brand

        store_name = validated_data["store"]["store"].strip()
        if store_name == "":
            store = None
        else:
            store = Store.objects.get_or_create(store=store_name, user=user)[0]
        validated_data["store"] = store

        tags_raw = validated_data.pop("tags")
        tags = [Tag.objects.get_or_create(name=tag["name"].strip(), user=user)[0] for tag in tags_raw]

        review = Review.objects.create(**validated_data)

        for tag in tags:
            review.tags.add(tag)

        return review
