# 이진수

def hex_to_bin(_num):
    dec = 0
    if _num.isdecimal():
        dec = int(_num)
    else:
        dec = ord(_num) - 55
    _hex_num = ""
    for _i in range(4):
        if dec & 1 << _i:
            _hex_num = "1" + _hex_num
        else:
            _hex_num = "0" + _hex_num
    return _hex_num


for tc in range(int(input())):
    N, hex_num_list = input().split()
    result = ""
    for hex_num in hex_num_list:
        result += hex_to_bin(hex_num)

    print("#{} {}".format(tc+1, result))