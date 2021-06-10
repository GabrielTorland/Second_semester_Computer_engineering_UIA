String = input("Pleas type a string: ")
String2 = input("Pleas type another string: ")

if String == String2:
    print("are equal")
    exit()
else:
    print("are not equal")
if String.find(String2) != -1:
    print("is a substring")

elif String2.find(String) != -1:
    print("is a substring")
else:
    print("is not a substring")