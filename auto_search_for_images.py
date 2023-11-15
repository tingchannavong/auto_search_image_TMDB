import openpyxl
import requests
import os
import pandas as pd

def download_movie_image(movie_name, save_folder='movie_images'):
    # Ensure the folder for saving images exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # TMDB API configuration
    api_key = 'YOUR_TMDB_API_KEY'  # Replace with your TMDB API key
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
        else:
            print(f"Failed to download image. Status code: {image_response.status_code}")
    else:
        print(f"Movie '{movie_name}' not found or an error occurred.")

# Example usage
movie_name_to_search = 'Inception'
download_movie_image(movie_name_to_search)

# Open the Excel file
excel_file_path = "C:\\Users\\thipphaphone.c\\Desktop\\Learning\\movie_list.xlsx"
workbook = openpyxl.load_workbook(excel_file_path)
worksheet = workbook.active

#Image folder path
folder_path = "C:\\Users\\thipphaphone.c\\Desktop\\Learning\\images"

# Iterate through the rows in the spreadsheet

for row in worksheet.iter_rows(min_row=3, values_only=True):
    movie_title, _ = row[:2]

    # Construct a search query URL for TMDb
    query = movie_title.replace(' ', '+')
    url = f'https://api.themoviedb.org/3/search/movie?api_key=YOUR_API_KEY&query={query}'

    # Send a GET request to the API
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Determine the file extension from the content type
        content_type = response.headers['content-type']
        file_extension = content_type.split('/')[1]

        # Generate a unique filename
        file_number = len(os.listdir(folder_path)) + 1
        filename = f"m{file_number}.{file_extension}"

        # Save the image to the specified folder
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Image saved as {filename} in {folder_path}")

        # Update the Excel file
        worksheet.cell(row=row[2].row, column=2, value=image_url)
        print(f"Excel file updated with {filename} in column D, row {row}")
    else:
        print(f"Failed to download image. Status code: {response.status_code}")

# Save the modified Excel file
workbook.save('movie_list_with_images.xlsx')

  # # Check if there are results
    # if data['results']:
    #     # Extract the image URL for the first result
    #     image_url = f"https://image.tmdb.org/t/p/w500{data['results'][0]['poster_path']}"

    #     # Update the Excel spreadsheet with the image URL
    #     worksheet.cell(row=row[0].row, column=2, value=image_url)