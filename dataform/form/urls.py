from django.urls import path , include
from . import views 

urlpatterns = [
    path('old/', views.contact ),
    path('', views.snippet_detail,name='form-page'),
    path('success',views.sucess_form,name="success"),
    path('exports/',views.export_data,name="exporting"),
    path('crew/',views.crew_page,name="crew"),
    path('anime/',views.anime_page,name="anime"),
    path('tiktok/',views.bantt)
]
