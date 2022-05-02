#! /usr/bin/env python3
import bs4
import requests

res = requests.get('https://www.amazon.com/dp/B08FQG96RP?ref=ppx_yo2ov_dt_b_product_details&th=1')
res.raise_for_status() #raise and exception if bad response

soup = bs4.BeautifulSoup(res.text, 'html.parser') # res.text -> the html from the page, and bs4.Beautifu... reutrns a beautiful soup object. You also don't have to pass a second param for html

elems = soup.select('#corePrice_feature_div > div > span > span:nth-child(2)') #This is how we select specific css selector for html elements
#returns a list of objects
elems[0].text.strip() # each elem should have a text property from which we can get the text and strip the whitespace away fomr
