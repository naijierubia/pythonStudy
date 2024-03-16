"""
URL configuration for mysitel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page/001', views.page_001_view, name='page_001'),
    path('page/<int:pageNumbers>', views.pageN_view, name='pageN'),
    # 只匹配两位数字
    re_path(r'^(?P<NumberA>\d{1,2})/add/(?P<NumberB>\d{1,2})$', views.add_view, name='add'),
    # 生日界面
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$',views.birthday_view, name='birthday')
]
