# enius_scraper import google_search_genius, scrape_genius_lyrics
from genius_scraper import search_genius_direct, scrape_genius_lyrics

snippet = input("🎤 Enter a lyrics snippet: ")
genius_url = search_genius_direct(snippet)

if genius_url:
    print(f"🔗 Found Genius URL: {genius_url}")
    song_data = scrape_genius_lyrics(genius_url)

    if song_data:
        print(f"\n🎶 {song_data['title']} by {song_data['artist']}")
        print(f"\n📃 Lyrics Preview:\n{song_data['lyrics'][:1000]}")
else:
    print("😔 No Genius page found.")
