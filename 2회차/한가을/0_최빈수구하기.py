import sys

sys.stdin = open("_최빈수구하기.txt")

# 고등학생 1,000명의 수학 성적을 토대로 통계 자료를 만들려고 한다
# 학교에서는 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데
# 최빈수는 특정 자료에서 가장 여러 번 나타나는 값을 의미

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고
# 그 다음 줄부터는 점수가 주어진다

# # 부호와 함께 테스트 케이스의 번호를 출력
# 공백 문자 후 최빈수 출력
# 최빈수가 여러 개일 때는 가장 큰 점수 출력

# 출력 예시
#1 71
#2 76
#3 79
#4 80
#5 52
#6 66
#7 35
#8 97
#9 92
#10 72

T = int(input())

for _ in range(1, T + 1):
    tc = int(input())
    mathScore = list(map(int, input().split()))
    data = [0] * 1001

    #* mathScore의 값을 하나씩 확인
    #* 그 값을 인덱스로 해서 data 리스트의 해당 인덱스에 1씩 증가
    for i in mathScore:
        data[i] += 1

    #* data 리스트 값들 중 최대값 구하기
    maxValue = max(data)
    #* 여러 개의 최빈값을 담을 리스트 정의
    result = []

    #* data 리스트의 요소를 하나씩 확인
    for i in range(len(data)):
        #* 그 값이 maxValur와 같다면
        if data[i] == maxValue:
            #* result에 추가
            result.append(i)
    
    print('#{} {}'.format(tc, max(result)))