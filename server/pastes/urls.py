from django.urls import path
from . import views
from .views import  PasteView, PasteDetail, PasteAddView

app_name = 'pastes'

urlpatterns = [
    path('', views.index, name = "index"),
    path('list/', PasteView.as_view(), name = "paste_list"),
    path('detail/<int:pk>', PasteDetail.as_view(), name = 'paste_detail'),
    path('add_paste/', views.PasteAddView, name = 'add_paste'),

]