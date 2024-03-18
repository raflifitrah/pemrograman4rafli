a = int(input("masukkan bilangan pertama: "))
b = int(input("masukkan bilangan kedua: "))
c = int(input("masukkan bilangan ketiga: "))

if a > b and a > c:
    print(f"bilangan {a} lebih besar dibanding {b} dan {c}")
elif b > a and b > c:
    print(f"bilangan {b} lebih besar dibanding {a} dan {c}")
elif c > a and c > b:    
    print(f"bilangan {c} lebih besar dibanding {a} dan {b}")    
elif a == b > c:
    print(f"bilangan {a} sama dengan {b}, tapi lebih besar dari bilangan {c}")
elif a == c > b:    
    print(f"bilangan {a} sama dengan {c}, tapi lebih besar dari bilangan {b}")
elif b == c > a:    
    print(f"bilangan {b} sama dengan {c}, tapi lebih besar dari bilangan {a}")
else:
    print("ketiga bilangan tersebut sama besar")