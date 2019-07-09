# 1-lt-dif
n,m=input().split()
if len(n)==len(m):
    
    count=0
    for i in range(len(n)):
        
        
        
        if n[i]!=m[i]:
            count+=1
            
if count==1:
    print('yes')
else:
    print('no')
        
