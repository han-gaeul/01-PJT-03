import sys

sys.stdin = open("_문자열의거울상.txt")

# 'b', 'd', 'p', 'q'로 이루어진 문자열이 주어진다
# 거울에 비추면 어떤 문자열이 되는지 구하라
# 예 : 'bdppq'를 거울에 비추면 'pqqbd'처럼 나타남

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는 'b', 'd', 'p', 'q' 만으로 이루어진
# 하나의 문자열이 주어진다

# 출력 예시
#1 pqqbd
#2 bddqqqpppp

# b -> d
# d -> b
# p -> q
# q -> p

T = int(input())

for tc in range(1, T + 1):
    word = list(input())
    word.reverse()

    for i in range(len(word)):
        if word[i] == 'b':
            word[i] = 'd'
        elif word[i] == 'd':
            word[i] = 'b'
        elif word[i] == 'p':
            word[i] = 'q'
        elif word[i] == 'q':
            word[i] = 'p'
    
    print('#{} {}'.format(tc, ''.join(word)))