from django.shortcuts import render

from django.http import HttpResponse


# Create your views here.
def news_list(request):
	return HttpResponse("新闻列表")

def news_id(request,newsid):
	nid="Your news id is %s" % newsid
	return HttpResponse(nid)

def news_search(request):
	keys=request.GET.get('keys')
	newss="Your search news is %s" % keys
	return HttpResponse(newss)

def tpm(request):
	context={"tpm":"This is DTL parameter test!","Lily":30,"wangsp":28}
	return render(request,'DTL_pm.html',context=context)