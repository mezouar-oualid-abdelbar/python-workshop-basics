print('''1
2
3
4

 ''')

p = "Python"
c = "Coding"

# 1
#p[6] out of range 
p[6:]

#print(p[6:])

#no output no value

# 2
p[::-1]

#print(p[::-1])

#flip thr word

# 3
p += c
p # pythonCoding

# 4
p = "Mython"
#p[0] = "P" TypeError: 'str' object does not support item assignment 
p = "P" + p[1:]
p # Python

