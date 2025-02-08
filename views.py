from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import userForm
from news.models import News
from service.models import Service
def submitform(request):
    try:
        if request.method=="POST":
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalAns=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalAns 
            }
            #url="/gefhome/?output={}".format(finalAns)
            #return redirect(url)
            return HttpResponse(finalAns)
    except:
        pass

def homePage(request):
    '''data={
        'title':'NID & CS',
        'bdata':'Flow Mate',
        'clist':['PHP','Java','Django'],
        'numbers':[],
        'student_details':[
            {'Name': 'Aarjav', 'Contact':7827850349},
            {'Name': 'Saanvi', 'Contact':9711025563}
        ]
    }'''
    newsData=News.objects.all()
    finalAns=0
    fn=userForm()
    data={'form':fn,
          
          'newsData':newsData
          }

    try:
        if request.method=="POST":
            n1=int(request.POST['num1'])
            n2=int(request.POST['num2'])
            finalAns=n1+n2
            data={
                'form':fn,
                'output':finalAns 
            }
            url="/gefhome/?output={}".format(finalAns)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"shoppy.html",data)
def aboutUs(request):
    return HttpResponse("<b>This site still belongs to FlowMate.</b>")
def gefhome(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"index7.html",{'output':output})
def gmefhome(request):
    return render(request,"fashion.html")
def Course(request):
    return HttpResponse("This site doesn't belong to anyone.")
def courseDetails(request, courseid):
    return HttpResponse(courseid) 
def calculator(request):
    if request.method=="POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t/5
        data={
            'total':t,
            'per':p
        }
        return render(request,"shoppy.html",data)
    return render(request,"shoppy.html")
'''    c=''
    if request.method=="POST":
        n=eval(request.POST.get('num1'))
        if (n%2==0):
            c="Even Number"
        else:
            c="Odd Number"
    return render(request,"shoppy.html",{'c':c})
'''
'''    c=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2 
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="Invalid opr......"
    print(c)
    return render(request,"shoppy.html",{'c':c})'''