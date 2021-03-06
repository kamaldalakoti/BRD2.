"""Admission URL Configuration

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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# import notifications.urls


admin.site.site_header = 'Student Admission'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include( 'Student.urls')),
    path('',include( 'Teachers.urls')),
    path('',include( 'student_dashboard.urls')),
    path('accounts/',include ('accounts.urls')),
    # url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
