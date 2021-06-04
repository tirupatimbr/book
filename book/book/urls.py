"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.contrib.auth import views as auth_views
from bookapp import views
from rest_framework_swagger.views import get_swagger_view

from django.conf.urls.static import static
schema_view = get_swagger_view(title = "Book API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_api/',schema_view),
    path('api/',include(('bookapp.urls','bookapp'),namespace='bookapp')),
    # path('bookapp/',include('bookapp.urls')),
    path('register/',views.registration),
    path('login/',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('password_reset/',views.password_reset,name="password_reset"),
    path('image/',views.profile_image,name="image"), 
    path('base_64_post/',views.base_64_post,name="base_64_post"),
    path('base_post/',views.base_post,name="base_post"),

    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
