import playwright.sync_api
import json
import os
from datetime import datetime

URL_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "config", "urls.csv")


def load_urls():
    with open(URL_FILE_PATH, "r") as f:
        urls = [line.strip() for line in f if line.strip()]
    return urls


def main():
    urls = load_urls()
    print("Starting browser screenshot for the following URLs:")
    for url in urls:
        print(f" - {url}")
    with playwright.sync_api.sync_playwright() as p:
        browser = p.chromium.launch()
        # Open browser page
        page = browser.new_page()
        for url in urls:
            # validate url
            if not url.startswith("http://") and not url.startswith("https://"):
                url_to_visit = f"https://{url}"
            else:
                url_to_visit = url
            print(f"Navigating to {url_to_visit}...")
            try:
                page.goto(url_to_visit)

                # Take screenshot and save with url and timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_filename = f"{url.replace('.', '_')}_{timestamp}.png"
                screenshot_dir = os.path.join(
                    os.path.dirname(__file__), "..", "screenshots"
                )
                screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
                os.makedirs(screenshot_dir, exist_ok=True)
                rel_path = os.path.relpath(
                    screenshot_path, os.path.join(os.path.dirname(__file__), "..")
                )
                print(f"Taking screenshot and saving to {rel_path}...")
                page.screenshot(path=screenshot_path, full_page=True)

            except Exception as e:
                print(f"Failed to take screenshot of {url}: {e}")
        # close browser
        page.close()
        browser.close()


if __name__ == "__main__":
    main()
