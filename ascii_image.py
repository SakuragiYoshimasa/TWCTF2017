f = open('art_ascii.txt', 'r')

data = []
full = ''
n = 1
for l in f:
    #print(l[9:9+8] + l[18:18+8] + l[27:27+8] + l[36:36+8])
    if n == 1:
        full += l[27:27+8] + l[36:36+8]
        n+=1
        continue
    #if n == 371:
    #    full += l[9:9+8] + l[18:18+8] + l[27:27+8] + l[36:36+6]
    #    n+=1
    #    continue

    full += l[9:9+8] + l[18:18+8] + l[27:27+8] + l[36:36+8]
    n += 1

print('len:' + str(len(full)))

    #dots.append(l[46:-1].ljust(16,' '))
    #full += l[46:-1].ljust(16,' ')
    #print(len(l[46:-1].ljust(16,' ')))
f.close()


import numpy as np
from PIL import Image

data = []

h = 64
'''
1
2
3
4
6
8
12
13
19
24
26
38
39
52
57
76
78
104
114
152
156
228
247
312
456
494
741
988
'''

w = int(len(full) / 6 / h)

for j in range(h):

    row_data = []

    for i in range(w):

        r1 = int(full[(j * w + i) * 6], 16)
        r2 = int(full[(j * w + i) * 6 + 1], 16)
        g1 = int(full[(j * w + i) * 6 + 2], 16)
        g2 = int(full[(j * w + i) * 6 + 3], 16)
        b1 = int(full[(j * w + i) * 6 + 4], 16)
        b2 = int(full[(j * w + i) * 6 + 5], 16)
        '''
        r1 = int(full[(j + i * h) * 6], 16)
        r2 = int(full[(j + i * h) * 6 + 1], 16)
        g1 = int(full[(j + i * h) * 6 + 2], 16)
        g2 = int(full[(j + i * h) * 6 + 3], 16)
        b1 = int(full[(j + i * h) * 6 + 4], 16)
        b2 = int(full[(j + i * h) * 6 + 5], 16)
        '''

        r = r1 * 16 + r2
        g = g1 * 16 + g2
        b = b1 * 16 + b2

        row_data.append(np.array([r,g,b]))

        '''
        g1 = int(full[(j * w + i) * 2], 16)
        g2 = int(full[(j * w + i) * 2 + 1], 16)
        row_data.append(g1 * 16 + g2)
        '''


    data.append(np.array(row_data))

pilImg = Image.fromarray(np.uint8(np.array(data)))
pilImg.save('out.jpg', 'JPEG', quality=100, optimize=True)
