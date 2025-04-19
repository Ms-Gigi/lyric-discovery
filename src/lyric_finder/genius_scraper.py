import requests
from bs4 import BeautifulSoup
import random


# Headers to mimic a real browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

def search_genius_direct(query):
    """
    Search Genius using their internal API (no key needed) and return top song URL.
    """
    api_url = f"https://genius.com/api/search/multi?per_page=5&q={query.replace(' ', '%20')}"
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print("❌ Failed to fetch Genius search results.")
        return None

    data = response.json()
    urls = []

    sections = data.get('response', {}).get('sections', [])
    for section in sections:
        if section['type'] == 'song':
            hits = section.get('hits', [])
            for hit in hits:
                urls.append(hit['result']['url'])

    return random.choice(urls) if urls else None


def scrape_genius_lyrics(url):
    """
    Scrape lyrics, title, and artist from a Genius song page.
    """
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"❌ Failed to load Genius page: {url}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title and artist
    title_tag = soup.find('h1')
    artist_tag = soup.find('a', attrs={'href': lambda x: x and '/artists/' in x})


    # Gather all lyric containers
    lyrics_divs = soup.find_all('div', class_=lambda x: x and 'Lyrics__Container' in x)
    if not lyrics_divs:
        print("⚠️ Could not find lyrics on the page.")
        return None

    lyrics_lines = []
    for div in lyrics_divs:
        for br in div.find_all("br"):
            br.replace_with("\n")
        lyrics_lines.append(div.get_text(separator="\n", strip=True))

    lyrics = "\n".join(lyrics_lines)

    return {
        "title": title_tag.text.strip() if title_tag else "Unknown Title",
        "artist": artist_tag.text.strip() if artist_tag else "Unknown Artist",
        "lyrics": lyrics,
        "url": url
    }
