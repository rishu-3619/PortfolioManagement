from django.shortcuts import render

# Create your views here.
def index(request):
	"""The home page for Portfolio Manager"""
	return render(request, 'PortfolioManagerHome/index.html')

def about(request):
	"""The about page for Portfolio Manager"""
	return render(request, 'PortfolioManagerHome/about.html')