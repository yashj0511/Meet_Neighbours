from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path('', views.index, name = 'home'),
      path('meet', views.meet, name = 'meet'),
      path('sort',views.sort,name='sort'),
      path('sort/age/<int:age>',views.sortbyage,name='sortbyage'),
      path('sort/gender/<str:sex>',views.sortgender,name='sortbygender'),  
      path('sort/age/teen',views.teenage,name='teenagers'),  
      path('sort/age/adults',views.adults,name='adults'),  
      path('events',views.events,name="events"),
     path('greet',views.greet,name='greet')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)