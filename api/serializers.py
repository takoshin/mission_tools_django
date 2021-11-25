from rest_framework import serializers
from .models import LostArticle, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password',]
        extra_kwargs = {
            'password':{
                'write_only': True,
                'required':True
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LostArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostArticle
        fields = [
            'id',
            'lost_article',
            'place',
            'discoverer',
            'customer',
            'phone_number',
            'staff_name',
            'state',
            'created_at',
            'updated_at',
        ]