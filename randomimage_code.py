import requests
from bs4 import BeautifulSoup

def get_sample_image(query):
    # Construct the URL for Google Images search
    url = f"https://www.google.com/search?hl=en&tbm=isch&q={query}"
    
    # Set a user-agent to avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the first image element
    image_element = soup.find('img')
    
    if image_element and 'src' in image_element.attrs:
        # Get the image URL
        image_url = image_element['src']
        return image_url
    else:
        return None

# Example usage
query = "puppies"
image_url = get_sample_image(query)

if image_url:
    print("Sample Image URL:", image_url)
else:
    print("No image found.")
