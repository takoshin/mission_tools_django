from django.contrib import admin
from .models import User, LostArticle
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


class LostArticleAdmin(admin.ModelAdmin):
    fields = (
        'lost_article_name',
        'place',
        'discoverer_name',
        'customer_name',
        'phone_number',
        'return_date',
        'staff_name',
        'returned',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )



admin.site.register(User, UserAdmin)
admin.site.register(LostArticle, LostArticleAdmin)