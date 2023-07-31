"""milkfarm_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.conf.urls import url
from milkfarm_backend_app import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('member', views.MemberViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("member/",views.NewMember.as_view()),
    path("todaysdata/",views.Today.as_view()),
    path("payments/",views.Payments.as_view())
    # path('',include(router.urls))
]
