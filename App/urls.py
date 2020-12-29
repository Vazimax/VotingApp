from django.urls import path
from .views import Home , Detail , Results , Vote

app_name = 'polls'
urlpatterns = [
    path('',Home,name="home"),
    path('<str:pk>/',Detail,name="detail"),
    path('<str:pk>/results/',Results,name="result"),
    path('<str:pk>/vote/',Vote,name="vote"),

]