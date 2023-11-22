
def reverse_array(arr):
    return arr[::-1]

originalArray = list(map(int, input("Enter space-separated integers for the array: ").split()))

reversed_arr = reverse_array(originalArray)
print("Original array is : " , originalArray)
print("Reversed array is : " , reversed_arr)


