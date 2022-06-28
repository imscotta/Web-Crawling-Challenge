# Import the dependencies.
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager

# Dependencies
from bs4 import BeautifulSoup
import requests

def scrape():
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #MArs news
    # URL of page to be scraped
    url = 'https://redplanetscience.com/'
    # Retrieve page with the requests module
    response = requests.get(url)
    browser.visit(url)
    html = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')
    # Examine the results, then determine element that contains sought info
    print(soup.prettify())
    # results are returned as an iterable list
    results = soup.find_all('div', class_='list_text')
    articles = []
    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return article title and description
            title = result.find('div', class_='content_title').text
            description = result.find('div', class_='article_teaser_body').text

            # Print results only if title, price, and link are available
            if (title and description):
                print('-------------')
                print(title)
                print(description)
                
            # Dictionary to be added to list
            post = {
                'title': title,
                'description': description,
            }

            articles.append(post)
                
        except AttributeError as e:
            print(e)
    print(articles)

    #JPL Mars
    # URL of page to be scraped
    url = 'https://spaceimages-mars.com'
    # Retrieve page with the requests module
    response = requests.get(url)
    browser.visit(url)
    html = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')
    # Examine the results, then determine element that contains sought info
    print(soup.prettify())
    #find the featured image, its actually not in the html
    featured_image_url = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = url + "/" + featured_image_url
    print(featured_image_url)

    #Mars Facts
    # URL of page to be scraped
    url = 'https://galaxyfacts-mars.com'
    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(response.text, 'html.parser')
    # Examine the results, then determine element that contains sought info
    print(soup.prettify())
    # results are returned as an iterable list
    results = soup.find_all('tr')
    mars_info = []
    # Loop through returned results
    for result in results:
        # Error handling
        try:
            # Identify and return values of header and text
            title = result.find('th').text
            content = result.find('td').text

            # Print results only if title, price, and link are available
            if (title and content):
                print('-------------')
                print(title)
                print(content)
                
            # Dictionary to be inserted as a MongoDB document
            post = {
                'title': title,
                'content': content,
            }
            
            mars_info.append(post)
                        
        except AttributeError as e:
            print(e)

    #Mars Hemisphere
    # URL of page to be scraped
    url1 = 'https://marshemispheres.com/cerberus.html'
    url2 = 'https://marshemispheres.com/schiaparelli.html'
    url3 = 'https://marshemispheres.com/syrtis.html'
    url4 = 'https://marshemispheres.com/valles.html'
    # Retrieve page with the requests module
    response1 = requests.get(url1)
    browser.visit(url1)
    html1 = browser.html
    response2 = requests.get(url2)
    browser.visit(url2)
    html2 = browser.html
    response3 = requests.get(url3)
    browser.visit(url3)
    html3 = browser.html
    response4 = requests.get(url4)
    browser.visit(url4)
    html4 = browser.html
    # Create BeautifulSoup object; parse with 'html.parser'
    soup1 = BeautifulSoup(html1, 'html.parser')
    soup2 = BeautifulSoup(html2, 'html.parser')
    soup3 = BeautifulSoup(html3, 'html.parser')
    soup4 = BeautifulSoup(html4, 'html.parser')
    # Examine the results, then determine element that contains sought info
    print(soup1.prettify())
    print(soup2.prettify())
    print(soup3.prettify())
    print(soup4.prettify())
    # find images and titles
    img1 = soup1.find('img', class_='wide-image')['src']
    title1 = soup1.find('h2', class_='title').text
    img2 = soup2.find('img', class_='wide-image')['src']
    title2 = soup2.find('h2', class_='title').text
    img3 = soup3.find('img', class_='wide-image')['src']
    title3 = soup3.find('h2', class_='title').text
    img4 = soup4.find('img', class_='wide-image')['src']
    title4 = soup4.find('h2', class_='title').text
    hemisphere_image_urls = [
        {"title": title1, "img_url": url1 + "/" + img1},
        {"title": title2, "img_url": url2 + "/" + img2},
        {"title": title3, "img_url": url3 + "/" + img3},
        {"title": title4, "img_url": url4 + "/" + img4},
    ]
    #Results variables
    mars_data = {
        "articles": articles[0],
        "featured_image": featured_image_url,
        "mars_info": mars_info,
        "images_urls": hemisphere_image_urls
    }
    print(mars_data)
    return mars_data