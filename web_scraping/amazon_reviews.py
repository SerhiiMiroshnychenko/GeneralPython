import sys
import time
from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com/Odoo-Development-Cookbook-effective-applications/product-reviews/1805124277/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
page = None
try:
    page = requests.get(url)  # this might throw an exception if something goes wrong.
except Exception as e:
    print(e.__class__, e)
    error_type, error_obj, error_info = sys.exc_info()
    print('ERROR FOR LINK:', url)
    print(error_type, 'Line:', error_info.tb_lineno)

time.sleep(2)
if page:
    soup = BeautifulSoup(page.text, 'html.parser')
    review_div = soup.find('div', class_='a-row a-spacing-small review-data')
    if review_div:
        review_span = review_div.find('span', {'data-hook': 'review-body'})
        if review_span:
            review_content = review_span.find('span').text
            print(f"{review_content = }")
        else:
            print("Review span not found")
    else:
        print("Review div not found")
else:
    print(f"{page = }")
    print(f"{page.reason = }")  # Ban scraps)
    print(f"{page.text = }")  # Ban scraps)
