def remainder(a,b):
    r=0
    if a>b and b!=0:
        r=a%b
        return r
    elif a<b and a!=0:
        r=b%a
        return r
    elif a<0 or b<0 :
        return 0
    else:
        return None