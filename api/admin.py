from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # Campos a serem exibidos na lista de posts no painel de administração
    list_display = ('title', 'author', 'created_at', 'updated_at')
    
    # Permite pesquisa por título e autor
    search_fields = ('title', 'author')
    
    # Permite filtrar os posts pela data de criação
    list_filter = ('created_at', 'author')
    
    # Campos que aparecem no formulário de criação/edição
    fields = ('title', 'subject', 'author', 'content', 'image', 'created_at', 'updated_at')
    
    # Campos somente leitura
    readonly_fields = ('created_at', 'updated_at')

    # Filtro de exibição para facilitar a navegação na lista
    ordering = ('-created_at',)  # Ordenar os posts pela data de criação (mais recente primeiro)

admin.site.register(Post, PostAdmin)
