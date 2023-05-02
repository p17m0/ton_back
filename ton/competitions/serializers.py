from rest_framework import serializers
from . import models

class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competition
        fields = ['name', 'currency', 'type_of_competition', 'amount_of_members', 'date', 'time', 'win', 'royalty']
