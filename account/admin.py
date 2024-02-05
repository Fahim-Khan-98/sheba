from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "crimesection_admin", "entertainment_admin", "phone")
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('crimesection_admin', 'entertainment_admin', 'phone')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'crimesection_admin', 'entertainment_admin', 'phone'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
