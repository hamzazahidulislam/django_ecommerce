from django.urls import path
from .views import *
from product.views import Create_Product, Product_List, Category_List, Product_Edit, Product_Delete, Product_Detail

urlpatterns = [
    path('login/', user_login, name='user-login'),
    path('logout/', user_logout, name='user-logout'),
    path('signup/', user_signup, name='user-singup'),
    path('dashboard/', user_dashboard, name='user-dashboard'),
    path('create-post/', create_post, name='create-post'),
    path('profile/', user_profile, name='profile'),
    path('profile/create-profile/', create_profile, name='create-profile'),
    path('profile/edit-profile/', edit_profile, name='edit-profile'),
    path('dashboard/create-product', Create_Product.as_view(), name='create-product'),
    path('dashboard/product-list', Product_List.as_view(), name='product-list'),
    path('dashboard/product-edit/<int:pk>', Product_Edit.as_view(), name='product-edit'),
    path('dashboard/product-delete/<int:pk>', Product_Delete.as_view(), name='product-delete'),
    path('dashboard/product-detail/<int:pk>', Product_Detail.as_view(), name='product-detail'),
    path('dashboard/category-list', Category_List.as_view(), name='category-list'),
]