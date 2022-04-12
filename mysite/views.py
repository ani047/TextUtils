# I have created my Website...

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # add={'Name':'Anil','Place':'Indore'}
    return render(request, 'index.html')


def Getting(request):
    return HttpResponse("Getting Data Successfully")

    '''return HttpResponse("""<h2> Please Choose the Course</h2> 
    <a href='https://www.w3schools.com/python/' target=_blank>Python</a><br> 
    <a href='https://www.w3schools.com/java/'>Java</a><br>
    <a href ='https://www.w3schools.com/html/'>HTML</a>""")
'''



def Analyze(requet):
    djtext=requet.POST.get('text','default')
    removepunc=requet.POST.get('removepunc', 'off')
    fullcaps = requet.POST.get('fullcaps', 'off')
    newlineremover = requet.POST.get('newlineremover', 'off')
    extraspaceremover=requet.POST.get('extraspaceremover','off')

    print(removepunc)
    print(djtext)
    if removepunc =='on':

        #Analyzed=djtext
        punctialtions='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        Analyzed=" "
        for char in djtext:
            if char not in punctialtions:
                Analyzed=Analyzed+char
        param = {'purpose': 'Remove Punc', 'Analyze_text': Analyzed}

        #return render(requet, 'Analyze.html', param)
        djtext=Analyzed

    if(fullcaps=='on'):
        Analyzed=""
        for char in djtext:
            Analyzed=Analyzed+char.upper()
        param = {'purpose': 'Change to UpperCase', 'Analyze_text': Analyzed}
        #return render(requet, 'Analyze.html', param)
        djtext=Analyzed

    if(newlineremover=="on"):
        Analyzed = ""
        for char in djtext:
            if char!='\n':
                Analyzed = Analyzed + char
        param = {'purpose': 'Remove New Line', 'Analyze_text': Analyzed}
        #return render(requet, 'Analyze.html', param)
        djtext=Analyzed

    if(extraspaceremover=="on"):
        Analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                Analyzed = Analyzed + char
        param = {'purpose': 'Remove New Line', 'Analyze_text': Analyzed}
    return render(requet, 'Analyze.html', param)
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("Please select any Operation")



def removepunc(request):
    return HttpResponse("Nothing here")




