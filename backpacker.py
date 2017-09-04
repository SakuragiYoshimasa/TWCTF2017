import subprocess
import itertools

c = 'nc backpacker.chal.ctf.westerns.tokyo 39581'

p = subprocess.Popen(['nc' ,'backpacker.chal.ctf.westerns.tokyo', '39581'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

#data = open("sample.txt", "r").read()

output = p.communicate()[0].decode('UTF-8')
bef = ''
ans_array = []

for line in output.split('\n'):

    if bef != 'Your Answer: ':
        print(line)
    else:
        ans = str(len(ans_array))
        for n in ans_array: ans += ' ' + str(n)
        print(b'%b' % ans.encode('UTF-8'))
        print(line)
        print(sum(ans_array))
        print(ans_array)


    if bef == 'Input: ':
        problem = [int(l) for l in line.split(' ')]
        N = problem[0]
        integers = problem[1:]
        neg = []
        pos = []

        for i in integers:
            if i < 0: neg.append(i)
            else: pos.append(i)

        neg_dict = {}

        for l in range(1, len(neg) + 1):
            combs = list(itertools.combinations(neg, l))

            for comb in combs:
                comb_list = list(comb)
                neg_dict[sum(comb_list)] = comb_list

        for l in range(1, len(pos) + 1):
            combs = list(itertools.combinations(pos, l))

            for comb in combs:
                comb_list = list(comb)
                pos_sum = sum(comb_list)

                #Found
                if -pos_sum in neg_dict:
                    #print(comb_list)
                    ans_array =  neg_dict[-pos_sum]
                    ans_array.extend(comb_list)

                    #print(ans_array)


    bef = line
