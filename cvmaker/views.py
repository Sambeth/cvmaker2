from django.shortcuts import render


def home(request):
	context = {
		'title': 'API',
	}
	template = 'index.html'
	return render(request, template, context)
