from django.urls import path,include
from base_app import views

app_name = 'main'

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.homepage,name='home'),
    path('logout/',views.logout_view,name='logout_custom'),
    path('predict/',views.predict,name='predict'),
]