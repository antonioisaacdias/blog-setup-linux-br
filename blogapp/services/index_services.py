from datetime import datetime

def short_format_datatime(posts_json):
    for post in posts_json:
        date_string = post['created_at']    
        date_object = datetime.fromisoformat(date_string)        
        formatted_date = date_object.strftime("%d/%m/%y às %H:%M")
        post['created_at'] = formatted_date 

    return posts_json
