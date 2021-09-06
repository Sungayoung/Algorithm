# 다중 반복문에서 빠져나오기 위해 별도의 함수 작성

def max_card(card_list, max_black):
    max_val = 0
    cur_val = 0

    # 리스트 중 
    for idx_1 in range(len(card_list)):
        for idx_2 in range(idx_1 + 1, len(card_list)):
            for idx_3 in range(idx_2 + 1, len(card_list)):
                cur_val = card_list[idx_1] + card_list[idx_2] + card_list[idx_3]
                print(f"{cur_val} = {card_list[idx_1]}({idx_1}) + {card_list[idx_2]} ({idx_2}) + {card_list[idx_3]} ({idx_3}) ")
                if cur_val <= max_black:
                    if cur_val == max_black:
                        return max_black
                    else:
                        if cur_val > max_val:
                            max_val = cur_val
    return max_val


card_num, max_black = tuple(map(int, input().split()))
card_list = list(map(int, input().split()))

print(max_card(card_list, max_black))
