
import urllib.request
import urllib.error

def check_website(url):
    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0"}
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            print("Website is working!")
            print("Status Code:", response.status)

    except urllib.error.HTTPError as error:
        print("Website responded with an error.")
        print("Status Code:", error.code)

    except urllib.error.URLError:
        print("Website is unreachable.")

    except TimeoutError:
        print("Request timed out.")

    except ValueError:
        print("Invalid URL format.")

url = input("Enter website URL: ")

if not url.startswith(("http://", "https://")):
    url = "https://" + url

check_website(url)
