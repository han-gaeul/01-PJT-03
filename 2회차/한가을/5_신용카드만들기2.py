import sys

sys.stdin = open("_신용카드만들기2.txt")

# 신용카드를 만들려면 아래 두 가지의 조건을 만족해야 한다
# 카드 번호는 3, 4, 5, 6, 9로 시작
# 번호에 '-'이 들어갈 수 있으며 '-'를 제외한 숫자 개수는 16개

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스는 한 개의 줄로 이루어지면
# 각 줄에는 자연수와 '-'로 이루어진 문자열이 주어진다

# 주어진 카드 번호로 신용 카드를 만들 수 있으면 1, 없으면 0 출력

# 출력 예시
#1 0
#2 0
#3 0
#4 1
#5 0
#6 1
#7 0
#8 0
#9 0
#10 0

T = int(input())

for tc in range(1, T + 1):
    cardNumber = input()
    cardNumber = cardNumber.replace('-', '')
    cardNumber = list(cardNumber)

    count = 0

    if cardNumber[0] in ['3', '4', '5', '6', '9'] and len(cardNumber) == 16:
        count += 1
    else:
        count = 0
    
    print(f'#{tc} {count}')