from django.shortcuts import render

# Create your views here.
def view_bag(request):
    """ A view to view the shopping bag """

    return render(request, 'bag/bag.html')