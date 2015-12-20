def recurPower(base, exp):
    if exp==0:
        return 1
    elif exp==1:
         return base
    elif exp>1:
         return base*recurPower(base,exp-1)
