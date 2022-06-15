
k=int(input())

# Den här hittar talen vars kubsumma är k

for i in range(100):
    for j in range(100):
        if i**3+j**3==k:
            print(i,j)
