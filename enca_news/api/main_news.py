from bs4 import BeautifulSoup
import requests

class BodyNews:
    def __init__(self, url):
        self.url = url
        self.html = requests.get(str(url)).text
        self.soup = BeautifulSoup(self.html,'html.parser')
       
    def getMainNews(self):
        try:
            content = self.soup.find('div', class_ = "post-content").get_text()
        except:
            content = ''
        return content
    

