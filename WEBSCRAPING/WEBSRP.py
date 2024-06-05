# importing libraries
from bs4 import BeautifulSoup
import http.client
import ssl

def fetch_html(url):
    # Extract host and path from URL
    host = url.split("//")[1].split("/")[0]
    path = "/" + "/".join(url.split("//")[1].split("/")[1:])
    
    # Establish a connection and make the request
    context = ssl.create_default_context()
    conn = http.client.HTTPSConnection(host, context=context)
    conn.request("GET", path, headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'
    })
    response = conn.getresponse()
    if response.status == 200:
        html = response.read().decode('utf-8')
        conn.close()
        return html
    else:
        conn.close()
        return None

def main(URL):
    # opening our output file in append mode
    File = open("out.csv", "a")

    # Fetch the HTML content
    webpage = fetch_html(URL)

    if webpage:
        # Creating the Soup Object containing all data
        soup = BeautifulSoup(webpage, "html.parser")

        # retrieving product title
        try:
            # Outer Tag Object
            title = soup.find("span", attrs={"id": 'productTitle'})
            # Inner NavigableString Object
            title_value = title.string
            # Title as a string value
            title_string = title_value.strip().replace(',', '')
        except AttributeError:
            title_string = "NA"
        print("Product Title = ", title_string)

        # saving the title in the file
        File.write(f"{title_string},")

        # retrieving price
        try:
            price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip().replace(',', '')
        except AttributeError:
            price = "NA"
        print("Product Price = ", price)

        # saving the price
        File.write(f"{price},")

        # retrieving product rating
        try:
            rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip().replace(',', '')
        except AttributeError:
            try:
                rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip().replace(',', '')
            except:
                rating = "NA"
        print("Overall Rating = ", rating)

        # saving the rating
        File.write(f"{rating},")

        # retrieving review count
        try:
            review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip().replace(',', '')
        except AttributeError:
            review_count = "NA"
        print("Total Reviews = ", review_count)

        # saving the review count
        File.write(f"{review_count},")

        # retrieving availability status
        try:
            available = soup.find("div", attrs={'id': 'availability'})
            available = available.find("span").string.strip().replace(',', '')
        except AttributeError:
            available = "NA"
        print("Availability = ", available)

        # saving the availability and closing the line
        File.write(f"{available},\n")

    # closing the file
    File.close()

if __name__ == '__main__':
    # opening our url file to access URLs
    file = open("url.txt", "r")
    # iterating over the urls
    for links in file.readlines():
        main(links.strip())
