a=int(input())
s=0
if a<=150:
    s=0.4463*a
elif a<=400:
    s=(a-150)*0.4663+150*0.4463
else :
    s=250*0.4663+150*0.4463+(a-400)*0.5663
print("%.1f"%(s,))