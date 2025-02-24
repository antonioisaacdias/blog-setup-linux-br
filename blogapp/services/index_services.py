from datetime import datetime

def format_datatime(posts_json):
    for post in posts_json:
        date_string = post['created_at']
        date_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_date = date_object.strftime("%d/%m/%y às %H:%M")
        post['created_at'] = formatted_date 
    return posts_json