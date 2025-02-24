from django.contrib import admin
from django_quill.fields import QuillField
from .models import Post
from django import forms
from django.utils.text import slugify

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    slug = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        label='Slug'
    )

    def clean_slug(self):
        if self.instance.pk and not self.cleaned_data.get('slug'):
            slug = slugify(self.instance.title)
            return slug
        return self.cleaned_data.get('slug')

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'created_at', 'updated_at', 'is_highlighted', 'slug')  # Exibindo o slug na lista
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at', 'slug')  # Tornando o slug readonly
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'subject', 'resume', 'content', 'author', 'image', 'is_highlighted', 'created_at', 'updated_at')
        }),
    )

    class Media:
        css = {
            'all': ('css/admin.css',)  # Certifique-se de que este arquivo CSS existe em static/css/admin/
        }

admin.site.register(Post, PostAdmin)

