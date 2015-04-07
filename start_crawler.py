# fisrt sys arg is target websit..
import sys
import urllib2
import BeautifulSoup

#class Crawler(object):
#    def __init__(self,args):


def get_content(url):
    if url[:4] == "http":
        source = urllib2.urlopen(url)
    else: 
         source = urllib2.urlopen('http://'+ url)

    content = source.read()
    soup = BeautifulSoup.BeautifulSoup(content) 
    with open('htmlContent.txt','w+') as f:
        f.write(content)
    print(soup)
    return soup

def get_price(soup):
    itemPrice = soup.findAll('price')
    print(itemPrice)
    for price in itemPrice:
        print price

if __name__ == "__main__":
    web  = sys.argv[1]
    soup = get_content(web)
    print("here")
    get_price(soup)
    




