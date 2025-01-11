print("Enter 'exit' for exit.")
while True:
        ipei = input('Please enter IPEI: ')
        if ipei == 'exit':
            break
        else:
            try:
                first_part = ipei[:5]
                second_part = ipei[5:-1]

                hex_first_part = str(hex(int(first_part)))
                hex_second_part = str(hex(int(second_part)))
                str_r = (str(hex_first_part)+str(hex_second_part))
            except ValueError:
                print("it's not IPEU, try again!")
            else: print(str_r[:1] + str_r[2:6] + str_r[-5:])