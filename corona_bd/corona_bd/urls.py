
from django.contrib import admin
from django.urls import path
from api.views import Home, MainPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', Home.as_view()),
    path('', MainPage.as_view())
]