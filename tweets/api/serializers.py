from rest_framework import serializers
from tweets.models import Tweet
from accounts.api.serializers import UserDisplaySerializer
from django.utils.timesince import timesince


class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDisplaySerializer(read_only=True) # this brings all data from user not only id
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()
    class Meta:
        model = Tweet
        fields = [
            'user',
            'content',
            'timestamp',
            'date_display',
            'timesince',
        ]

    def get_date_display(self, obj):
        return obj.timestamp.strftime("%b %d, %Y | at %I:%M %p")

    def get_timesince(self, obj):
        return timesince(obj.timestamp) + " ago"
