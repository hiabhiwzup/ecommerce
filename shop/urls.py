from django.urls import path
from . import views
urlpatterns = [
path('', views.index, name="ShopHome"),
path('about/', views.about ,name ="about us"),
path('contact/', views.contact,name ="contact us"),
path('tracker/', views.tracker ,name ="trackingstatus"),
path('search/', views.search ,name ="search"),
path("products/<int:myid>", views.prodview ,name ="about the product"),
path('checkout/', views.checkout ,name ="checking out"),
]