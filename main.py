def palindrome(s):
    return s == s[::-1]
String = input("Plz type a string:")
print(len(String))
ans = palindrome(String)
if ans:
    print("is a palindrome")
else:
    print("is not a palindrome")
print(String[::-1])

# Or you can do this
#if String == "".join(list(reversed(String))):
    #print("%s is a palindrome" % String)
