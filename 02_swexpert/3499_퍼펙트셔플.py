for tc in range(int(input())):
    card_len = int(input())
    card = input().split()
    half = (card_len + 1) // 2
    new_card = [0] * card_len
    for i in range(card_len):
        new_card[i // half + (i % half) * 2] = card[i]

    print("#{} ".format(tc+1), end="")
    print(*new_card)
