largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
    except:
        print("invalid input")
        continue
    if largest is None:
        largest = num
    if largest < num:
        largest = num
    if smallest is None:
        smallest = num
    if smallest > num:
        smallest = num

print("Maximum is: ", largest)
print("Minimum is: ", smallest)
