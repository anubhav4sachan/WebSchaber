# -*- coding: utf-8 -*-
# 
from bs4 import BeautifulSoup
import requests as re
import os

term = str(input("Enter the search term:")) 
param = {"q": term}

#Directory Settings
dir_name = term.replace(" ", "_").lower()
if not os.path.isdir(dir_name):
    os.makedirs(dir_name)
    
# Web Text Scraping
try:
    rt = re.get("https://www.bing.com/search", params = param)
    soupt = BeautifulSoup(rt.text, "html.parser")
    '''
    print(soupt.prettify())        #To print just the text. 
    It is not possible to write the whole of 'bd.prettify()' using the normal 
    input and output streams as they require string arguments to be passed on.
    '''
except:
    print("Internet Disconnected. Connect to download text.")

results = soupt.find("ol", {"id":"b_results"})
lists = results.findAll("li", {"class":"b_algo"})
file = open("./"+ dir_name + "/" + term +".txt", 'w')
file.close()
for item in lists:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]
    if item_text and item_href:
        print(item_text + "\n" + item_href + "\n")
        file = open("./"+ dir_name + "/" + term +".txt", 'a')
        file.write(item_text + "\n" + item_href + "\n\n")
        file.close()
        
# Web Images Scraping
from PIL import Image
from io import BytesIO
try:
    ri = re.get("https://www.bing.com/images/search", params = param)
    soupi = BeautifulSoup(ri.text, "html.parser")
    links = soupi.findAll("a", {"class":"thumb"})
    for item in links:
        try:
            img_obj = re.get(item.attrs["href"])
            print("Downloading: ", item.attrs["href"])
            title = item["href"].split("/")[-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./"+ dir_name + "/" + title, img.format)
            except:
                print("Could not Save :\'(")
        except:
            print("Image cannot be requested.")
except:
    print("Internet Disconnected. Connect to download images.")