def inSort(L):
    """Insertion sort algorithm. Assuming that (L) is a given list of numbers.
    The procedure sorts the list (L) in place in an increasing order."""
    for j in range(1, len(L)):
        # take L[j] element from the list starting from position 2
        key = L[j]
        i = j - 1
        # and insert it into the sorted sequence on the left
        while i > -1 and L[i] > key:
            L[i + 1] = L[i]
            i = i - 1
        L[i + 1] = key

def inSortR(L):
    """Insertion sort algorithm. Assuming that (L) is a given list of numbers.
    The procedure sorts the list (L) in place in a decreasing order."""
    for j in range(1, len(L)):
        # take L[j] element from the list starting from position 2
        key = L[j]
        i = j - 1
        # and insert it into the sorted sequence on the left
        while i > -1 and L[i] < key:
            L[i + 1] = L[i]
            i = i - 1
        L[i + 1] = key

def linearSearch(v, L):
    for i in range(len(L)):
        if L[i] == v:
            return i + 1
    return

def addBin(A, B):
    C = []
    carry = 0
    add = 0
    for i in range(len(A), -1):
        add = A[i] + B[i] + carry
        carry = 0
        if add == 3:
            C[i] = 1
            carry = 1
        elif add == 2:
            C[i] = 0
            carry = 1
        elif add == 1:
            C[i] = 1
            carry = 0
        elif add == 0:
            C[i] = 0
            carry = 0
    return C


L = [5,2,4,6,1,3]
# print(L)
# inSortR(L)
# print(L)
print(linearSearch(1, L))