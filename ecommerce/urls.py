from django.urls import path
from.import views
from django.conf.urls.static import static
from django.conf import settings  




urlpatterns = [
    
    path('lot',views.logoutpage,name='lot'),
     path('reg',views.userform,name='reg'),
    path('log',views.log,name='log'),
    path('lin',views.loginpage,name='lin'),
    path('',views.home,name=''),
    path('cat',views.categories,name='cat'),
    path('prop',views.property,name='prop'),
    path('cars',views.car,name='cars'),
    path('bike',views.bike,name='bike'),
    path('mobiles',views.mobiles,name='mobiles'),
    path('ele',views.electronics,name='ele'),
    path('fur',views.furnitures,name='fur'),
    path('detail/<int:pk>',views.detail.as_view(),name='detail'),
    path('deta/<int:pk>',views.deta.as_view(),name='deta'),
    path('deta1/<int:pk>',views.deta1.as_view(),name='deta1'),
    path('deta2/<int:pk>',views.deta2.as_view(),name='deta2'),
    path('deta3/<int:pk>',views.deta3.as_view(),name='deta3'),
    path('deta4/<int:pk>',views.deta4.as_view(),name='deta4'),
    path('search',views.search,name='search'),
    path('search',views.search1,name='search'),
     path('create',views.create.as_view(),name='create'),
      path('list',views.list.as_view(),name='list'),
       path('delete/<int:pk>',views.delete.as_view(),name='delete'),
        #   path('list',views.list.as_view(),name='list'),
      
     
    
]


urlpatterns+= static(settings.MEDIA_URL,
                     document_root=settings.MEDIA_ROOT)