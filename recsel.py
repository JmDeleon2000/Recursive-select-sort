
a = [1000, 1, 8, 2, 0, 1, -6, 3, 5, 9, 8, 9, 1, 3, 0, -100]


def recsel(array):
    def recselint(n):
        if n == 1:
            return
        k = array[n-1]
        i = n-2
        recselint(n-1)
        while i >= 0 and array[i] > k:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = k

    recselint(len(array))
    return array

recsel(a)
print(a)