from django.contrib import admin
from django.urls import path
from .views import main_view, signup_view
from profiles.views import my_recommendations_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main-view'),
    path('signup/', signup_view, name='signup-view'),
    path('profiles/', my_recommendations_view, name='my-recs-view'),
    path('<str:ref_code>/', main_view, name='main-view'),
]
