from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/<int:user_id>', views.user_detail, name='detail'),
    # path('users/', views.users, name='users_index'),
    path('skills/create/', views.SkillCreate.as_view(), name='skills_create'),
    path('skills/<int:pk>/update/',
         views.SkillUpdate.as_view(), name='skills_update'),
    path('skills/<int:pk>/delete/',
         views.SkillDelete.as_view(), name='skills_delete'),
]
