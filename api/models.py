from uuid import uuid4
from django.db import models
from django_quill.fields import QuillField
from django.utils.text import slugify

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, null=False, blank=False, unique=True)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Título', unique=True)
    slug = models.SlugField(blank=True ,unique=True)  # O slug será gerado automaticamente
    subject = models.CharField(max_length=100, null=False, blank=False, verbose_name= 'Assunto')
    author = models.CharField(max_length=80, null=False, blank=False, verbose_name='Autor')
    resume = models.TextField(null=False, blank=False, verbose_name='Resumo')
    content = QuillField(blank=True, null=True, verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Atualizado em')
    image = models.ImageField(upload_to='posts/', default='posts/Linux_logo.jpg', verbose_name='Imagem')
    is_highlighted = models.BooleanField(default=False, verbose_name='Ativo no carossel')

    class Meta:
        db_table = 'posts'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            # Garantir que o slug seja único
            original_slug = self.slug
            counter = 1
            while Post.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)