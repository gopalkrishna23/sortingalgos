def bubblesort(arr,n):
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key 
n=6
arr=[1,5,4,8,7,6]
bubblesort(arr,n)
print(arr)
