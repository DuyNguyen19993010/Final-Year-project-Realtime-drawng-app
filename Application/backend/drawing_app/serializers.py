from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {'password':{'write_only':True,'required':True}}
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user = user)
        return user
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user','fname','lname','occupation','location', 'aboutMe','profile_pic']
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ['canvas','index','id']
class LayerAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'
class LayerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = ['image']
class joinedRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['room']
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'