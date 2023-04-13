from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from rest_framework import generics, permissions
from rest_framework.authentication import BasicAuthentication
from rest_framework.parsers import FormParser, MultiPartParser


from .models import Hackathon, Submission
from .serializers import HackathonSerializer, SubmissionSerializer


class HackathonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [FormParser, MultiPartParser]
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(creator=self.request.user)


class HackathonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]


class SubmissionCreateAPIView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        hackathon_id = self.kwargs.get('hackathon_id')
        hackathon = get_object_or_404(Hackathon, id=hackathon_id)
        serializer.save(user=self.request.user, hackathon=hackathon)

    def get_serializer_context(self):
        context =  super().get_serializer_context()
        context['hackathon'] = get_object_or_404(Hackathon, id=self.kwargs.get('hackathon_id'))
        return context

class SubmissionListAPIView(generics.ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [BasicAuthentication]


    def get_queryset(self):
        hackathon_id = self.kwargs.get('hackathon_id')
        return Submission.objects.filter(hackathon__id=hackathon_id)
    
class SubmissionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class HackathonRegistrationAPIView(generics.CreateAPIView):
    queryset = Hackathon.objects.all()
    serializer_class = HackathonSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        hackathon_id = self.kwargs.get('hackathon_id')
        hackathon = Hackathon.objects.get(id=hackathon_id)
        serializer.save(user=self.request.user, hackathon=hackathon)
