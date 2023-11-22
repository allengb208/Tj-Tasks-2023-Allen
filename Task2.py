def count_pairs(arr, K):
    
    sum=0
    N=len(arr)

    for i in range(N):
        for j in range(i+1,N):
            if arr[i]+arr[j]== K :
                sum +=1 

    return sum 


arr = list(map(int,input("Enter the numbers with spaces between them : ").split()))
K = int(input("Enter the total sum : "))

SumOfTheGivenNumber =  count_pairs(arr,K)
print("The number of pairs which form K is  : " , SumOfTheGivenNumber )