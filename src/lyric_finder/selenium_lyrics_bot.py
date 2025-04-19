from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Update your local chromedriver path!
CHROMEDRIVER_PATH = "C:/Users/adebu/PycharmProjects/lyric-discovery/chromedriver-win64/chromedriver.exe"

def search_lyrics_snippet_with_selenium(snippet):
    service = Service(CHROMEDRIVER_PATH)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Optional: hide browser
    driver = webdriver.Chrome(service=service, options=options)

    try:
        print("🌐 Opening Genius...")
        driver.get("https://genius.com")

        # Wait a bit for page to load
        time.sleep(2)

        # Genius now shows a visible search input on the homepage
        search_input = driver.find_element(By.NAME, "q")
        search_input.send_keys(snippet)
        search_input.send_keys(Keys.RETURN)


        print("🔍 Searching for:", snippet)
        time.sleep(3)

        # Click on the first result
        first_result = driver.find_element(By.CLASS_NAME, "mini_card")
        first_result.click()

        print("🎯 Opening top result...")
        time.sleep(3)

        # Print the song title from the new page
        title = driver.find_element(By.TAG_NAME, "h1").text
        print("🎶 Song title:", title)

    except Exception as e:
        print("❌ Error:", e)
    finally:
        driver.quit()


# Example usage
if __name__ == "__main__":
    snippet = input("Enter a snippet of lyrics: ")
    search_lyrics_snippet_with_selenium(snippet)
