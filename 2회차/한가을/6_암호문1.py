import sys

sys.stdin = open("_암호문1.txt")

# 0 ~ 999999 사이의 수를 나열하여 만든 암호문이 있다
# 급히 수정해야 할 일이 발생했는데 특수 제작된 처리기로만 수정이 가능
# 이 처리기는 1개의 기능을 제공한다
# 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입하며 s는 덧붙일 숫자들

# 첫 번째 줄에는 원본 암호문의 길이
# 두 번째 줄에는 원본 암호문
# 세 번째 줄에는 명령어의 개수
# 네 번째 줄에는 명령어가 주어짐
# 총 10개의 테스트 케이스가 주어진다

# 문자열이 주어졌을 때 암호문을 수정하고 결과의 처음 10개 숫자 출력

# for _ in range(1, 11):
#     originalCodeLength = int(input())
#     originalCode = input().split()

#     commandNumber = int(input())
#     command = input().split()

#     for index in range(len(command)):
#         if command[index] == 'l':
#             x = int(command[index + 1])
#             y = int(command[index + 2])

#             for i in range(y):
#                 originalCode.insert(x, command[index + 3])
#                 x += 1
#                 index += 1
    
#     word = ''

#     for j in range(10):
#         word += originalCode[j] + ' '

#     print(f'#{_} {word}')

#! --------------------------------

for _ in range(1, 11):

    originalCodeLength = int(input())
    originalCode = input().split()
    commandNumber = int(input())
    command = input().split()

    for idx in range(len(command)):
            if command[idx] == 'I':
                    x = int(command[idx + 1]) 
                    y = int(command[idx + 2])

                    for i in range(y):
                            originalCode.insert(x, command[idx + 3])
                            x += 1
                            idx += 1

    word = ''

    for j in range(10):
        word += originalCode[j] + " "
        
    print(f'#{_} {word}') 