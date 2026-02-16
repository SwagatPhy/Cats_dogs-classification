import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup

def get_url(url):
  r = requests.get(url)
  return r.text


query = 'cats'
url = f'https://www.google.com/search?q={query}&sca_esv=44ea38d9bdd60463&hl=EN&biw=2560&bih=1230&udm=2&sxsrf=ANbL-n7xnID1YG5ZWApwAabL91eE7wwikA%3A1770297871941&ei=D5qEaa6ROfPk2roP2N_X4QU&ved=0ahUKEwju1La-ucKSAxVzslYBHdjvNVwQ4dUDCBQ&uact=5&oq=dogs&gs_lp=Egtnd3Mtd2l6LWltZyIEZG9nczIHECMYJxjJAjIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBUiAA1AAWJECcAB4AJABAJgBlwKgAfMDqgEDMi0yuAEDyAEA-AEBmAICoAKFBMICCBAAGIAEGLEDwgIFEAAYgASYAwCSBwMyLTKgB80NsgcDMi0yuAeFBMIHBTItMS4xyAcOgAgA&sclient=gws-wiz-img'
print(url)

headers = {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36'}
google_api_key = 'AIzaSyCbaw7hwfNKYo4OAd0Sn23zvmRLvjzwXm8'



url_text = get_url(url,headers=headers)
soup = BeautifulSoup(url_text, 'html.parser')

# urls = []
# for item in soup.find_all('img'):
#   # print(item['src'])
#   urls.append(item['src'])

# print(len(urls))


