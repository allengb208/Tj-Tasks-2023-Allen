# Techno-jam Dsa Questions(My-Approach)

## Write a program to reverse an array or string.


1. I defined a function in which i passed the parameter (arr). i used the [::-1] method to reverse the array , and then returned it.

2. Then called the function inside a different variable which was reversed_arr ,  then i printed both the original and reversed array..


## Given an array of N integers, and an integer K, the task is to find the number of pairs of integers in the array whose sum is equal to K.

1. I created a function named count_pairs. I initialised a variable sum to keep count of the sum.

2. I created a variable N and the value assigned was the length of the array.

3. Then i created a for loop ,  which iterated over the length of the array.

4. Then i nested one more loop inside the for loop which iterated from i+1(means the next number from i as i is already used) to the length of the array.

5. A if loop was created with a situation that if arr[i]+arr[j]==k , i.e: if the both numbers gave a sum equal to K , sum+=1 .

6. Then i returned the sum inside the first for loop and then took input of arr and K, then called the function inside a variable, then printed it.



## Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

1. i created  a function with the parameters as array and N .

2. i ran a for loop which iterated over the array, and then a if statement which returned the number if it was not in the array.

3. Then i took inputs, called the function , then printed it,
