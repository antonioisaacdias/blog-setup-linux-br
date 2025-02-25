from datetime import datetime
import locale

# Define o locale para português do Brasil
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")

def long_format_datatime(post_json):     
    # Converte as datas corretamente aceitando timezone
    created_at_obj = datetime.fromisoformat(post_json['created_at'])
    updated_at_obj = datetime.fromisoformat(post_json['updated_at'])
    
    # Formata no estilo brasileiro com nome do mês em português
    post_json['created_at'] = created_at_obj.strftime("%d de %B de %Y às %H:%M")
    post_json['updated_at'] = updated_at_obj.strftime("%d de %B de %Y às %H:%M")
    
    return post_json
