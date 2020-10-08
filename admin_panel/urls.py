from django.urls import path
from . import views


app_name = 'admin_panel'

urlpatterns = [
    path('',views.Index.as_view(), name='index' ),
    path('aboutUs/', views.AboutUs.as_view(), name='aboutUs'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('list_products/', views.ProductListView.as_view(), name=views.ProductListView.name),
]

