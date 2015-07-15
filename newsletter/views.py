from django.shortcuts import render
from .forms import SignUpForm
from .forms import ContactForm

#home route
def home( request ) :

	title = "Forms Example"
	
	form = SignUpForm( request.POST or None )

	
	context = {
		"title" : title,
		'form' : form		
	}

	if form.is_valid() : 
		instance = form.save( commit=False )
		instance.save()
		msj = "User %s successfuly updated" % ( instance.email )
		context = {
			'title' : 'Thank you!',
			'messages' : [ msj, "Another message" ]
		}

	return render( request, "home.html", context )
#end of home route

#contact route
def contact( request ) : 

	form = ContactForm( request.POST or None )
	
	if form.is_valid() :
		context = { 
			'title' : 'Correct Submition',
			 
		 }
	else : 
		context = {
			'title' : 'Contact Us!',	
			'form' : form
		}

	return render( request, "contact.html", context )
#end of contact route
