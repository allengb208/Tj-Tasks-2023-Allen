def findMissingNumber(arr,N):
    for num in range(1,N+1):
        if num not in arr:
            return num
        


arr =  list(map(int,input("Enter the list of array with appropriate spaces : ").split()))
N=len(arr) 
missingNumber = findMissingNumber(arr,N)
print("The missing number in array is " , missingNumber)