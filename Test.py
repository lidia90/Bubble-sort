a = [64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]

for i in range(len(a)):
    for j in range(i + 1, len(a)):

        if a[i] > a[j]:
           a[i], a[j] = a[j], a[i]

print (a)
