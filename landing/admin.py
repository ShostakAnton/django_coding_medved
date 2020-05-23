from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email"]
    # list_display = [field.name for field in Subscriber._meta.fields]
    # exclude = ["email"]  # не показывать поле на странице редактирования
    # fields = ["email"]  # показывать указаное поле на страниуе редактирования
    list_filter = ('name',)  # добавление фильтра

    search_fields = ['name', 'email']  # добавление поисковой строки

    # inlines = [FieldMappingInline]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscriberAdmin)
