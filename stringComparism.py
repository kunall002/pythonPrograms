str1="Greek"
str2="Greek"
str3=str1

print("id of str1=",hex(id(str1)))
print("id of str2=",hex(id(str2)))
print("id of str3=",hex(id(str3)))

print(str1 is str1)
print(str1 is str2)
print(str1 is str3)

str1+="s"
str4="Geeks"

print("\n ID of changed str1 =",hex(id(str1)))
print("\n ID of str4 =",hex(id(str1)))
print(str1 is str4)