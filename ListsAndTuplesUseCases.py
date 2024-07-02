"""create a new list after performing some transformation"""
order_amounts = [100, 200, 50, 500, 400, 900, 1200, 70]
orders_including_gst_1 = []

for x in order_amounts:
    orders_including_gst_1.append(x + x * .18)
print(orders_including_gst_1)

# List comprehension
orders_including_gst_2 = [x+x*.20 for x in order_amounts]
