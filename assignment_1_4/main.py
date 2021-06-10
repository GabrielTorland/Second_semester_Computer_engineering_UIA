
String = input("Pleas type a string: ")
print("The string length is: %d" % len(String))
for x in map(chr, range(97, 123)):
        print("'%c' : " % x, end="")
        print(String.count(x))
