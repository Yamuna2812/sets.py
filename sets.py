num=input("Enter the sequence of numbers")
print("Entered sequence of number is:",num)
uniqDig = set(num)
for elem in uniqDig:
    print(elem,"occurs",num.count(elem),"times")