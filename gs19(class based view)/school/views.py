from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .forms import StudentForm

# Create your views here.

## function based view
# def home(request):
#     return HttpResponse('<h1>This is a function based view</h1>')

## class based view
class HomeView(View):
    name = 'Salman'
    def get(self, request):
        # return HttpResponse('<h1>This is a class based view</h1>') 
        return HttpResponse(self.name) 

## child class
class HomeChildView(HomeView):
    def get(self, request):
        return HttpResponse(self.name) 

############ template render and pass the context ##############
class IndexView(View):
    context = {'info':'This text is render by context'}
    def get(self, request):
        return render(request, 'school/index.html', self.context)


############ how to render form with post method #########
class ContactView(View):
    def get(self, request):
        fm = StudentForm()
        return render(request, 'school/contact.html', {'form': fm})
    
    def post(self, request):
        fm = StudentForm(request.POST)
        if fm.is_valid():
            print('Name : ', fm.cleaned_data['name'])
            return HttpResponse("Thanku for submitting the form!!!")
        