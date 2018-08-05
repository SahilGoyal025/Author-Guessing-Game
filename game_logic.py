from random import choice 
from csv import DictReader
from pyfiglet import figlet_format
from requests import get
from bs4 import BeautifulSoup
Url='http://quotes.toscrape.com'
def read_quotes(filename):
	with open(filename,'r',encoding='utf-8') as f:
		csv_read=DictReader(f);
		#for quote in csv_read:
		#	quotes.append(quote);
		quotes=list(csv_read)
	return quotes


def game(quotes):
	print(figlet_format('Quote        Guessing                   Game : '))
	game_status=True
	while(game_status):
		quote=choice(quotes)
		guess=4
		#print(quote)
		print(f"Here Is the Quote For you : {quote['text']}")
		while guess>0 :
			response=input(f'\nGuess the author - Guesses remaining  {guess} : ')
			if(response.lower()==quote['author'].lower()):
				print('Congrats You Answered the correct author . YOU WIN !. :)\n')
				break
			guess-=1
			print('Ooops ! You guessed wrong . ')
			hint(quote,guess)
		if(guess==0):
			print('\nSorry! you could not guess it ! YOU LOSE :(')
			print(f'\nCORRECT ANSWER :  {quote["author"]} .\n')
		while(game_status not in ('y','yes','yeah' ,'n','no' ,'nah')):
			game_status=input('Do you want to play again y/n ? ').lower()
		if(game_status in ('y', 'yes' , 'yeah')):
			print('\nOk! Another Round of Game \n')
			game_status=True
		else:
			print('\nOK GOOD  BYE!')
			game_status=False

def hint(quote,guess):
	if(guess==3):
		response=get(Url+quote['author-link']).text
		soup=BeautifulSoup(response,'html.parser')
		birth_date=soup.find(class_='author-born-date')	
		birth_place=birth_date.find_next_sibling().get_text()
		birth_date=birth_date.get_text()
		print('Here is a HINT! : ')
		print(f'The author was born on {birth_date}  {birth_place} .')
	if(guess==2):
		print('Here is a HINT! : ')
		print(f'Author\'s First Name starts with letter {quote["author"][0]} .' )
	if(guess==1):
		name_list=quote['author'].split(' ')
		last_name=name_list[-1];
		print('Here is a HINT! : ')
		print(f'Auhtor\'s Last Name  starts with letter {last_name[0]} .')




quotes=read_quotes('csv_quotes.csv')
quote=choice(quotes)
#print(quote)
#print(quote['text'])
#print(quotes)
game(quotes)

