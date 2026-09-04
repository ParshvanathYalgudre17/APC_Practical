cart = {}

def add_product(name, price, quantity):
    cart[name] = [price, quantity]

def remove_product(name):
    if name in cart:
        del cart[name]

def subtotal():
    total = 0
    for price, quantity in cart.values():
        total = total + price * quantity
    return total

def coupon_discount(amount):
    if amount >= 5000:
        return amount * 0.10
    return 0

def gst(amount):
    return amount * 0.18

def final_invoice():
    sub = subtotal()
    discount = coupon_discount(sub)
    taxable = sub - discount
    tax = gst(taxable)
    return sub, discount, tax, taxable + tax

add_product("Laptop", 50000, 1)
add_product("Mouse", 500, 2)

sub, discount, tax, final = final_invoice()

print("Subtotal =", sub)
print("Discount =", discount)
print("GST =", tax)
print("Final Bill =", final)
