# Generated by Django 4.2 on 2023-11-10 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_advancedjobsearch_boostnowprofileform_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBlogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(blank=True, max_length=255, null=True)),
                ('Author_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Author_Email', models.CharField(blank=True, max_length=255, null=True)),
                ('Date_of_Submission', models.CharField(blank=True, max_length=255, null=True)),
                ('Blog_Content', models.CharField(blank=True, max_length=255, null=True)),
                ('Category_Topic', models.CharField(blank=True, max_length=255, null=True)),
                ('Keywords_Tags', models.CharField(blank=True, max_length=255, null=True)),
                ('Author_Bio', models.CharField(blank=True, max_length=255, null=True)),
                ('Author_Profile_Picture_base64', models.TextField(blank=True, null=True)),
                ('Images_videos_base64', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPosting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_Title', models.CharField(blank=True, max_length=255, null=True)),
                ('Company_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('Location', models.CharField(blank=True, max_length=255, null=True)),
                ('Job_Type', models.CharField(blank=True, max_length=255, null=True)),
                ('Industry', models.CharField(blank=True, max_length=255, null=255)),
                ('Job_Description', models.CharField(blank=True, max_length=255, null=255)),
                ('Responsibilities', models.CharField(blank=True, max_length=255, null=255)),
                ('Qualifications', models.CharField(blank=True, max_length=255, null=255)),
                ('Education_Requirements', models.CharField(blank=True, max_length=255, null=255)),
                ('Experience_Level', models.CharField(blank=True, max_length=255, null=255)),
                ('Salary_Compensation', models.CharField(blank=True, max_length=255, null=255)),
                ('Application_Deadline', models.CharField(blank=True, max_length=255, null=255)),
                ('Application_Instructions', models.CharField(blank=True, max_length=255, null=255)),
                ('Application_URL_Email', models.CharField(blank=True, max_length=255, null=255)),
                ('Benefits', models.CharField(blank=True, max_length=255, null=255)),
                ('Company_Logo_base64', models.TextField(blank=True, null=True)),
                ('Company_Description', models.CharField(blank=True, max_length=255, null=255)),
                ('Contact_Information', models.CharField(blank=True, max_length=255, null=255)),
                ('Tags_Keywords', models.CharField(blank=True, max_length=255, null=255)),
                ('Job_ID', models.CharField(blank=True, max_length=255, null=255)),
                ('Job_Posting_Date', models.CharField(blank=True, max_length=255, null=255)),
                ('Expiration_Date', models.CharField(blank=True, max_length=255, null=255)),
            ],
        ),
    ]
