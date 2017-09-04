# coding: UTF-8
import socket
import itertools
import time
import math

#input is N integers and d is a number of digits of N
#if all_sum - new_val == 0, the set extracted inv_ans_ind by all indices is answer
def solve2(_inputs, d):

    indices = [i for i in range(len(_inputs))]
    all_sum = sum(_inputs)
    print('sum:' + str(all_sum))
    bef_dic = {}

    for i in range(len(indices)):
        #First
        if i == 0:
            for j in range(len(indices)):
                bef_dic[str(j).rjust(d + 1)] = _inputs[j]

        else:
            new_dic = {}
            print(len(bef_dic))
            for key, val in bef_dic.items():
                last = int(key[-d-1:])

                for j in range(last + 1, len(indices)):
                    new_val = val + _inputs[j]
                    new_dic[key + str(j).rjust(d + 1)] = new_val

                    if new_val == 0:
                        print('Found')
                        ans_ind = list(map(lambda n:int(n), filter(lambda s:s!=' ' and s!='', (key + str(j).rjust(d + 1)).split(' '))))
                        return [_inputs[r] for r in ans_ind]

                    elif all_sum - new_val == 0:
                        print('Remain Found')
                        inv_ans_ind = list(map(lambda n:int(n), filter(lambda s:s!=' ' and s!='', (key + str(j).rjust(d + 1)).split(' '))))
                        ans_ind = [r for r in indices if r not in inv_ans_ind]
                        elapsed_time = time.time() - start
            bef_dic = new_dic

# Firstly, calc all sum of all combinations of negative integers,
# Secondly, find a combinations which sum of match with negative set
# Here, if once over the 0, more combinations have not been considered.
# flipped is true when len(pos) < len(neg)
'''
def solve3(_neg, _pos, flipped=False):

    #construct negative dictionary
    #key is a sum value
    start = time.time()
    neg_dict = {}
    neg_min = [0 for i in range(len(_neg))]

    for l in range(1, len(_neg) + 1):
        combs = list(itertools.combinations(_neg, l))
        for comb in combs:
            comb_list = list(comb)
            val = sum(comb_list)
            neg_dict[val] = comb_list
            if val < neg_mins[l]: neg_mins[l] = val
    elapsed_time = time.time() - start
    print ("elapsed_time at coml:{0}".format(elapsed_time) + "[sec]")

    pos_indices = [i for i in range(len(_pos))]
    d = int(math.log10(len(_pos)) + 1)
    bef_dic = {}

    for l in range(len(pos_indices)):
        #First
        if l == 0:
            for j in range(len(indices)):
                bef_dic[str(j).rjust(d + 1)] = _pos[j]

        else:
            new_dic = {}
            print(len(bef_dic))
            for key, val in bef_dic.items():
                last = int(key[-d-1:])

                for j in range(last + 1, len(indices)):
                    new_val = val + _pos[j]
                    if new
                    new_dic[key + str(j).rjust(d + 1)] = new_val

            bef_dic = new_dic
'''

# for level in range(len(inp)):
#   最初は全てlevel1の集合に入れる O(N)
#   levelが偶数ならその半分のlevelの集合からふたつ選んで合成
#   levelが奇数ならlevel/2とlevel/2 + 1の集合からふたつ選んで合成
def solve4(_inputs, maxLevel):

    indices = [i for i in range(len(_inputs))]
    all_level_set = {} #値とindexのリスト

    for level in range(1, len(indices) + 1):
        print('level: %d' % level)
        level_set = {}
        if level == 1:
            for i in range(len(indices)):
                level_set[_inputs[i]] = set([i])

        else:
            target1_level = int(level / 2)
            target2_level = int(level / 2) + 1 if level % 2 == 1 else int(level / 2)

            for k1, v1 in all_level_set[target1_level].items():
                if (-k1 in all_level_set[target2_level]) and (len(v1 & all_level_set[target2_level][-k1]) == 0):
                    print('Found and return ans')
                    ans_set = v1 | all_level_set[target2_level][-k1]
                    ans_list = list(ans_set)
                    ans = [_inputs[i] for i in ans_list]
                    return ans

                if level > maxLevel / 2: continue
                for k2, v2 in all_level_set[target2_level].items():
                    if k1 < k2: break
                    if(len(v1 & v2) == 0):
                        level_set[k1 + k2] = v1 | v2
        all_level_set[level] = level_set

