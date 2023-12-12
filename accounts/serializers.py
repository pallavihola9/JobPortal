# registration/serializers.py
from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    terms_and_conditions = serializers.BooleanField(default=False)
    confirm_password = serializers.CharField(write_only=True)  # Add this line

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'full_name', 'password', 'terms_and_conditions', 'confirm_password')  # Include confirm_password
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        if validated_data['password'] != validated_data['confirm_password']:
            raise serializers.ValidationError("Password and Confirm Password must match")
        user = CustomUser(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            terms_and_conditions=validated_data.get('terms_and_conditions', False),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class EmployerSignUpSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Employer
        fields = ('id', 'username', 'email', 'password', 'confirm_password', 'terms_and_conditions')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Password and Confirm Password must match")
        return data

    def create(self, validated_data):
        # Remove 'confirm_password' from 'validated_data'
        validated_data.pop('confirm_password', None)

        # Manually set the password field
        password = validated_data.pop('password')
        employer = Employer(**validated_data)
        employer.password = password  # Set the password field directly
        employer.save()
        return employer

class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProfile
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class ProfileHighlighterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileHighlighter
        fields = '__all__'

class BoostnowProfileFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoostnowProfileForm
        fields = '__all__'

class AdvancedJobSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedJobSearch
        fields = '__all__'

##################################### New APi Serializer ###################################
class JobPostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosting
        fields= '__all__'

class AddBlogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddBlogs
        fields = '__all__'        