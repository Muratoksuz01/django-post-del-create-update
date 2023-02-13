from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display=["title","publishing_date","slug"]#admin sayfasında direkt görulecek kısım
    list_display_links=['publishing_date']#bu kısım link olacak basarsan direkt posta gideceksin
    list_filter=["publishing_date"]# sağ tarafta parametreye göre fitreleme kısmı cıkıyor
    search_fields=["title","content"]#en ustte arama cubugu geliyor title ve content iceriğini kolayca arayabilirsin
    list_editable=["title"]#admin sayfasında direk degişiklik yapabilmeni sağlıyor    
   # prepopulated_fields={ 'slug':("title",)}#admin panelinde slug tarafını titleye bağlı kıldık yanı title yazarken sen yukarıda asagıda sluug yazılacak otomatik
    class Meta:
        model=Post



admin.site.register(Post,PostAdmin)



