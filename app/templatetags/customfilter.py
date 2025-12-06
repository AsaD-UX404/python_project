from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    c = cart.keys()
    for cartid in c:
        if int(cartid) == product.id:
            return cart.get(cartid)
        
@register.filter(name='cart_quantity')
def cart_quantity(product,cart):
    c = cart.keys()
    count = 0
    for cartid in c:
        if int(cartid) == product.id:
            q = cart.get(cartid)
            count = product.product_finalprice * q
    return count

@register.filter(name='toatal_quantity')
def toatal_quantity(product,cart):
    sum = 0
    for i in product:
        sum+=cart_quantity(i,cart)
    return sum

@register.filter(name='len')
def len(cart):
    sum = 0
    if cart is not None:
        for i in cart:
            sum+=1
        if sum >= 1:
            return True
        else:
            return False
    else:
        return False