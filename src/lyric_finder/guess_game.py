import sys
import os

# Add the 'src' folder to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import random
from lyric_finder.scraper import search_lyrics_snippet, get_full_lyrics

def play_guess_the_song(snippet):
    print("\n🎲 Welcome to Guess the Song!")

    # Get results for the lyric snippet
    results = search_lyrics_snippet(snippet)
    if not results:
        print("😔 No results found.")
        return

    # Randomly select one song from results
    song = random.choice(results)
    print(f"\n🔍 Fetching lyrics for one of the matches...")

    lyrics = get_full_lyrics(song["link"])
    if not lyrics:
        print("Could not fetch lyrics.")
        return

    # Split lyrics into lines
    lines = lyrics.split('\n')
    lines = [line.strip() for line in lines if line.strip()]  # remove empty ones

    if len(lines) < 3:
        print("🤷 Not enough lyrics to play.")
        return

    # Show a few random lines
    start_index = random.randint(0, len(lines) - 3)
    snippet_lines = lines[start_index:start_index + 3]

    print("\n🎤 Guess the song from this snippet:\n")
    for line in snippet_lines:
        print(f"  {line}")

    guess = input("\n🎯 Your guess (title or artist): ").lower().strip()

    correct_title = song["title"].lower()
    correct_artist = song["artist"].lower()

    if guess in correct_title or guess in correct_artist:
        print("✅ Correct!! 🎉")
    else:
        print("❌ Oof! The correct answer was:")
        print(f"• {song['title']} by {song['artist']}")
        print(f"🔗 {song['link']}")

    again = input("\n🔁 Play again? (y/n): ").lower()
    if again == 'y':
        play_guess_the_song(snippet)

from lyric_finder.guess_game import play_guess_the_song

if __name__ == "__main__":
    snippet = input("Enter a keyword to pull lyrics from: ")
    play_guess_the_song(snippet)
