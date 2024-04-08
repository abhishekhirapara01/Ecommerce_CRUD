from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index,name= 'index'),
    path('mobile/<int:id>',views.mobile, name='mobile'),
    path('show/',views.show,name="show"),
    path('add/',views.add, name='add'),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('register/',views.register,name="register"),
    path('login/',views.loginaccount,name="loginaccount"),
    path('logout/',views.logoutaccount,name="logoutaccount"),
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path('confirm_checkout/', views.confirm_checkout, name='confirm_checkout'),
    path('remove/<int:mobile_id>/', views.remove_from_cart, name='remove_from_cart'), 
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
