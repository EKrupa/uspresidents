from django.contrib import admin
from django.urls import path
from .views import home, president

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('president/<int:id>', president, name='president')
]
