from django.contrib import admin
from django_quill.fields import QuillField
from .models import Post
from django import forms

# Criando um formulário customizado para o admin
class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

# Definindo a classe admin
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'created_at', 'updated_at', 'is_highlighted')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    class Media:
        css = {
            'all': ('css/admin.css',)  # Certifique-se de que este arquivo CSS existe em static/css/admin/
        }

admin.site.register(Post, PostAdmin)
