dict_1 = {}
while True:
    input2 = input()
    if input2 == "stop":
        break
    elif input2 in dict_1.keys():
        dict_1[input2] += 1
    else:
        dict_1[input2] = 1
print("Unique : %d" % len(dict_1.keys()))
print("Total : %d" % sum(dict_1.values()))

for string, value in dict_1.items():
    print("%s : %d" % (string, value))
