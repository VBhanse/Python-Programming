name = "harry" #Strings are immutable
s = "hello world"
#name[0] = "R" #You cannot do this as 'str' object does not support item assignment

a = len(s)
# print(a)
# print(s.upper())
# print(s.lower())
# print(s.capitalize())
# print(s.title())
# text = "\nhello world"
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())

# text = "Python is fun"
# print(text.find("is"))
# print(text.replace("fun", "awesome"))

# text = "Apples, bananas, pineapples"

# print(text.split(","))

# print(",".join(["Apples", "bananas", "pineapples"]))

text = "Python123"
print(text.isalpha()) #check if the string has only alphabets
print(text.isdigit()) #check if the string has only digits
print(text.isalnum()) #check if the string has both alphabets and numbers
print(text.isspace()) #checks if it has any spaces
