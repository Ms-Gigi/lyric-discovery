import sys
import os

# Add the 'src' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from lyric_finder.scraper import search_lyrics_snippet
import csv

def export_to_csv(results, filename="results.csv"):
    """
    Export list of song result dictionaries to a CSV file.
    """
    if not results:
        print("⚠️ No results to export.")
        return

    keys = results[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n✅ Results exported to {filename}")

if __name__ == "__main__":
    print("🎵 Welcome to Lyric Finder 🎵")
    snippet = input("Enter a snippet of lyrics: ")

    results = search_lyrics_snippet(snippet)

    if results:
        print("\n🎶 Matching Results:")
        for idx, song in enumerate(results, 1):
            print(f"{idx}. {song['title']} — {song['artist']}")
            print(f"   🔗 {song['link']}")

        # Ask if user wants to view full lyrics
        view = input("\n👀 View full lyrics for a song? Enter number (or press Enter to skip): ").strip()
        if view.isdigit():
            song_idx = int(view) - 1
            if 0 <= song_idx < len(results):
                selected_song = results[song_idx]
                print(f"\n📖 Fetching full lyrics for: {selected_song['title']} by {selected_song['artist']}")
                lyrics = get_full_lyrics(selected_song['link'])
                if lyrics:
                    print("\n🎤 Full Lyrics:\n")
                    print(lyrics[:3000])  # Show first 3000 chars (to avoid overwhelming)
                else:
                    print("❌ Couldn't retrieve the lyrics.")
            else:
                print("❌ Invalid selection.")

        # Offer CSV export
        export = input("\n📁 Export results to CSV? (y/n): ").lower()
        if export == 'y':
            export_to_csv(results)
    else:
        print("😔 No matches found.")