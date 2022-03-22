
from django.urls import path

from stupid.views import(
    IndexView,

)

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
  
    

]