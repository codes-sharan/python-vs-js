# string methods in python

str = 'Hello world'

print(str.lower())
print(str.upper())
print(str.capitalize())
print(str.title())
print(str.strip())
print(str.split())

words = ['Hello', 'World', 'Python']
sentence = "-".join(words)
print(sentence)

print(str)
print(str.replace('world', 'python'))

print("hello".find('l'))
print("hello".startswith("he"))
print("hello".endswith('llo'))