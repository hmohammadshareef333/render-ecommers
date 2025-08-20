# from django.shortcuts import redirect, render
# from .models import Products,CartModel
# from django.db.models import Q
# from django.contrib.auth.decorators import login_required

# # Create your views here.


# def home(request):
#     category_nav=True
#     trend=False
#     sale=False
#     all_products=Products.objects.all()

#       # trending functionality
#     if 'trending' in request.GET:
#         trending_products=Products.objects.filter(trending=1)
#         all_products=trending_products
#         category_nav=False
#         trend=True
#     if 'sale' in request.GET:
#         sale_products=Products.objects.filter(sale=1)
#         all_products=sale_products
#         category_nav=False
#         sale=True


#     # search functionality
#     if 'query' in request.GET:
#         query_data=request.GET['query']
#         # print(query_data)
#         category_nav=False
#         all_products=Products.objects.filter(Q(category__icontains=query_data) | Q(name__icontains=query_data) |Q(desc__icontains=query_data))
    
    
#     product_categories=[]
 
#     for i in all_products:
#         if i.category not in product_categories:
#             product_categories+=[i.category]

#     # print(product_categories)
 
#     if 'category_query' in request.GET:
#         category_nav=True
#         category_query_data=request.GET['category_query']
#         # print(category_query_data)
#         all_products=Products.objects.filter(category=category_query_data)
#         # print(all_products)
#         # category_nav=True
#         context={'all_products':all_products,'product_categories':product_categories,'category_nav':category_nav}
#         return render(request,'home.html',context)

#     cart_products_count=CartModel.objects.filter(host=request.user).count()


#     context={'all_products':all_products,'product_categories':product_categories,'category_nav':category_nav,'trend':trend,'sale':sale,'cart_products_count':cart_products_count}
#     return render(request,'home.html',context)

# # @login_required(login_url='login_')
# def cart(request):

#     cart_products=CartModel.objects.filter(host=request.user)
#     print(cart_products)

#     cart_products_count=CartModel.objects.filter(host=request.user).count()

#     context={'cart_products':cart_products,'cart_products_count':cart_products_count}

#     return render(request,'cart.html',context)


# # @login_required(login_url='login_')
# def addtocart(request,id):
#     product=Products.objects.get(id=id)

#     try:
#         item_exist=CartModel.objects.get(name=product.name)
#         item_exist.quantity+=1
#         item_exist.totalprice+=item_exist.price
#         item_exist.save()

#     except:
#         CartModel.objects.create(category=product.category,name=product.name,desc=product.desc,price=product.price,totalprice=product.price,host=request.user)
    
#     return redirect('cart')
from django.shortcuts import redirect, render  
from .models import Products, CartModel  
from django.db.models import Q  
from django.contrib.auth.decorators import login_required  

# Create your views here.  

def home(request):  
    category_nav = True  
    trend = False  
    sale = False  
    all_products = Products.objects.all()  

    # trending functionality  
    if 'trending' in request.GET:  
        trending_products = Products.objects.filter(trending=1)  
        all_products = trending_products  
        category_nav = False  
        trend = True  
    if 'sale' in request.GET:  
        sale_products = Products.objects.filter(sale=1)  
        all_products = sale_products  
        category_nav = False  
        sale = True  

    # search functionality  
    if 'query' in request.GET:  
        query_data = request.GET['query']  
        # print(query_data)  
        category_nav = False  
        all_products = Products.objects.filter(Q(category__icontains=query_data) | Q(name__icontains=query_data) | Q(desc__icontains=query_data))  

    product_categories = []  
    for i in all_products:  
        if i.category not in product_categories:  
            product_categories += [i.category]  
    # print(product_categories)  

    if 'category_query' in request.GET:  
        category_nav = True  
        category_query_data = request.GET['category_query']  
        # print(category_query_data)  
        all_products = Products.objects.filter(category=category_query_data)  
        # print(all_products)  
        # category_nav=True  
        context = {'all_products': all_products, 'product_categories': product_categories, 'category_nav': category_nav}  
        return render(request, 'home.html', context)  

    cart_products_count = 0  
    if request.user.is_authenticated:  # Check if the user is authenticated  
            cart_products_count = CartModel.objects.filter(host=request.user).count()  

    context = {'all_products': all_products, 'product_categories': product_categories, 'category_nav': category_nav, 'trend': trend, 'sale': sale, 'cart_products_count': cart_products_count}  
    return render(request, 'home.html', context)  

@login_required(login_url='login_')  
def cart(request):  
    cart_products = []  
    cart_products_count = 0  
    cart_total_price=0
    # if request.user.is_authenticated:  
    #     cart_products = CartModel.objects.filter(host=request.user)  
    #     print(cart_products)  
    # cart_products_count = CartModel.objects.filter(host=request.user).count()  

    # context = {'cart_products': cart_products, 'cart_products_count': cart_products_count}  
    # return render(request, 'cart.html', context) 
   
    if request.user.is_authenticated:
        # Fetch all cart products for the user
        cart_products = CartModel.objects.filter(host=request.user)
        
        # Calculate the total quantity of products in the cart
    cart_products_count = sum(item.quantity for item in cart_products)
    cart_total_price = sum(item.totalprice for item in cart_products) 

    context = {
        'cart_products': cart_products,
        'cart_products_count': cart_products_count,
        'cart_total_price':cart_total_price
    }
    return render(request, 'cart.html', context)
    # cart_products_count = 0
    # cart_total_price = 0

    # if request.user.is_authenticated:
    # # Fetch all cart products for the user
    #    cart_products = CartModel.objects.filter(host=request.user)
    
    # # Calculate the total quantity of products in the cart
    #    cart_products_count = sum(item.quantity for item in cart_products)
    
    # # Calculate the total price of products in the cart
    #    cart_total_price = sum(item.quantity * item.product.price for item in cart_products)  # Assuming product.price gives the price of a single unit.

    #    context = {
    #    'cart_products': cart_products,
    #    'cart_products_count': cart_products_count,
    #     'cart_total_price': cart_total_price,
    #     }

    # return render(request, 'cart.html', context)


@login_required(login_url='login_')  
def addtocart(request, id):  
    product = Products.objects.get(id=id)  

    if request.user.is_authenticated:  
        try:  
            item_exist = CartModel.objects.get(name=product.name, host=request.user)  # Add host to the query  
            item_exist.quantity += 1  
            item_exist.totalprice += item_exist.price  
            item_exist.save()  
        except CartModel.DoesNotExist:  # Changed from except: to explicitly catch DoesNotExist  
            CartModel.objects.create(category=product.category, name=product.name, desc=product.desc, price=product.price, totalprice=product.price, host=request.user)  

    return redirect('cart')  