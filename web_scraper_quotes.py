from bs4 import BeautifulSoup
from time import sleep
from requests import get
from csv import DictWriter

def quotes_scraper():
	BaseUrl='http://quotes.toscrape.com'
	next_btn='/page/1/'		 #it will find the tag which conatins the link to next page of quotes 
	#next_btn=next_btn.find('a')['href']
	quotes=[]				# quotes will contain the quotes from the whole website
	while next_btn:
		response=get(BaseUrl+next_btn).text               #reponse contains the html response got from url
		soup=BeautifulSoup(response,'html.parser')
		all_quote_tags=soup.find_all(class_='quote')
		for quote in all_quote_tags:
			quotes.append({
				'text':quote.find(class_='text').get_text(),
				'author':quote.find(class_='author').get_text(),
				'author-link':quote.find('a')['href']
			})
		next_btn=soup.find(class_='next')
		if next_btn:
			next_btn=next_btn.find('a')['href']
		sleep(1)		# program execution is delayed for 1 sec so that the site's server will not get overloaded with requests.
	return quotes
def writing_csv(quotes):
	with open('csv_quotes.csv','w',encoding='utf-8') as f:
		headers=['text' , 'author' , 'author-link']
		writer_object=DictWriter(f,fieldnames=headers)
		writer_object.writeheader()
		for quote in quotes:
			writer_object.writerow(quote)

quotes=quotes_scraper()
writing_csv(quotes)



