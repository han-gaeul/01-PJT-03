import sys

sys.stdin = open("_소득불균형.txt")

# n명의 사람의 소득이 주어졌을 때
# 평균 이하의 소득을 가진 사람들의 수 출력

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# T개의 테스트 케이스에 대해 각각 두 줄로 주어진다
# 첫 번째 줄에는 정수의 개수 N이 주어지며
# 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다

# 각 테스트 케이스마다 '#x' 출력하고
# 한 줄씩 평균 이하의 소득을 사진 사람들의 수 출력

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    income = list(map(int, input().split()))
    
    #* 평균 소듣
    incomeAvg = sum(income) / N

    #* 소득이 평균 이하인 사람의 숫자
    count = 0

    #* income의 요소를 하나씩 확인
    for i in income:
        #* 만약 i가 평균 소득과 같다면
        if i <= incomeAvg:
            #* count에 1 추가
            count += 1
    
    print('#{} {}'.format(tc, count))