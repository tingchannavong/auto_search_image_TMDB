import requests
import os

def download_movie_image(movie_name, save_folder=None):

    save_folder = save_folder or "C:\\Users\\thipphaphone.c\\Desktop\\Learning\\incorrect_images"

    # Ensure the folder for saving images exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # TMDB API configuration
    api_key = 'xxxxxxxxxxxxxxxxxxxx'  # Replace with your TMDB API key
    base_url = 'https://api.themoviedb.org/3'
    search_url = f'{base_url}/search/movie'

    # Search for the movie
    params = {'api_key': api_key, 'query': movie_name}
    response = requests.get(search_url, params=params)
    data = response.json()

    # Check if the search was successful
    if response.status_code == 200 and data['results']:
        # Get the first result (assuming it's the most relevant)
        movie_id = data['results'][0]['id']

        # Get movie details
        details_url = f'{base_url}/movie/{movie_id}'
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
            image_filename = f'{save_folder}/{movie_name.replace(" ", "_")}_poster.jpg'
            with open(image_filename, 'wb') as image_file:
                image_file.write(image_response.content)
            print(f"Image saved as {image_filename}")
            return image_filename
        else:
            print(f"Failed to download image. Status code: {image_response.status_code}")
    else:
        print(f"Movie '{movie_name}' not found or an error occurred.")


    
