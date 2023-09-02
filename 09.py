v1=int(input("digite um numero"))
v2=int(input("digite um numero"))
v3=int(input("digite um numero"))
if v1>v2 and v1>v3:
    print (f"O número maior é o {v1}")
elif v2>v1 and v2>v3:
    print (f"O número maior é o {v2}")
else: 
    print (f"O número maior é o {v3}")