def solve5(_neg, _pos, flipped=False):
    neg_dict = {}
    all_level_neg_set = {}
    all_sum = sum(_neg) + sum(_pos)
    start = time.time()
    for level in range(1, len(_neg) + 1):
        level_set = {}
        if level == 1:
            for i in range(len(_neg)):
                level_set[_neg[i]] = set([_neg[i]])
        else:
            target1_level = int(level/2)
            target2_level = int(level/2) if level % 2 == 0 else int(level / 2) + 1

            for k1, v1 in all_level_neg_set[target1_level].items():
                for k2, v2 in all_level_neg_set[target2_level].items():
                    if(len(v1 & v2) == 0): level_set[k1 + k2] = v1 | v2
        all_level_neg_set[level] = level_set
        neg_dict.update(level_set)
    elapsed_time = time.time() - start
    print ("elapsed_time at construct neg set:{0}".format(elapsed_time) + "[sec]")

    all_level_pos_set = {}
    start = time.time()
    for level in range(1, len(_pos) + 1):
        level_set = {}
        if level == 1:
            for i in range(len(_pos)):
                level_set[_pos[i]] = set([_pos[i]])
        else:
            target1_level = int(level/2)
            target2_level = int(level/2) if level % 2 == 0 else int(level / 2) + 1

            for k1, v1 in all_level_pos_set[target1_level].items():
                for k2, v2 in all_level_pos_set[target2_level].items():

                    if(len(v1 & v2) == 0):
                        pos_sum = k1 + k2
                        level_set[pos_sum] = v1 | v2

                        if -pos_sum in neg_dict:

                            elapsed_time = time.time() - start
                            print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
                            return  list(neg_dict[-pos_sum] | v1 | v2)

                        if all_sum - pos_sum in neg_dict:



        all_level_pos_set[level] = level_set
    return


def solve(_neg, _pos, flipped=False):

    neg_dict = {}
    start = time.time()
    for l in range(1, len(_neg) + 1):
        combs = list(itertools.combinations(_neg, l))
        for comb in combs:
            comb_list = list(comb)
            neg_dict[sum(comb_list)] = comb_list
    elapsed_time = time.time() - start
    print ("elapsed_time at coml:{0}".format(elapsed_time) + "[sec]")

    for l in range(1, len(_pos) + 1):
        combs = list(itertools.combinations(_pos, l))

        for comb in combs:
            comb_list = list(comb)
            pos_sum = sum(comb_list)
            #Found
            if -pos_sum in neg_dict:
                ans = []
                if not flipped:
                    ans = neg_dict[-pos_sum]
                    ans.extend(comb_list)
                else:
                    ans = comb_list
                    ans.extend(neg_dict[-pos_sum])
                elapsed_time = time.time() - start
                print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
                return  ans

if __name__ == '__main__':

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('backpacker.chal.ctf.westerns.tokyo', 39581))
    bef, inp_str, ans_str = '', 'Input: ', 'Your Answer: '
    ans_array = []

    while True:
        recv = s.recv(8092).decode('UTF-8')
        if recv == '':
            break

        for line in recv.split('\n'):
            print(line)
            if bef == inp_str:
                temp = line
                problem = [int(l) for l in temp.split(' ')]
                N = problem[0]

                while N != len(problem[1:]):
                    temp += s.recv(8092).decode('UTF-8').split('\n')[0]
                    problem = [int(l) for l in temp.split(' ')]

                neg, pos = list(filter(lambda i:i<0, problem[1:])), list(filter(lambda i:i>0, problem[1:]))
                ans_array = solve5(neg, pos) if len(neg) < len(pos) else solve5(pos, neg, True)

            if line == ans_str:
                ans_array.sort()
                ans = str(len(ans_array))
                for n in ans_array: ans += ' ' + str(n)
                ans += '\n'
                s.send(ans.encode('utf-8'))
                print(ans.encode('utf-8'))
            bef = line
    s.close()
