from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

def search_lyrics_snippet(snippet, driver_path='C:/Users/adebu/PycharmProjects/lyric-discovery/chromedriver-win64/chromedriver.exe'):
    """
    Search Lyrics.com for a lyrics snippet and return a list of dictionaries
    with song title, artist, and link to full lyrics.
    """
    # Configure headless browser (runs without opening Chrome window)
    options = Options()
    options.add_argument("--headless")
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Format search URL
        query = snippet.replace(' ', '+')
        url = f"https://www.lyrics.com/serp.php?st={query}&qtype=2"

        # Open the search page
        driver.get(url)
        time.sleep(2)  # Wait for content to load

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all search results
        results = soup.find_all('td', class_='tal qx')

        matches = []
        for result in results:
            title_tag = result.find('strong')
            artist_tag = result.find('a')
            link_tag = result.find('a')

            if title_tag and artist_tag and link_tag:
                title = title_tag.text.strip()
                artist = artist_tag.text.strip()
                link = "https://www.lyrics.com" + link_tag['href']

                matches.append({
                    "title": title,
                    "artist": artist,
                    "link": link
                })

        return matches

    except Exception as e:
        print("Error while scraping:", e)
        return []

    finally:
        driver.quit()  # Always close the browser session

import requests

def get_full_lyrics(link):
    """
    Given a full lyrics page URL, scrape and return the song's full lyrics.
    """
    try:
        response = requests.get(link)
        if response.status_code != 200:
            print(f"❌ Failed to load page: {link}")
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        # Lyrics are inside a <pre id="lyric-body-text"> tag
        lyrics_tag = soup.find('pre', id='lyric-body-text')
        if lyrics_tag:
            return lyrics_tag.get_text(strip=True)
        else:
            print("⚠️ Could not find lyrics on the page.")
            return None

    except Exception as e:
        print("Error fetching lyrics:", e)
        return None
