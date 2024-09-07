from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [    
  path('', views.index, name='index'),
  path('aml', views.aml, name='aml'),
  path('bd', views.bd, name='bd'),
  path('blog', views.blog, name='blog'),
  path('book', views.book, name='book'),
  path('dig', views.dig, name='dig'),
  path('fa', views.fa, name='fa'),
  path('inter', views.inter, name='inter'),
  path('lead', views.lead, name='lead'),
  path('mb', views.mb, name='mb'),
  path('sc', views.sc, name='sc'),
  path('tax', views.tax, name='tax'),
  path('ui', views.ui, name='ui'),
  path('web', views.web, name='web'),
]