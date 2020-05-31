from django.urls import path , include
from . import views 

urlpatterns = [
    path('old/', views.contact ),
    path('', views.snippet_detail,name='form-page'),
    path('success',views.sucess_form,name="success"),
    path('exports/',views.export_data,name="exporting")
]
