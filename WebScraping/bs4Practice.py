#! /usr/bin/env python3
import bs4
import requests

def getAmazonPrice(productUrl):
  res = requests.get(productUrl)
  res.raise_for_status
  soup = bs4.BeautifulSoup(res.text, 'html.parser')
  elems = soup.select('#corePrice_feature_div > div > span > span:nth-child(2)')
  return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/dp/B08FQG96RP?ref=ppx_yo2ov_dt_b_product_details&th=1')

print('the price is:' + price)
