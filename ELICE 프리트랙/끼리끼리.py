# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
card = []
red_pocket = []
blue_pocket = []
card_box = []

# 지시사항 1번을 참고하여 코드를 작성하세요.
N = int(input())
for i in range(N):
    card = int(input())
    if card >= 0 :
        red_pocket.append(card)
    else:
        blue_pocket.append(card)

card_box.append(red_pocket) 
card_box.append(blue_pocket) 

# 아래 코드는 결과를 확인하기 위한 코드입니다.
print(card_box)