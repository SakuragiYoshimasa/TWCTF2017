
f = open('art_ascii.txt', 'r')

dots = []
full = ''
n = 1
for l in f:
    print(l[46:-1])
    if n == 1:
        full += l[46 + 8:-1].ljust(8,' ')
        n +=1
        continue


    #dots.append(l[46:-1].ljust(16,' '))
    full += l[46:-1].ljust(16,' ')
    n+=1
    print(len(l[46:-1].ljust(16,' ')))


print(len(dots))
print(len(full))
#print(full)
print(full[-300:-1])
f.close()



for j in range(4,30):
    print('-*******************')
    print(j)
    print('-*******************')
    for i in range(int(len(full) / j)):
        print(full[i * j: (i + 1) * j])



'''
for i in range(2, 20):
    #if len(dots) % i != 0: continue
    print('-*******************')
    print(i)
    print('-*******************')
    for j in range(int(len(dots)/ i)):
        s = ''
        for k in range(i):
            s += dots[i * j + k]

        print(s)
'''
