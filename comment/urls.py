from django.urls import path
from . import views

app_name='comment'

urlpatterns = [
    path('create/<int:product_id>/', views.create_comment, name='create'),
    path('edit/<int:comment_id>/', views.edit_comment, name='edit'),
]