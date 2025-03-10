from django.contrib import admin
from django.urls import path, include
from myapp import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),# Include `myapp` URLs
]


