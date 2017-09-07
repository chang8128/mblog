from django.contrib import admin
from .models import Post
from .models import Stock0

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'pub_date')
	
	
class Stock0Admin(admin.ModelAdmin):
	list_display = ('ai_date', 'stockname', 'code', 'industry', 'percent', 'buyprice')


admin.site.register(Post, PostAdmin)
admin.site.register(Stock0, Stock0Admin)