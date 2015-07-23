from django.shortcuts import render

def about( request ) :
	context = {
		'title' : 'About bitch!!!'
	}
	return render( request, 'about.html', context )
