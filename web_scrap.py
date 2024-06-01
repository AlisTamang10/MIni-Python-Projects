import re
import urllib.request

def scrape_website(url):
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')

        # Search for the <h2 class="section-title font-dosis">Top Jobs</h2> tag
        pattern = r'<h2 class="section-title font-dosis">Top Jobs</h2>'
        match = re.search(pattern, html)

        if match:
            print('Found <h2 class="section-title font-dosis">Top Jobs</h2> tag.')
        else:
            print('Tag not found.')

    except urllib.error.HTTPError as e:
        print(f'An error occurred: {e.code} {e.reason}')

# Example usage
url = 'https://www.jobsnepal.com/'
scrape_website(url)