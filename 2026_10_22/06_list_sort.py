l1 = [10,40,20,30,40]
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

l2 = ['this', 'is', 'python']
l2.sort()
print(l2)

l2.sort(key=lambda x: len(x))
print(l2)

l2.sort(key=lambda x: x[-1]) #sort by last character only
print(l2)