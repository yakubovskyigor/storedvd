from django.contrib import admin

from shop.models import Photo, Article, Single, WriteComment

admin.site.register(Photo)
# admin.site.register(Article)
admin.site.register(Single)
# admin.site.register(WriteComment)


# class DateFilter(admin.SimpleListFilter):
#     title = 'Дата'
#     parameter_name = "date"
#
#     def lookups(self, request, model_admin):
#
#         return (
#             ('01', 'январь'),
#             ("02", "февраль"),
#         )
#
#
#         # filters = []
#         # article = Article.objects.order_by('date').last()
#         # return filters
#
#     def queryset(self, request, queryset):
#         if not self.value():
#             return queryset
#         value = self.value()
#         return queryset.filter(value)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    search_fields = ['title']
    list_filter = ('date',)


class WriteCommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'email')
    list_filter = ('status',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(WriteComment, WriteCommentAdmin)