import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten_url(self, original_url):
        hash_object = hashlib.md5(original_url.encode())
        short_hash = hash_object.hexdigest()[:8]
        shortened_url = f"https://your-short-domain/{short_hash}"
        self.urls[shortened_url] = original_url
        return shortened_url

    def redirect(self, shortened_url):
        if shortened_url in self.urls:
            return self.urls[shortened_url]
        else:
            return None

# Example usage
def main():
    shortener = URLShortener()
    original_url = "ww.facebook.com"

    # Shorten the URL
    shortened_url = shortener