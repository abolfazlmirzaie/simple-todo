from rest_framework import serializers
from .models import Task



class TaskSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user', 'id', 'created_at', 'updated_at')
        hidden_fields = ('user', 'id', 'created_at', 'updated_at')