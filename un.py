import urllib.request
import re
from urllib.error import HTTPError

def fetch_html(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html_content = response.read().decode('utf-8')
        return html_content
    except HTTPError as e:
        print("HTTP Error:", e)
        return None
    except Exception as e:
        print("Error fetching URL:", e)
        return None

def extract_job_categories(html_content):
    if html_content:
        # Find all the <a> tags inside the <div> tag with class "col-md-6"
        job_categories = re.findall(r'<div class="col-md-6">(?:.*?)</div>', html_content, re.DOTALL)
        categories = []
        for job_category in job_categories:
            # Extract the text from each <a> tag
            category_text = re.findall(r'<a.*?>(.*?)</a>', job_category)
            categories.extend(category_text)
        return categories
    else:
        print("No HTML content to extract from.")
        return None

def main():
    url = "https://www.jobsnepal.com/"
    html_content = fetch_html(url)
    if html_content:
        job_categories = extract_job_categories(html_content)
        if job_categories:
            print("Job Categories:")
            for category in job_categories:
                print(category)
        else:
            print("No job categories found.")
    else:
        print("Failed to fetch HTML content.")      

if __name__ == "__main__":
    main() 