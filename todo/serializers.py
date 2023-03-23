from rest_framework import serializers

from .models import Todo

# creating the serializers whose work is to convert model instances to json
class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')