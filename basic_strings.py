# it modify string 
# uppercase

x='Hi everyone'
print(x.upper())   # this will do everything in capital
print(x.lower())   #this will lowercase
# now alter the above case if we use 
m='Hi everyone'
m.upper()
print(m)    # this will give no capital it will just copy the same as it is mentioned

# to remove white spaces 
q='lets   us  study   python'
print(q.strip())

# replace 
k='Hello world'
print(k.replace('H','kh'))

# how to splitting a string
l='Hello world'
print(l.split())
print(l.split()[0])  #always remember to to give [] this after () otherwise syntax error

# strings contenation (add / combine) using a '+' operator
e="Hello"
f="machine"
g="world"

h=e+f+g 
print(h)   # H=e+" "+f+" "+g



