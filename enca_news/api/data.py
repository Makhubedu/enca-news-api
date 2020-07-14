import requests
from bs4 import BeautifulSoup


class GetData:
    def __init__(self, category,*args, **kwargs):
        self.html = requests.get(f"https://www.sabcnews.com/sabcnews/category/{category}/").text
        self.soup = BeautifulSoup(self.html,'html.parser')
       

    def getContent(self):
        self.title = self.soup.find("h1", class_='rpw2e-title').get_text()
        self.lead_content = self.soup.find('div',class_='category_lead_excerpt').get_text()
        self.img = self.soup.find('img',class_='wp-post-image')['src']
        try:
            self.image_caption = self.soup.find('div', class_='featured_caption').get_text()
        except:
            self.image_caption = ''
            print("Some thing is wrong.")
        
        return {
            "title" : self.title,
            "lead_content" : self.lead_content,
            "image" : self.img,
            "image_caption": self.image_caption
        }

    
    def getImages(self):
        source_image = []
        self.thumb_images = self.soup.findAll('img',class_='size-thumb')
        for i in range(len(self.thumb_images)):
            source_image.append(self.thumb_images[i]['src'])
        return source_image

    def getBodyTitle(self):
        source_title = []
        body_title = self.soup.findAll('span',class_='sabc_cat_list_item_title')
        for i in range(len(self.thumb_images)):
            source_title.append(body_title[i].get_text())
        return source_title
    def summary(self):
        source_sammary = []
        summary = self.soup.findAll('p',class_='sabc_cat_list_item_summary')
        for i in range(len(self.thumb_images)):
            source_sammary.append(summary[i].get_text()[:75])
        return source_sammary
    def links(self):
        source_link =[]
        links = self.soup.findAll('span',class_='sabc_cat_list_item_title')
        for link in links:
            new_link = link.find('a')['href']
            source_link.append(new_link)
        return source_link
    
    
    
    

    

    
        
        

    