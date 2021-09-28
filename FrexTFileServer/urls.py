"""FrexTFileServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from FrexTFileServer import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'tcls/$', views.tcls),
    url(r'questions/$', views.questions),
    url(r'tests/$', views.tests),

    url(r'own_bits/$', views.own_bits), # 必须放在前面？？？？

    url(r'online_bits/$', views.online_bits), # 必须放在前面？？？？
    url(r'online_logs/$', views.online_logs), # 不然会先匹配logs？？？？

    url(r'bits/$', views.bits),
    url(r'logs/$', views.logs),
    url(r'results/$', views.results),
    url(r'experiment/$', views.experiment),

    url(r'help/$', views.help),
    url(r'ping/$', views.ping),
]
