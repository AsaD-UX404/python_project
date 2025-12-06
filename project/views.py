from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from app.models import *
from django.contrib import messages
def home(request):
    products = Singal_Frame_Products.objects.all()[:3]
    products2 = Singal_Frame_Products.objects.all()[3:6]
    cat = Categorys.objects.all()
    main = Singal_Frame_Products.objects.filter(id=10)
    return render(request,'index.html',{'p1':products,'p2':products2,'c':cat,'m':main})

def singup(request):
    if request.method == 'POST':
            try:
                  name = request.POST.get('name')
                  email = request.POST.get('email')
                  password = request.POST.get('password')
                  Customer(customer_name=name,customer_email=email,customer_password=password).save()
                  messages.success(request, "User Created succesfully")
                  return HttpResponseRedirect('/login')
            except Exception as e:
                  messages.error(request, "Please Fill form properley")
                  return HttpResponseRedirect('/singup')
    return render(request,'singup.html')

def login(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            if email:
                  try:
                        u = Customer.objects.get(customer_email=email)
                  except Exception as e:
                        messages.error(request, "Plaese Sing up You are nota a user")
                        return HttpResponseRedirect('/login')
                  if u:
                        request.session['customer'] = u.customer_email
                        messages.success(request, "Logind")
                        return HttpResponseRedirect('/')
            else:
                  messages.error(request, "Plaese fille field")
                  return HttpResponseRedirect('/login')
    return render(request,'login.html')

def cartadd(request,id):
      cart = request.session.get('cart')
      r = request.GET.get('remove')
      if cart:
            quantity = cart.get(id)
            if quantity ==0 :
                  cart.pop(id)
                  messages.error(request, "PRODUCT Removed Sussefully")
            else:
                  if r:
                        cart[id] = quantity-1
                  else:
                        if quantity:
                              cart[id] = quantity+1
                        else:
                              cart[id] = 1
                              messages.success(request, "PRODUCT ADED TO CART")
      else:
            cart = {}
            cart[id] = 1
            messages.success(request, "PRODUCT ADED TO CART")
      request.session['cart'] = cart
      if request.method == 'POST':
            cart = request.session.get('cart')
            if cart:
                  cart.pop(id)
                  messages.error(request, "PRODUCT Removed Succsefully")
            return redirect('/cartdisplay')
      return redirect('/cartdisplay')

def account(request):
      name = request.session.get('customer')
      if name:
            d = name[:10]
      c=request.session.get('cart')
      s = Singal_Frame_Products.objects.filter(id__in=c)
      orders = Orders.objects.filter(customer_email=name)
      return render(request,'account.html',{'d':d,'s':s,'o':orders})


def proddisplay(request,id):
      s = Singal_Frame_Products.objects.get(pk=id)
      return render(request,'detailpage.html',{'d':s})

def cartdisplay(request):
      c = request.session.get('cart')
      if c:
            cart = request.session.get('cart').keys()
            s = Singal_Frame_Products.objects.filter(id__in=cart)
      else:
            s = ''
      if request.method == 'POST':
            a = request.POST.get('add')
            p = request.POST.get('phone')
            c = request.session.get('cart').keys()
            product = Singal_Frame_Products.objects.filter(id__in=c)
            for i in product:
                  ce = request.session.get('cart')
                  if ce:
                        Orders(
                              customer_email=request.session.get('customer'),
                              phone=p,
                              addres = a,
                              image = i.product_image,
                              product = i.product_name,
                              quantity = request.session['cart'].get(str(i.id)),
                              totalprice = i.product_finalprice * request.session['cart'].get(str(i.id))
                        ).save()
                        messages.success(request, "Order Is Placed")
                        request.session['cart'] = {}
                  else:
                        messages.error(request, "Cart is empty")
            s=''
      return render(request,'cart.html',{'s':s})



def categorie(request,id):
      c = Categorys.objects.filter(pk=id)
      p1 = Singal_Frame_Products.objects.filter(category_id=id)
      return render(request,'categorydispaky.html',{'p1':p1,'c':c})

def contact(request):
      if request.method == 'POST':
            e = request.POST.get('email')
            m = request.POST.get('msg')
            if e and m:
                  Contact(email=e,msg=m).save()
                  messages.success(request, "Query sent succesfuly")
                  return HttpResponseRedirect('/contact')
            else:
                  messages.error(request, "Fill the Field propraly")
                  return HttpResponseRedirect('/contact')
      return render(request,'contact.html')