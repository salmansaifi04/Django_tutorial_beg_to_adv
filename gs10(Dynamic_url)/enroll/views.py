from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'enroll/home.html')

# def show(request,my_id):
#     if my_id == '1':
#         student = {'name':'Salman', 'my_id' : my_id}
#     if my_id == '2':
#         student = {'name':'Suraj', 'my_id' : my_id}
#     if my_id == '3':
#         student = {'name':'Prakash', 'my_id' : my_id}
#     return render(request, 'enroll/show.html', student)


def show(request,my_id):
    if my_id == 1:
        student = {'name':'Salman', 'my_id' : my_id}
    if my_id == 2:
        student = {'name':'Suraj', 'my_id' : my_id}
    if my_id == 3:
        student = {'name':'Prakash', 'my_id' : my_id}
    return render(request, 'enroll/show.html', student)


def subshow(request,my_id, my_subid):
    if my_id == 1 and my_subid == 5:
        student = {'name':'Salman', 'my_id' : my_id, 'info':'sub_info', 'my_sub_id':my_subid}
    if my_id == 2 and my_subid == 6:
        student = {'name':'Suraj', 'my_id' : my_id, 'info':'sub_info', 'my_sub_id':my_subid}
    if my_id == 3 and my_subid == 7:
        student = {'name':'Prakash', 'my_id' : my_id, 'info':'sub_info', 'my_sub_id':my_subid}
    return render(request, 'enroll/show.html', student)