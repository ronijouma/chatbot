import requests
from bs4 import BeautifulSoup

def scrape_sigma_info():
    url = "https://www.sigma.se/sv/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = [h.text.strip() for h in soup.find_all("h2")]
        return headlines if headlines else ["No specific information found."]
    except requests.exceptions.RequestException as e:
        return [f"Error fetching information: {e}"]
