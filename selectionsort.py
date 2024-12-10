def selectionsort(arr,n):
    mini=0
    for i in range(0,n):
        mini=i
        for j in range(i+1,n):
            if(arr[j]<arr[mini]):
                mini=j
        temp=arr[i]
        arr[i]=arr[mini]
        arr[mini]=temp 
n=6
arr=[3,1,8,7,5,4]
selectionsort(arr,n)
print(arr)
       
