from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm,CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
        # Add any additional fields here.
    )
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","password1", "password2", "is_staff", "is_superuser"),
            },
        ),
    )

    list_display = ('username','is_staff','is_superuser')

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Profile)