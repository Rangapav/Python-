"""
URL configuration for Log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('signin/',views.signup,name='signin'),
    path('home/',views.home,name='home'),
    path('Employee/',views.EmpListView.as_view(),name='Employee'),
    path('create/',views.EmpCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.EmpUpdateView.as_view()),
    path('delete/<int:pk>/',views.EmpDeleteView.as_view()),
    path('logout/',views.logout_view,name='logout'),
    path('employee_list/',views.employee_list)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
