import requests
import os

def download_tv_show_image(tv_show_name, save_folder=None, year=None):
    
    save_folder = save_folder or "C:\\Users\\thipphaphone.c\\Desktop\\Learning\\series_images"

    # Ensure the folder for saving images exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # TMDB API configuration
    api_key = '80a500d30241b4584b32e52123f2fa73'  # Replace with your TMDB API key
    base_url = 'https://api.themoviedb.org/3'
    search_url = f'{base_url}/search/tv'

    # Search for the TV show
    params = {'api_key': api_key, 'query': tv_show_name, 'year': year}
    response = requests.get(search_url, params=params)
    data = response.json()

    # Check if the search was successful
    if response.status_code == 200 and data['results']:
        # Get the first result (assuming it's the most relevant)
        tv_show_id = data['results'][0]['id']

        # Get TV show details
        details_url = f'{base_url}/tv/{tv_show_id}'
        params = {'api_key': api_key}
        response = requests.get(details_url, params=params)
        details = response.json()

        # Get the poster path
        poster_path = details['poster_path']

        # Download the image
        image_url = f'https://image.tmdb.org/t/p/original{poster_path}'
        image_response = requests.get(image_url)

        # Save the image to the specified folder
        if image_response.status_code == 200:
            image_filename = f'{save_folder}/{tv_show_name.replace(" ", "_")}_poster.jpg'
            with open(image_filename, 'wb') as image_file:
                image_file.write(image_response.content)
            print(f"Image saved as {image_filename}")
            return image_filename
        else:
            print(f"Failed to download image. Status code: {image_response.status_code}")
    else:
        print(f"TV show '{tv_show_name}' not found or an error occurred.")

# Year Parameter does not work sadly ;(




