from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account

class AccountAdmin(UserAdmin):
    # 관리자 화면
    list_display = ('phonenum', 'nickname', 'username', 'birthY', 'birthM', 'birthD', 'create_at', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('phonenum', 'username', 'nickname')
    readonly_fields = ('id', 'create_at', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)