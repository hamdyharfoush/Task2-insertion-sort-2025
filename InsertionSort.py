# Name :Hamdy Harfoush
# Section : 3
def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  

arr = [9, 8, 4, 5, 2, 1]
insertion_sort(arr)
print("القائمة بعد الترتيب:", arr)