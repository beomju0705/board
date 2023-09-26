import requests

def get_book_image(title, api_key):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {
        'q' : title,
        'key': api_key,
    }
    response = requests.get(base_url, params)
    data = response.json()
    
    if 'items' in data and 'imageLinks' in data['items'][0]['volumeInfo']:
        return data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
