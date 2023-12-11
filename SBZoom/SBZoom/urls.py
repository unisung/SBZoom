"""
URL configuration for SBZoom project.

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
from django.urls import path, include
from kangnam import views #SBZoom home페이지용 view를 kananam app의 views것 사용.


urlpatterns = [
    path('',views.home, name="index"),
    path('admin/', admin.site.urls),
    path('SBZoom/',views.home, name="home"),
    path('SBZoom/kangnam/',include('kangnam.urls')),
    path('SBZoom/gangdong/',include('gangdong.urls')),
    path('SBZoom/dobong/',include('dobong.urls')),
    path('SBZoom/dongdaemun/',include('dongdaemun.urls')), 
    path('SBZoom/dongjak/',include('dongjak.urls')),
    path('SBZoom/eunpyeong/',include('eunpyeong.urls')),
    path('SBZoom/gangbuk/',include('gangbuk.urls')),
    path('SBZoom/gangseo/',include('gangseo.urls')),
    path('SBZoom/geumcheon/',include('geumcheon.urls')),
    path('SBZoom/guro/',include('guro.urls')),
    path('SBZoom/gwanak/',include('gwanak.urls')),
    path('SBZoom/gwangjin/',include('gwangjin.urls')),
    path('SBZoom/jongro/',include('jongro.urls')),
    path('SBZoom/junggu/',include('junggu.urls')),
    path('SBZoom/jungnang/',include('jungnang.urls')),
    path('SBZoom/mapo/',include('mapo.urls')),
    path('SBZoom/nowon/',include('nowon.urls')),
    path('SBZoom/seocho/',include('seocho.urls')),
    path('SBZoom/seodaemun/',include('seodaemun.urls')),
    path('SBZoom/seongbuk/',include('seongbuk.urls')),
    path('SBZoom/seongdong/',include('seongdong.urls')),
    path('SBZoom/songpa/',include('songpa.urls')),
    path('SBZoom/yangcheon/',include('yangcheon.urls')),
    path('SBZoom/yeongdeungpo/',include('yeongdeungpo.urls')),
    path('SBZoom/yongsan/',include('yongsan.urls')) 
]
