from django.shortcuts import render
import requests
import json
from .models import Think_Analytics
from .forms import info_form

def data(request):
	a=requests.get('https://randomuser.me/api')
	# print(a)
	text= a.json()  #python dictionary to retrive a data
	# my_text=json.dumps(text, indent=5 )  #json data format to easily analyze a data
	# print(my_text)
	loc = {

		'street_number': text['results'][0]['location']['street']['number'],
		'street_name': text['results'][0]['location']['street']['name'],
		'city': text['results'][0]['location']['city'],
		'country': text['results'][0]['location']['country'],
		'postcode': text['results'][0]['location']['postcode'],
	}
	my_loc = []
	for key, value in loc.items():
		my_loc.append(value)

	location = '{}, {}, {},{} - {}'.format(my_loc[0], my_loc[1], my_loc[2], my_loc[3], my_loc[4])

	context = {
		'name': text['results'][0]['name']['first'],
		'age': text['results'][0]['dob']['age'],
		'gender': text['results'][0]['gender'],
		'Address': location,
		'email': text['results'][0]['email'],
		'image': text['results'][0]['picture']['medium']
	}

	form = info_form(context)
	form.save()

	content = Think_Analytics.objects.all()
	info = {'text': content }
	return render(request, 'home.html', info)






