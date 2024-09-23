"""the program shuld add numbers from 1 to a specified number in a list
for multiples of 3 it should be "fizz"
    for multiply of 5 it should be "buzz"
    for numbers multiples of both 3 and 5 it should be "fizzbuzz"
    print the list"""





print("fizz Buzz Program")
till_num=int(input("Enter the specified number: "))

my_list=[]

for num in range(1,till_num+1):
    my_list.append(num)
    if num % 3 == 0:
        print("Fizz...")
        if num % 5 == 0:
            print("Fizz Buzz....")
    elif num % 5 == 0:
        print("Buxx...") 
    else:
        print(num)      

print(my_list)