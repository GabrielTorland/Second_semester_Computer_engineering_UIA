import statistics
List1 = []
while True:
    input1 = int(input())
    if input1 == 0:
        break
    List1.append(input1)
print("Average : %i" % int(sum(List1)/len(List1)))
print("Median : %d" % statistics.median(List1))
print("Descending : %s" % ' '.join(map(str, sorted(List1)[::-1])))