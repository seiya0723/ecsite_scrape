from django.urls import path
from . import views

app_name    = "rakuten_review"
urlpatterns = [ 
    path("", views.index, name="index"),
]


