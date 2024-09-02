from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
    """ A view to view the shopping bag """

    return render(request, 'bag/bag.html')

# Form sends item+id, quantity and redirect_url to this view
def add_to_bag(request, item_id):
    """ Add a quantity of a specified product to the bag """

    # quantity from form is converted to integer
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # Gets the bag session variable if it already exists or creates it if it doesnt
    bag = request.session.get('bag', {})


    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # Updates the item quantity or adds item if not already in bag
        if item_id in list(bag.keys()):
            bag[item_id] == quantity
        else:
            bag[item_id] = quantity

    # Updates bag variable with current data
    request.session['bag'] = bag
    
    return redirect(redirect_url)