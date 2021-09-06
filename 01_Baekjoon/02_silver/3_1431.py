from functools import cmp_to_key

def priority(word1, word2):
    # 1. A와 B의 길이가 다르면, 짧은 것이 먼저 온다.
    if len(word1) < len(word2): # word1의 길이가 word2의 길이보다 짧으면 word1을 앞으로 보냄
        return -1
    elif len(word1) > len(word2):
        return 1
    else:
        # 2. 만약 서로 길이가 같다면, A의 모든 자리수의 합과 B의 모든 자리수의 합을 비교, 작은 합을 가지는 것이 먼저온다
        word1_num = 0
        word2_num = 0
        for word in word1:
            if word.isdecimal():
                word1_num += int(word)
        for word in word2:
            if word.isdecimal():
                word2_num += int(word)
        if word1_num < word2_num:
            return -1
        elif word1_num > word2_num:
            return 1
        else:
            # 3. 1,2번 조건으로도 비교할 수 없으면 사전순으로 비교
            if word1 < word2:
                return -1
            else:
                return 1

        
T = int(input())
input_list = []
for i in range(T):
    input_list.append(input())

result_list = sorted(input_list, key=cmp_to_key(priority))
for result in result_list:
    print(result)

# if(x[0] < y[0]): # x[0] 값이 y[0]값 보다 작으면
# 		return 1 # y 내용을 앞으로 보냄
# 	elif(x[0] > y[0]):
# 		return -1
# 	else: # x[0] 값이 y[0]값과 동일하면
# 		if(x[1] < y[1]): # x[1]과 y[1]을 비교해서 y[1]이 크면
# 			return -1 # x 내용을 앞으로 보냄
# 		elif(x[1] > y[1]):
# 			return 1
# 		else:
# 			return 0