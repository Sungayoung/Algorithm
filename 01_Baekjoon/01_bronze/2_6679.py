for i in range(1000, 10000):
    dec_num = 0
    duodenary_num = 0
    hex_num = 0
    
    num = i
    while num > 0:
        dec_num += num % 10
        num = num // 10
   
    num = i
    while num > 0:
        duodenary_num += num % 12
        num = num // 12
    
    num = i
    while num > 0:
        hex_num += num % 16
        num = num // 16
    
    if dec_num == hex_num and hex_num == duodenary_num and dec_num == duodenary_num:
        print(i)
    