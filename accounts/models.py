from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import base64

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password=None):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, default="null")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    terms_and_conditions = models.BooleanField(default=False)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Employer(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Securely hash and store passwords
    terms_and_conditions = models.BooleanField(default=False)

class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    upload_resume = models.FileField(upload_to='resumes/')
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description_1 = models.TextField()
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    description_2 = models.TextField()
    skill_set = models.TextField()

    def __str__(self):
        return self.name


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    certification = models.CharField(max_length=100)
    completion_date = models.DateField()

    def __str__(self):
        return self.course_name

class ProfileHighlighter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.TextField()
    work_experience = models.TextField()

    def __str__(self):
        return self.name

class BoostnowProfileForm(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    education = models.TextField()
    work_experience = models.TextField()

    def __str__(self):
        return self.full_name

class AdvancedJobSearch(models.Model):
    EXPERIENCE_CHOICES = (
        ('0-1', '0 to 1 years'),
        ('1-2', '1 to 2 years'),
        ('3-5', '3 to 5 years'),
        ('5-10', '5 to 10 years'),
    )

    key_skills = models.CharField(max_length=100)
    location = models.CharField(max_length=50)  # You may want to use a ForeignKey to a City model here if needed.
    experience = models.CharField(max_length=5, choices=EXPERIENCE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    industry = models.CharField(max_length=100)
    function = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.key_skills} - {self.location}"
    
class JobPosting(models.Model):

    TYPES = (
        ('full_time', 'Full-Time'),
        ('part_time', 'Part-Time'),
        ('contract', 'Contract'),
    )

    Job_Title = models.CharField(max_length=255,null=True,blank=True)
    Company_Name = models.CharField(max_length=255,null=True,blank=True)
    Location = models.CharField(max_length=255,null=True,blank=True)
    Job_Type = models.CharField(max_length=255,choices=TYPES) 
    Industry = models.CharField(max_length=255,null=255,blank=True)
    Job_Description = models.CharField(max_length=255,null=255,blank=True)
    Responsibilities = models.CharField(max_length=255,null=255,blank=True)
    Qualifications = models.CharField(max_length=255,null=255,blank=True)
    Education_Requirements = models.CharField(max_length=255,null=255,blank=True)
    Experience_Level = models.CharField(max_length=255,null=255,blank=True)
    Salary_Compensation = models.CharField(max_length=255,null=255,blank=True)
    Application_Deadline = models.CharField(max_length=255,null=255,blank=True)
    Application_Instructions  = models.CharField(max_length=255,null=255,blank=True)
    Application_URL_Email = models.CharField(max_length=255,null=255,blank=True)
    Benefits = models.CharField(max_length=255,null=255,blank=True)
    Company_Logo_base64 = models.TextField(null=True, blank=True)
    Company_Description = models.CharField(max_length=255,null=255,blank=True)
    Contact_Information = models.CharField(max_length=255,null=255,blank=True)
    Tags_Keywords = models.CharField(max_length=255,null=255,blank=True)
    Job_ID  = models.CharField(max_length=255,null=255,blank=True)
    Job_Posting_Date = models.CharField(max_length=255,null=255,blank=True)
    Expiration_Date = models.CharField(max_length=255,null=255,blank=True)


class AddBlogs(models.Model):
    blog_title = models.CharField(max_length=255,null=True,blank=True) 
    Author_Name = models.CharField(max_length=255,null=True,blank=True) 
    Author_Email= models.CharField(max_length=255,null=True,blank=True) 
    Date_of_Submission = models.CharField(max_length=255,null=True,blank=True) 
    Blog_Content= models.CharField(max_length=255,null=True,blank=True) 
    Category_Topic = models.CharField(max_length=255,null=True,blank=True) 
    Keywords_Tags = models.CharField(max_length=255,null=True,blank=True)
    Author_Bio = models.CharField(max_length=255,null=True,blank=True) 
    Author_Profile_Picture_base64 =models.TextField(null=True,blank=True)  
    Images_videos_base64 = models.TextField(null=True,blank=True)