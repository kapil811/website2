from django.http import HttpResponse
from django.shortcuts import render

#home services products contactus

#home
def home (request):
    return render (request,"index.html")

#services
def services (request):
    return HttpResponse ('<a href= "/"> go to home</a> <br> this is service page')

#products
def products (request):
    return HttpResponse ('<a href= "/"> go to home</a> <br> this is products page')

#contactus           newtextp punc      newtextc capit
def contactus (request):
    gettext = request.POST.get('textu')
    punc = request.POST.get('removepunc','off')
    capit = request.POST.get('capital','off')
    punctutions = ''',.<>?"?/\|:;'@#$%^&*()'''
    newtextp =''
    newtextc = ''
    if( punc=='on'):
        for char in gettext:
            if char not in punctutions:
                newtextp = newtextp + char
    if(punc == 'off'):
        newtextp = 'tick the checkbox'
    if( capit=='on'):
       newtextc = gettext.upper
    else:
        newtextc = 'tick the checkbox to get capitalized text' 

    params = {'textinput':gettext, 'updatedtextp':newtextp, 'updatedtextc':newtextc}
    return render (request,'contact.html',params)