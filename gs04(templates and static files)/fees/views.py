from django.shortcuts import render

# Create your views here.
def fee_django(request):
    return render(request, 'fees/feeone.html')    

def fee_python(request):
    return render(request, 'fees/feetwo.html')