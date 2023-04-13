from django.urls import path
from hackathons.views import HackathonListCreateAPIView, HackathonRetrieveUpdateDestroyAPIView, SubmissionCreateAPIView, SubmissionListAPIView, SubmissionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('hackathons/', HackathonListCreateAPIView.as_view(), name='hackathon-list-create'),
    path('hackathons/<int:pk>/', HackathonRetrieveUpdateDestroyAPIView.as_view(), name='hackathon-detail'),
    path('hackathons/<int:pk>/register/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('hackathons/<int:pk>/submissions/', SubmissionListAPIView.as_view(), name='submission-list'),
    path('hackathons/<int:pk>/submissions/<int:submission_pk>/', SubmissionRetrieveUpdateDestroyAPIView.as_view(), name='submission-detail')
]