from time import sleep
a1 = c = 0
a2 = 1
print(a2)
while True:
     n = a1 + a2
     print(n)
     a1 = a2
     a2 = n
     sleep(0.5)