from django.contrib import admin
from django.urls import path, include

from core.views import home
from risks.views import HomeView

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/', include('risks.urls')),
]
