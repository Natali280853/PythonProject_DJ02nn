from django.shortcuts import render
def page1(request):
    return render(request, 'mymain/page1.html')

def page2(request):
    return render(request, 'mymain/page2.html')

def page3(request):
    return render(request, 'mymain/page3.html')

def page4(request):
    return render(request, 'mymain/page4.html')