ticket_prices=[('salaar',200),('pushpa',350)]
for prices in ticket_prices:
    print(prices)
for movie,price in ticket_prices:
    print(movie)
#lamda
def square(num):
    return num**2
nums=[1,2,3,4]
for item in map(square,nums):
    print(item)
def slice(mystring):
    if len(mystring)%2==0:
        return "even"
    else:
        return mystring[0]
names=['salaar','devaratha','raisaar']
print(list(map(slice,names)))
numbers = [1, 2, 3]
squared = map(lambda x: x**2, numbers)
print(list(squared))
numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))
