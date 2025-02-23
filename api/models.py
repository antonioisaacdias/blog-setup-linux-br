from uuid import uuid4
from django.db import models
from django_quill.fields import QuillField

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False, null=False, blank=False, unique=True)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Título')
    subject = models.CharField(max_length=100, null=False, blank=False, verbose_name= 'Assunto')
    author = models.CharField(max_length=80, null=False, blank=False, verbose_name='Autor')
    content = QuillField(blank=True, null=True, verbose_name='Conteúdo')
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, null=False, verbose_name='Atualizado em')
    image = models.ImageField(upload_to='posts/', default='posts/Linux_logo.jpg', verbose_name='Imagem')
    is_highlighted = models.BooleanField(default=False, verbose_name='Ativo no carossel')

    class Meta:
        db_table = 'posts'