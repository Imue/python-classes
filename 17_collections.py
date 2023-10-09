cart = [
        {'item': 'apple','price': 100,'qty': 7},
        {'item': 'ball', 'price': 800, 'qty': 1},
        {'item': 'cat', 'price': 19100, 'qty': 1},
    ]

print("Total orders", len(cart));
total = 0
items = 0
for order in cart:
 p= order['price']
 q = order['qty']
 i = order['item']
 print(i, "is", p*q)
 total += p
 items += q

 x = (7.5 * total)/100
 x += total
 z = (10 * x)/100
 #x -= z
 z = x - z
 
 print("Total price", total)
 print("Total items", items)
 print("gross price", x)
 print("net price", z)
 
input();
         
