from django.contrib import admin
from .models import Article
# Register your models here.

#定制admin界面
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","content","authors","is_deleted","readed_num","created_time","last_time")
    #注意逗号，正序排列，  -id 倒叙
    ordering = ("id",)
admin.site.register(Article,ArticleAdmin)