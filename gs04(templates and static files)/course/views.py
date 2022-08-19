from django.shortcuts import render

# Create your views here.
def learn_django(request):
    context = {'cname' : 'Django'}
    return render(request, 'course/courseone.html', context=context)

def learn_python(request):
    return render(request, 'course/coursetwo.html', {'cname2':'Python', 'duration': '4 Months', 'seats' : 10})