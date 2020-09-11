import pandas as pd
from math import cos, asin, sqrt, pi

x = pd.read_excel('/home/rafael/Desktop/testing.xlsx')
a = x.values.tolist()


def distance(lat1, lon1, lat2, lon2):
    p = pi/180
    a = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p) * cos(lat2*p) * (1-cos((lon2-lon1)*p))/2
    return 12742 * asin(sqrt(a))

list_of_lat = []
for i in a:
    list_of_lat.append(i[1])


def heap_sort(a):
    for i in range(1, len(a), 1):
        j = i
        while j > 0 and a[j] > a[(j - 1) // 2]:
            a[j], a[(j - 1) // 2] = a[(j - 1) // 2], a[j]
            j = (j - 1) // 2

    for k in range(0, len(a) - 1, 1):
        a[0], a[len(a) - 1 - k] = a[len(a) - 1 - k], a[0]
        n = 0
        while 2 * n + 1 < len(a) - 1 - k:
            maximum = n
            if a[maximum] < a[2 * n + 1]:
                maximum = 2 * n + 1
            if 2 * n + 2 < len(a) - 1 - k and a[maximum] < a[2 * n + 2]:
                maximum = 2 * n + 2
            if maximum == n:
                break
            else:
                a[maximum], a[n] = a[n], a[maximum]
            n = maximum
    return a


sort = heap_sort(list_of_lat)
all_sort = []
for i in range(len(a)):
    for j in a:
        if sort[i] == j[1]:
            [all_sort.append(j[k]) for k in range(len(sort))]
print(all_sort)
