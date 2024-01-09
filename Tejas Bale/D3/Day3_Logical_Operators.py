x = 5
y = 10
z = 15

#and
r = (x<y)and(y>z) #false
print("(x<y)and(y>z)", r)

r = (x<y)and(y<z) #true
print("(x<y)and(y<z)", r)

r = (x!=y)and(y==z) #false
print("(x!=y)and(y==z)", r)

r = (x>y)and(y>z) #false
print("(x>y)and(y>z)", r)

#or
r = (x<y)or(y<z) #true
print("(x<y)or(y<z)", r)

r = (x>y)or(y>z)
print("(x>y)or(y>z)", r)

r = (x!=y)and(y==z) #false
print("(x!=y)and(y==z)", r)

#not
r = not(x!=y)
print(r)

r = not(y==z)
print(r)









