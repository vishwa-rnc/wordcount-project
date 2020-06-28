#from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    d={}
    for i in wordlist:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    sortedwords=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
def about(request):
    return render(request,'about.html')
