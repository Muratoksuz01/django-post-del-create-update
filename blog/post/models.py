from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField



# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120,verbose_name="Başlık")#verbose_name kullanıcıya gösterilen kısım yanı kullanıcı Başlık görecek admin sayfasında
    content=RichTextField(verbose_name="İçerik")
    publishing_date=models.DateField(verbose_name="yayınlanma tarihi",auto_now_add=True)
    image=models.ImageField(null=True,blank=True)
    slug=models.SlugField(unique=True,editable=False,max_length=130)
    user=models.ForeignKey("auth.User",verbose_name="Yazar",on_delete=models.CASCADE,related_name="posts")
    def __str__(self):#bir kac post yaptıgında admin sayfasında postun title kısmını gösteriyor 
        return self.title
    def get_absolute_url(self):
        return f"/post/{self.slug}"
    def get_create_url(self):
        return f"/post/create"
    def get_update_url(self):
        return f"/post/{self.slug}/update"
    def get_delete_url(self):
        return f"/post/{self.slug}/delete "
    def save(self,*args,**kwargs):
        self.slug=self.unigue_slug()
        return super(Post,self).save(*args,**kwargs)
    def unigue_slug(self):
        slug=slugify(self.title.replace("ı","i"))
        unigue_slug=slug
        counter=1
        while Post.objects.filter(slug=unigue_slug).exists():
            unigue_slug=f"{slug}-{counter}"
            counter+=1
        return unigue_slug
    class Meta:#burada postları sıraladık 
        ordering=["-id"]#buraya '-' işareti ters sırala demek burada id buyuk olan en basa gelecek 

class Comment(models.Model):
    post=models.ForeignKey('post.Post',related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200,verbose_name="İsim")
    content=models.TextField(verbose_name="Yorum") 
    created_date=models.DateField(auto_now_add=True)        



