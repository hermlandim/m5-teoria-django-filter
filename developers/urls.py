from django.urls import path
from developers import views

urlpatterns = [
    path('developers/', views.DeveloperView.as_view()),
]
