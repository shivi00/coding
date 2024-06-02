t=int(input())
ans=[]
while t:
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
 
    a,b=0,n-1
    s={}
    r_v=[0 for _ in range(2*k+3)]
    while a<b:
        su=arr[a]+arr[b]
        if su in s:
            s[su]+=1
        else:
            s[su]=1
        r_v[min(arr[a],arr[b])+1]+=1
        r_v[max(arr[a],arr[b])+k+1]-=1
        a+=1
        b-=1
 
    c=n
 
    le=len(r_v)
    for i in range(le-1):
        r_v[i+1]+=r_v[i]
    
     
    for l in range(2,2*k+1):
        su=0
        if l in s:
            su=(((n//2)-r_v[l])*2)+r_v[l]-s[l]
        else:
            su=(((n//2)-r_v[l])*2)+r_v[l]
        c=min(c,su)
 
    ans.append(c)
    t-=1
 
for i in ans:
    print(i)