from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,reverse
# Create your views here.

def db_login(request):
	username = request.GET.get('username')
	if username:
		return HttpResponse("gogo")
	else:
		rev=reverse('db:fuck')
		print ("="*20)
		print (rev)
		print ("="*20)
		return redirect(rev)

def fuck(request):
	return HttpResponse("Fuck you!")

def firstindex(request):
	return render(request,'index.html')
