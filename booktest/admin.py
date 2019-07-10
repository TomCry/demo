from django.contrib import admin
from .models import BookInfo, HeroInfo


# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'pub_date']
    # fields = ['btitle', 'bpub_date']
    fieldsets = (
        ('基本', {'fields': ('btitle', 'bpub_date')}),
        ('高级', {
            'fields': ['bread', 'bcomment', 'image'],
            'classes': ('collapse',)
        })
    )

@admin.register(HeroInfo)
class HeroInfoAdmin(admin.ModelAdmin):
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'hname', 'hcomment', 'hbook']
    list_filter = ['hname', 'hbook']
    search_fields = ['hname']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.site_header = "欢迎欢迎热烈欢迎"
admin.site.site_title = "Welcome!"
admin.site.index_title = "爱你呦"

