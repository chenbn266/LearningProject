
def partition(arr,low, high):
    pivot =arr[high]
    i = low-1 # minimal element index
    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def quickSort(arr,low, high):
    if low<high:
        mid = partition(arr, low ,high)
        quickSort(arr,low,mid-1)
        quickSort(arr,mid+1,high)
    return None






if __name__=="__main__":
    k = [1,3,5,3,123,443,65,76,2,34,46,242,4]

    quickSort(k,0,len(k)-1)
    print(k)
