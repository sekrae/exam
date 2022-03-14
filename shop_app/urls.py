from django.urls import path
from . import views

urlpatterns = [
    path('shop_app/', views.product_view, name='all_products'),
    # path('create_news/', views.create_view),
    # path('news_app/<int:id>/', views.detail_view, name='detail_view'),
    # path('news_app/<int:id>/delete/', views.delete_view, name='delete_new'),
    # path('news_app/<int:id>/update/', views.update_view, name='update_new'),
]