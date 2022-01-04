# 피보나치 수 3

# 피사노 주기: 피보나치 수를 어떤 수 K로 나눌 때 가지는 주기
# 주기의 길이: 나누는 수가 10 ^ K (K > 2) 일때 15 * 10 ^ (K - 1)

P = 15 * (10 ** 5)

N = int(input()) % P

fibo = [0, 1]

for idx in range(1, N):
    fibo.append((fibo[idx] + fibo[idx - 1]) % 1000000)

print(fibo[-1])
