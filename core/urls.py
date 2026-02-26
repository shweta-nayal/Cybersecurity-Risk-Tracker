from django.contrib import admin
from django.urls import path, include

from risks.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('api/', include('risks.urls')),
]
