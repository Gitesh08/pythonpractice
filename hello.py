print('Gitesh')

def findElement(arr, n, key):
    for i in range(n):
        if  arr[i]==key:
            return i
    return -1

if __name__=="__main__":
    arr = [2,3,5,67,100]
    key = 45
    
    n = len(arr)
    index = findElement(arr,n,key)
    if index!=-1:
        print("Here"+str(index+1)) 
    else:
        print("Not here")
        
            