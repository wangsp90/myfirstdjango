from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse


# Create your views here.
def news_list(request):
	return HttpResponse("新闻列表")

def news_id(request,newsid):			#通过url中指定某段直接传递newsid
	nid="Your news id is %s" % newsid
	return HttpResponse(nid)

def news_search(request):				#通过?keys=xxx来传递keys
	keys=request.GET.get('keys')
	newss="Your search news is %s" % keys
	return HttpResponse(newss)

#DTL test if 同时进行Django参数传递测试
def tpm_if(request):
	context={"tpm":"This is DTL parameter test!","names":["wangsp","Jane"],"age":16}
	return render(request,'DTL_if.html',context=context)

#DTL test for
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

#DTL test url parameter
def dtlurl(request):
	return render(request, 'DTL_url.html')

#add过滤器拼接测试
def add_view(request):
	context={
	"value1":["1",2,"3m"],
	"value2":["A","b","ZY"]
	}
	return render(request, 'testadd.html',context=context)

#cut过滤器删除测试
def cut_view(request):
	return render(request, 'testcut.html')

#date过滤器删除测试
def date_view(request):
	context={
		'now':datetime.now()
	}
	return render(request, 'date.html',context=context)