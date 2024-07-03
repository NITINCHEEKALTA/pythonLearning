# 4 main data structures
"""List - [1,2,3,4]
   Tuple - (1,2,3,4)
   Set- {1,2,3,4,5}
   Dictionary - {"brand":"iphone","model":"15","price":"1500"}

Sequence types
   List and Tuple have sequential order
   Set - non sequential
   Dictionary - Key value

Mutable vs Immutable
Mutable - Value can be changed  (Eg: List, Set, Dictionary)
Immutable - Value cannot be changed (Eg: String, Tuple)
"""

orders = [1,"2013-7-25",11599,"Closed"]
orders_1 = (3,"2023-12-25",11577,"Closed")
print(orders)
print("=========================================="*3)
print(type(orders))
print(type(orders_1))
orders[3] = "Open"
#orders_1[2] = "11223"
print(orders)
print(orders_1)
orders.append(100)
print("=========================================="*3)
print(orders)
print("=========================================="*3)
orders.insert(1,"Nitin")
print(orders)

