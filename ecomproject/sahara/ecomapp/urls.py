from . import views
from django.urls import path
app_name = 'ecomapp'

urlpatterns = [
    path('', views.allProdCat, name = 'allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name = 'product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDetail, name = 'proCatdetail')
]