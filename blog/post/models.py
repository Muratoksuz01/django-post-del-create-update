from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120,verbose_name="Başlık")#verbose_name kullanıcıya gösterilen kısım yanı kullanıcı Başlık görecek admin sayfasında
    content=models.TextField(verbose_name="İçerik")
    publishing_date=models.DateField(verbose_name="yayınlanma tarihi",auto_now_add=True)

    def __str__(self):#bir kac post yaptıgında admin sayfasında postun title kısmını gösteriyor 
        return self.title
    def get_absolute_url(self):
        return f"/post/datail/{self.id}"
    def get_create_url(self):
        return f"/post/create"
    def get_update_url(self):
        return f"/post/{self.id}/update"
    def get_delete_url(self):
        return f"/post/{self.id}/delete "
