  #def function
def hey_dude():
    print("hey")
    print("dude")
print(hey_dude())
def your_name(name):
    print(f"hello {name}")
your_name('salaar')
def return_result(a,b):
    print(a+b)
return_result(10,20)
def even_check(num):
    return num%2==0
print(even_check(20))
def even_list(num_list):#to check if any even number is present
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass
    return False
print(even_list([1,2,3,5]))
def even_list(num_list):
    even_numbers=[]
    for number in num_list:
        if number%2==0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers
print(even_list([1,2,3,4,5,6,7]))


