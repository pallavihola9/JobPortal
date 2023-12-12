# registration/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class RegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            if request.data.get('terms_and_conditions', False) is not True:
                return Response({'terms_and_conditions': ['You must accept the terms and conditions.']}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')

        if email is not None and password is not None:
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Ensure you return a Django HttpResponse when logging in
                login(request, user)
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

class EmployerSignUpView(APIView):
    def post(self, request):
        serializer = EmployerSignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployerLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            employer = Employer.objects.get(email=email)

            # Check if the provided password matches the stored password
            if employer.password == password:
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Employer.DoesNotExist:
            return Response({'error': 'Employer not found'}, status=status.HTTP_404_NOT_FOUND)


from rest_framework import generics

class MyProfileListCreateView(generics.ListCreateAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileSerializer
    
class UpdateMyProfileView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ProfileHighlighterList(generics.ListCreateAPIView):
    queryset = ProfileHighlighter.objects.all()
    serializer_class = ProfileHighlighterSerializer

class BoostnowProfileFormList(generics.ListCreateAPIView):
    queryset = BoostnowProfileForm.objects.all()
    serializer_class = BoostnowProfileFormSerializer

class AdvancedJobSearchList(generics.ListCreateAPIView):
    queryset = AdvancedJobSearch.objects.all()
    serializer_class = AdvancedJobSearchSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class ProfileHighlighterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProfileHighlighter.objects.all()
    serializer_class = ProfileHighlighterSerializer

class BoostnowProfileFormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoostnowProfileForm.objects.all()
    serializer_class = BoostnowProfileFormSerializer

class AdvancedJobSearchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvancedJobSearch.objects.all()
    serializer_class = AdvancedJobSearchSerializer

###################################### New APIs ####################################

class JobPostingView(APIView):
    def get(self,request,format=None):
        jobs = JobPosting.objects.all()
        serializer = JobPostingSerializer(jobs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = JobPostingSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'base_image' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['base_image']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['Company_Logo_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class JobPostingUpdateDelete(APIView):
    def put(self,request,pk):
        assign_task = JobPosting.objects.get(pk=pk)
        serializer = JobPostingSerializer(assign_task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        assign_task = JobPosting.objects.get(pk=pk)
        assign_task.delete()
        return Response({"message": "deleted successfully !"},status=status.HTTP_204_NO_CONTENT)    


class AddBlogsView(APIView):
    def get(self,request,format=None):
        jobs = AddBlogs.objects.all()
        serializer = AddBlogsSerializer(jobs,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = AddBlogsSerializer(data=request.data)
        if serializer.is_valid():
            # Check if a document file was uploaded
            if 'base_image' in request.data:
                # Get the uploaded file
                uploaded_file = request.data['base_image']

                # Convert the file to base64
                try:
                    base64_encoded = base64.b64encode(uploaded_file.read()).decode('utf-8')
                except Exception as e:
                    return Response({'error': 'Error encoding file to base64.'}, status=status.HTTP_400_BAD_REQUEST)

                # Update the serializer's data to store the base64 encoded document
                serializer.validated_data['Author_Profile_Picture_base64','Images_videos_base64'] = base64_encoded

            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class AddBlogsUpdateDelete(APIView):
    def put(self,request,pk):
        assign_task = AddBlogs.objects.get(pk=pk)
        serializer = AddBlogsSerializer(assign_task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        assign_task = AddBlogs.objects.get(pk=pk)
        assign_task.delete()
        return Response({"message": "deleted successfully !"},status=status.HTTP_204_NO_CONTENT)     
    