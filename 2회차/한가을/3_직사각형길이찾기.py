
import sys

sys.stdin = open("_직사각형길이찾기.txt")

# 직사각형의 네 변 중에서 세 변의 길이가 주어진다
# 나머지 한 변의 길이가 얼마인지 출력
# 세 변의 길이는 상하좌우 어디든 될 수 있으므로 순서는 중요하지 않음

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는 세 자연수 a, b, c가 주어진다

T = int(input())

for tc in range(1, T + 1):
    number = list(map(int, input().split()))
    number.sort()

    if number[0] != number[1]:
        print('#{} {}'.format(tc, number[0]))
    else:
        print('#{} {}'.format(tc, number[2]))