import sys

sys.stdin = open("_신용카드만들기1.txt")

# 신용카드 번호는 룬 공식(LUHN Formula)을 만족해야 함
# 룬 공식이란 카드 번호에서 마지막 자리(열여섯번째) 숫자 N을 구하는 공식

# 매 홀수 자리의 숫자마다 2를 곱해서 더함
# 매 짝수 자리의 숫자는 그대로 더함
# 위의 두 조건을 더한 숫자에 N을 더한 숫자가
# 10으로 나눴을 때 나눠 떨어지면 유효한 숫자

# 16자리의 카드 번호 중 처음 15개가 주어졌을 때
# 룬 공식을 만족하기 위해 마지막에 들어가야하는 숫자 N을 구하라

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스는 한 개의 줄로 이루어지며 각 줄에는 자연수 15개가 주어진다

# 출력 예시
#1 0
#2 2
#3 5
#4 1
#5 2
#6 0
#7 3
#8 6
#9 9
#10 1

T = int(input())

for tc in range(1, T + 1):
    cardNumber = list(map(int, input().split()))

    #* 15개의 숫자를 더할 변수 초기화
    sum_ = 0
    N = 0

    for i in range(15):
        if i % 2 == 0:
            sum_ += cardNumber[i] * 2
        else:
            sum_ += cardNumber[i]

    for j in range(10):
        if (sum_ + j) % 10 == 0:
            N += j
            break

    print('#{} {}'.format(tc, N))