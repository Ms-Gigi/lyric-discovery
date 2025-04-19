# 🎵 Lyric Finder & "Guess the Song" Game

Ever had a lyric stuck in your head but couldn’t remember the song?  
Or wanted to test your music memory with a fun challenge?

**Lyric Finder** is a tool that does both:  
✅ Helps you find songs from just a lyric snippet  
🎲 And lets you play a "Guess the Song" mini-game for fun

---

## ✨ Features

- 🔍 **Lyrics Discovery Tool**  
  Input a snippet of lyrics and get back the **song title**, **artist**, **full lyrics**, and a link to the Genius.com page.

- 🎮 **Guess-the-Song Game**  
  Get random lines from a song’s lyrics and try to guess the **title or artist** — it's like trivia for music lovers.

- 🔀 **Random Song Selection**  
  Pulls from the top Genius matches to make each round unique.

- 📎 **Genius Link After Guess**  
  See the full song if you guess wrong (or right!).

---

## 🎯 Who It's For

- Anyone who’s ever said:  
  *“What’s that song that goes...?”*  
- Trivia fans who love a challenge  
- Devs looking to see web scraping + games in action

---

## 🛠️ Tech Stack

| Tool          | Purpose                             |
|---------------|-------------------------------------|
| `Python`      | Core language                       |
| `requests`    | Fetch Genius search + lyrics pages  |
| `BeautifulSoup` | Parse HTML from Genius            |
| `random`      | Randomize songs and lyric lines     |
| `sys`/`os`    | Handle module imports cleanly       |

---

## 🚀 How It Works

### 1. **Lyrics Lookup Mode**
```bash
🎤 Enter a lyrics snippet: i can't feel my face
🔗 Found Genius URL: https://genius.com/The-weeknd-cant-feel-my-face-lyrics
🎶 Title: Can't Feel My Face by The Weeknd
📃 Full lyrics printed below
```


## 🤖 Bonus: Selenium-Powered Lyric Search Bot

For fun and to showcase browser automation skills, this project includes a **Selenium-based lyric search bot**.

### What It Does:
- Opens [Genius.com](https://genius.com) in a real browser
- Types your lyrics snippet into the search bar
- Clicks on the first result
- Prints the song title from the lyrics page



### To Run:
```bash
python src/lyric_finder/selenium_lyrics_bot.py
