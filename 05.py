v1=int(input("digite um numero"))
v2=int(input("digite um numero"))
v3=int(input("digite um numero"))
if v1>v2 and v1>v3:
    if v2>v3:
        print(f"a sequencia e {v3} , {v2} , {v1}")
    else:
        print(f"a sequencia e {v2} , {v3} , {v1}")
elif v2>v1 and v2>v3:
    if v1>v3:
        print(f"a sequencia e {v3} , {v1} , {v2} ")
    else:
        print(f"a sequencia e {v1} , {v3} , {v2}")
else:
    if v1>v2:
        print(f"a sequencia e {v2} , {v1} , {v3}")
    else:
        print(f" a sequencia e {v1} , {v2} , {v3}")    