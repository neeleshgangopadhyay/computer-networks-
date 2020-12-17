def xor(a, b):
    result = []

    # If bits are same XOR is 0, else 1
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)


def BinDiv(genlen, msg, gen):
    pick = genlen
    tmp = msg[0:pick]

    while pick < len(msg):
        if tmp[0] == "1":
            tmp = xor(gen, tmp) + msg[pick]
        else:
            tmp = xor('0' * pick, tmp) + msg[pick]

        pick += 1

    if tmp[0] == '1':
        tmp = xor(gen, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp


def main():
    message = input("Enter the polynomial : ") #dataword
    divisor = "10001000000100001"
    message = str(int(message) * (10**(len(divisor) - 1))) #dataword
    print("CRC Generating Polynomial = " + divisor)
    print("Modified t[u] = " + message)
    rem = BinDiv(len(divisor),message,divisor)
    codeword = str(int(message) + int(rem))
    print("Codeword = ",codeword)
    choice = int(input("Test Error Detection : (1-Yes)(0-No)"))
    if choice == 1:
        pos = int(input("Enter the position to insert the error : "))
        codeword = list(codeword)
        if codeword[pos-1]=='1':
            codeword[pos-1]='0'
        else:
            codeword[pos-1]='1'
        code=''
        for i in range(len(codeword)):
            code += codeword[i]
        print("Incorrect Codeword : " + code)
        syn = BinDiv(len(divisor), code, divisor)
        print("Syndrome : " + syn)
        if int(syn) == 0:
            print("NO ERROR!")
        else:
            print("Error detected!")

    else:
        syn = BinDiv(len(divisor), codeword, divisor)
        print("Syndrome : " + syn)
        if int(syn) == 0:
            print("NO ERROR!")








if __name__ == '__main__':
    main()