from django.shortcuts import redirect, render
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    # fix price to product_id
    price_from_form = Product.objects.get(id=request.POST['price']).price
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect("/checkout_thanks")

def checkout_thanks(request):
    
    all_orders = Order.objects.all()
    sumPrice = 0
    quantity = 0
    for order in all_orders:
        sumPrice += order.total_price
        quantity += order.quantity_ordered
        
    print('****** sumPrice', sumPrice)
    context = {
        'all_orders': Order.objects.all(),
        'sumPrice' : sumPrice,
        'quantity' : quantity,
        'last_price': Order.objects.last().total_price
    }
    

    return render(request, 'store/checkout.html', context)