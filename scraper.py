import requests
from bs4 import BeautifulSoup

def main():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    html_content = response.text
    print("\n--- Piece of the HTML page: ---")
    print(html_content[:500])

if __name__ == "__main__":
    main()