# Generated by Django 4.0 on 2022-01-15 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("brand", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="user_brands", to="auth.user"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("product", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="user_products", to="auth.user"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="user_tags", to="auth.user"
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("store", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="user_stores", to="auth.user"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("rating", models.PositiveSmallIntegerField(default=3)),
                ("notes", models.TextField(blank=True, max_length=4096, null=True)),
                ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ("product_url", models.URLField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("image", models.ImageField(blank=True, null=True, upload_to="product_images/")),
                ("thumbnail", models.ImageField(blank=True, null=True, upload_to="product_images/thumbnails/")),
                (
                    "brand",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="review.brand",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="reviews", to="review.product"
                    ),
                ),
                (
                    "store",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="review.store",
                    ),
                ),
                ("tags", models.ManyToManyField(related_name="reviews", to="review.Tag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="reviews", to="auth.user"
                    ),
                ),
            ],
            options={
                "ordering": ["-created_at"],
            },
        ),
    ]


operations = [
    migrations.CreateModel(
        name="Brand",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("brand", models.CharField(blank=True, max_length=255, null=True)),
            ("slug", models.SlugField(null=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            (
                "user",
                models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name="user_brands", to="auth.user"
                ),
            ),
        ],
        options={
            "ordering": ["-created_at"],
        },
    ),
    migrations.CreateModel(
        name="Product",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("product", models.CharField(max_length=255)),
            ("slug", models.SlugField(blank=True, null=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            (
                "user",
                models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name="user_products", to="auth.user"
                ),
            ),
        ],
        options={
            "ordering": ["-created_at"],
        },
    ),
    migrations.CreateModel(
        name="Tag",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("name", models.CharField(max_length=255)),
            ("slug", models.SlugField(blank=True, null=True)),
            ("date_added", models.DateTimeField(auto_now_add=True)),
            (
                "user",
                models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name="user_tags", to="auth.user"
                ),
            ),
        ],
        options={
            "ordering": ("name",),
        },
    ),
    migrations.CreateModel(
        name="Store",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("store", models.CharField(blank=True, max_length=255, null=True)),
            ("slug", models.SlugField(blank=True, null=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            (
                "user",
                models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name="user_stores", to="auth.user"
                ),
            ),
        ],
        options={
            "ordering": ["-created_at"],
        },
    ),
    migrations.CreateModel(
        name="Review",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("rating", models.PositiveSmallIntegerField(default=3)),
            ("notes", models.TextField(blank=True, max_length=4096, null=True)),
            ("price", models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ("product_url", models.URLField(blank=True, null=True)),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("image", models.ImageField(blank=True, null=True, upload_to="product_images/")),
            ("thumbnail", models.ImageField(blank=True, null=True, upload_to="product_images/thumbnails/")),
            (
                "brand",
                models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="reviews",
                    to="review.brand",
                ),
            ),
            (
                "product",
                models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, related_name="reviews", to="review.product"
                ),
            ),
            (
                "store",
                models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="reviews",
                    to="review.store",
                ),
            ),
            ("tags", models.ManyToManyField(related_name="reviews", to="review.Tag")),
            (
                "user",
                models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="reviews", to="auth.user"),
            ),
        ],
        options={
            "ordering": ["-created_at"],
        },
    ),
]
