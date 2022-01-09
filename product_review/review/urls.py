from django.urls import path

from review import views

urlpatterns = [
    # path('products/search/', views.search),
    path("tags/", views.TagModelViewSet.as_view({"get": "list", "post": "create"})),
    path("tags/<int:pk>/", views.TagModelViewSet.as_view({"get": "retrieve"})),
    path("reviews/", views.ReviewModelViewSet.as_view({"get": "list", "post": "create"})),
    path("reviews/<int:pk>/", views.ReviewModelViewSet.as_view({"get": "retrieve"})),
    path("reviews/tag/<str:tag_slug>", views.ReviewDetailByTagList.as_view()),
]
