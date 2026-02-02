n = int(input())

points = map(int,input().split()) #Using Direct iterator
mini = maxi = next(points)
count = 0

for point in points:
    if point>maxi:
        maxi = point
        count+=1
    elif point<mini:
        mini = point
        count+=1
print(count)


#%------------Using_List------------%#
# n = int(input())
# points = list(map(int,input().split()))
# mini = maxi = points[0]
# count = 0
# for point in points[1:]:
#     if point>maxi:
#         maxi = point
#         count+=1
#     elif point<mini:
#         mini = point
#         count+=1
# print(count)