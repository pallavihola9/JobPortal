# registration/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'full_name', 'is_active', 'is_admin', 'is_staff', 'terms_and_conditions')
    search_fields = ('email', 'full_name')
    list_filter = ('is_active', 'is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff')}),
        ('Terms and Conditions', {'fields': ('terms_and_conditions',)}),  # Add this line

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2', 'terms_and_conditions'),
        }),
    )
    ordering = ('email',)
    
    # Customize filter_horizontal based on your model's attributes
    filter_horizontal = ()

    # Optionally, you can add other related fields here if needed
    # filter_horizontal = ('some_related_field',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            # Creating a new user, so don't display 'user_permissions' and 'groups' fields
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)


admin.site.register(Employer)
admin.site.register(MyProfile)
admin.site.register(Course)
admin.site.register(ProfileHighlighter)
admin.site.register(BoostnowProfileForm)
admin.site.register(AdvancedJobSearch)
admin.site.register(JobPosting)
admin.site.register(AddBlogs)  
