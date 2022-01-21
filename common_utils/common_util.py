from pydoc import describe
import requests
import json
import xmltodict
from news.models import News, Stock, StockNews

# from db_config import DB, check_table_exists, insert_news
def insert_news(stocks_list, title, description, image_url, news_link, pub_date, source):
   """Inserts news to Database."""
   news = News(title=title, description=description, image_url=image_url, news_link=news_link, pub_date=pub_date, source=source)
   news.save() #save
  
   if news.id:
      for stock in stocks_list:
         if (f"{stock['symbol'].lower()}" in title.lower()+" "+description.lower()) or (stock['description'].lower() in title.lower()+" "+description.lower()) :
            #  TODO : Save stock(token) & News(id) in mapper DataBase(stock_news_mapper)
            # stock = Stock(pk=stock['token'])
            # news = News(pk=news.id)
            # stock_news = StockNews(stock, news)
            # stock_news.save()
            pass
def upload_economictimes_data(stocks_list):
   # XXX ECONOMICTIMES
   economictimes_url = 'https://economictimes.indiatimes.com/markets/stocks/rssfeeds/2146842.cms'
   response = requests.get(economictimes_url)
   xml_data_as_str = json.dumps(xmltodict.parse(response.text.replace("'","''")))
   item_data = json.loads(xml_data_as_str)['rss']['channel']['item']
   for news in item_data:
      try:
         insert_news(stocks_list, news['title'], news['description'], news['image'], news['link'], news['pubDate'], 'ECONOMICTIMES')
      except Exception as E:
         print("Exception : ", E)

def upload_moneycontrol_data(stocks_list):
   # XXX MONEYCONTROL
   moneycontrol_url = 'https://www.moneycontrol.com/rss/business.xml'
   response = requests.get(moneycontrol_url)
   xml_data_as_str = json.dumps(xmltodict.parse(response.text.replace("'","''")))
   item_data = json.loads(xml_data_as_str)['rss']['channel']['item']
   for news in item_data:
      try:
         insert_news(stocks_list, news['title'], news['description'], None, news['link'], news['pubDate'], 'MONEYCONTROL')
      except Exception as E:
         print("Exception : ", E)

def upload_ndtv_data(stocks_list):
   # XXX NDTV
   ndtv_url = 'https://feeds.feedburner.com/ndtvprofit-latest'
   response = requests.get(ndtv_url)
   xml_data_as_str = json.dumps(xmltodict.parse(response.text.replace("'","''")))
   item_data = json.loads(xml_data_as_str)['rss']['channel']['item']
   for news in item_data:
      try:
         insert_news(stocks_list, news['title'], news['description'], news['fullimage'], news['link'], news['pubDate'], 'NDTV')
      except Exception as E:
         print("Exception : ", E)
