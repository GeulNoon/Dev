from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'email',
            'name',
            'password',
            'affiliation',
            'age',
        )
        model = Post