from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', login_view, name='login'),
    path('employer_signup/', EmployerSignUpView.as_view(), name='employer-signup'),
    path('employer_login/', EmployerLoginView.as_view(), name='employer-login'),
    path('myprofile/', MyProfileListCreateView.as_view(), name='profile-list-create'),
    path('myprofile/<int:pk>/', UpdateMyProfileView.as_view(), name='update-user-profile'),
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('profile-highlighters/', ProfileHighlighterList.as_view(), name='profile-highlighter-list'),
    path('profile-highlighters/<int:pk>/', ProfileHighlighterDetail.as_view(), name='profile-highlighter-detail'),
    path('boostnow-profile-forms/', BoostnowProfileFormList.as_view(), name='boostnow-profile-form-list'),
    path('boostnow-profile-forms/<int:pk>/', BoostnowProfileFormDetail.as_view(), name='boostnow-profile-form-detail'),
    path('advanced-job-searches/', AdvancedJobSearchList.as_view(), name='advanced-job-search-list'),
    path('advanced-job-searches/<int:pk>/', AdvancedJobSearchDetail.as_view(), name='advanced-job-search-detail'),
 ############################### New Urls ##########################################   
    path('job_posting/', JobPostingView.as_view(), name='job_posting'),
    path('job_posting/<int:pk>/', JobPostingUpdateDelete.as_view(), name='job_posting'),
    path('add_blogs/', AddBlogsView.as_view(), name='job_posting'),
    path('add_blogs/<int:pk>/', AddBlogsUpdateDelete.as_view(), name='job_posting'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

