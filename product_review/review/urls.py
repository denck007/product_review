from django.urls import path, include, re_path

from review import views

urlpatterns = [
    # path('products/search/', views.search),
    path("reviews/", views.ReviewDetailList.as_view()),
    path("reviews/tag/<str:tag_slug>", views.ReviewDetailByTagList.as_view()),
    path("reviews/<int:review_id>/", views.ReviewDetail.as_view()),
    path("tags/<str:tag_slug>", views.TagDetail.as_view()),
]
