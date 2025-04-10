text = 'ice cream'
print(text[0]) # i
print(text[0:3]) # ice
print(text[4:]) # cream
print(text[:3]) # ice
print(text[1:]) # ce cream

text = "Let's learn python"
print(text.lower()) # let's learn python
print(text.upper()) # LET'S LEARN PYTHON
print(text.replace('python', 'java')) # Let's learn java
print(len(text)) # 19
print(text[0:5]) # Let's
print(text[6:]) # learn python
print(text[:5]) # Let's
print(text[6:]) # learn python
print(text[1:]) # et's learn python
print(text[1:5]) # et's

address = '''1234 Main St'''
print(address[0]) # 1
print(address[0:4]) # 1234
print(address[5:]) # Main St
print(address[:4]) # 1234
print(address[5:]) # Main St
print(address[1:]) # 234 Main St
print(address[1:4]) # 234
print(len(address)) # 11

s1 = 'Hello'
s2 = 'World'
print(s1 + ' ' + s2) # Hello World
print(s1 + s2) # HelloWorld

s = "total states in the US"
print(s[0:5]) # total
print(s[6:12]) # states
num = 25
print(s + ' ' + str(num)) # total states in the US 25
