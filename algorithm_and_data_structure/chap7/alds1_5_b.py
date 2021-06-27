def merge(a, left, mid, right):
    print("merge:", a, left, mid, right, sep=", ")
    n1 = mid - left
    n2 = right - mid
    L = []
    R = []
    for i in range(n1):
        L[i] = a[left + i]
    for i in range(n2):
        R[i] = a[mid + i]
    L[n1] = 2000000000
    R[n2] = 2000000000
    i = 0
    j = 0
    for k in range(left, right):
        if L[i] <= R[i]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1

def merge_sort(a, left, right):
    print("merge_sort",a,left,right,sep=", ")
    if left+1 < right:
        mid = int((left + right)/2)
        merge_sort(a, left, mid)
        merge_sort(a, mid, right)
        merge(a, left, mid, right)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(' ')))
    merge_sort(a,0,n-1)
    print(a, sep=' ')