# 2.11 sum_while.py

s = 0; k = 1; M = 100
while k <= M:
    s += 1/k
    k += 1
print(s)

"""
Kommentar: 
Feil 1: Løkken vil gå evig fordi k økes ikke:
    Rettet: k += 1

Feil 2: Siste M blir ikke med:
    Rettet: while k <= M:
    
Feil 3: Syntax feil for python 3: 
    print(s)
    

Terminal> sum_while.py"
5.187377517639621

Process finished with exit code 0

"""