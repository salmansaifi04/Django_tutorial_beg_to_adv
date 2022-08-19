from django.shortcuts import render

# Create your views here.
def learn_django(request):
    student = {
        'stu1' : {'name' : 'salman', 'roll' : 111},
        'stu2' : {'name' : 'prakash', 'roll' : 112},
        'stu3' : {'name' : 'suraj', 'roll' : 113},
    }
    return render(request, 'course/courseone.html', {'students' : student})

def learn_python(request):
    context = {
        'cname' : 'Python',
        'duration' : '4 Months',
        'seats' : 10
    }
    return render(request, 'course/coursetwo.html', context = context)