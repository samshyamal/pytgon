a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
l = []
f = []

for i in a:
     for j in b:
         if i == j:
           l.append(i)
for k  in l:
    if k not in f:
        f.append(k)
print(f)
