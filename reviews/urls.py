from django.urls import path
from . import views
    

urlpatterns = [
    path("", views.ReviewView.as_view(), name='home'),
    path("thank_you", views.ThankyouView.as_view(), name='thankyou'),
    path("reviews", views.ReviewListView.as_view(), name='reviews'),
    path("reviews/<int:pk>", views.ReviewDetail.as_view(), name='detail')
]