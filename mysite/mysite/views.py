import django
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def hello(request):
  return HttpResponse("Hello World")

def homepage_viewer(request):
  return render(request, 'menu_bar.html')
  
def template_practice(request):
	temp = Template('My name is {{ name }}. ')
	number_one = 1
	number_two = 2
	shopping_list = ['apple', 'orange', 'berry']

	if number_two < number_one:
		return render(request, 'templates.html', {'name' : 'George'})
	else:
		return render(request, 'templates.html', {'name' : 'Aja'})
	
