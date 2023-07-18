from django.urls import path
from.import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('registration/',views.registration,name='registration'),
    path('update/<int:id>',views.update,name='update'),
    path('home/<int:id>',views.home,name='home'),
    path('changepassword/<int:id>',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('gallery/',views.gallerys,name='gallery'),
    path('details/<int:id>',views.details,name='details'),
]