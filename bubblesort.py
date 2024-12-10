def bubblesort(arr,n):
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
n=6
arr=[1,7,6,5,4,3]
bubblesort(arr,n)
print(arr)