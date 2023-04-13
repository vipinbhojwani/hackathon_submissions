from rest_framework import serializers
from .models import Hackathon, Submission

class HackathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hackathon
        fields = ('id', 'title', 'description', 'background_image', 'hackathon_image', 'submission_type', 'start_datetime', 'end_datetime', 'reward_prize')

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ('id', 'name', 'summary', 'submission', 'hackathon')

    def validate(self, data):
        hackathon = self.context['hackathon']
        submission_type = hackathon.submission_type

        if submission_type == 'image':
            image = data.get('submission')
            if not image:
                raise serializers.ValidationError('An image submission is required.')
            # Add additional validation logic for image submissions here

        elif submission_type == 'file':
            file = data.get('submission')
            if not file:
                raise serializers.ValidationError('A file submission is required.')
            # Add additional validational logic for file submissions here

        elif submission_type == 'link':
            link = data.get('submission')
            if not link:
                raise serializers.ValidationError('A link submission is required.')
            # Add additional validation logic for link submissions here

        return data