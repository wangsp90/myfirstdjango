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

def tpm_if(request):
	context={"tpm":"This is DTL parameter test!","names":["wangsp","Jane"],"age":16}
	return render(request,'DTL_if.html',context=context)

def tpm_for(request):
	context={
	"books":[
	{"name":"将夜","price":99},
	{"name":"幽梦","price":78},
	{"name":"黑切","price":109}
	],
	"students":{"01":70,"02":32,"03":98}
	}
	return render(request, 'DTL_for.html', context=context)
