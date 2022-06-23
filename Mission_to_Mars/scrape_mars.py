# Dependencies
from bs4 import BeautifulSoup
import requests

def scrape():
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
    featured_image_url = url + featured_image_url
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
    url2 = 'https://marshemispheres.com/cerberus.html'
    url3 = 'https://marshemispheres.com/cerberus.html'
    url4 = 'https://marshemispheres.com/cerberus.html'
    # Retrieve page with the requests module
    response1 = requests.get(url1)
    browser.visit(1url)
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
    img1 = soup.find('img', class_='wide-image')['src']
    title1 = soup.find('h2', class_='title').text
    img2 = soup.find('img', class_='wide-image')['src']
    title2 = soup.find('h2', class_='title').text
    img3 = soup.find('img', class_='wide-image')['src']
    title3 = soup.find('h2', class_='title').text
    img4 = soup.find('img', class_='wide-image')['src']
    title4 = soup.find('h2', class_='title').text
    hemisphere_image_urls = [
        {"title": img1, "img_url": title1},
        {"title": img2, "img_url": title2},
        {"title": img3, "img_url": title3},
        {"title": img4, "img_url": title4},
    ]

    #Results variables
    mars_data = [
        {"articles": articles[0]},
        {"featured_image": featured_image_url},
        {"mars_info": mars_info},
        {"images_urls": hemisphere_image_urls}
    }

    return mars_data