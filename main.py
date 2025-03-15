# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
import requests


def main():
    print("Hello from uviolet!")
    response = requests.get("https://api.github.com")
    print(response.json())


if __name__ == "__main__":
    main()
