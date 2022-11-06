def feistel_cipher(a, b, rounds):
  i = 0
  LH = a
  RH = b
  temp = ''
  key_char =''
  while(i<rounds):
    key_char = input('\nEnter key for round %i: ' %(i+1))
    k = get_binary(ord(key_char))
    temp = RH
    RH = xor(LH, sum_bin(temp, k))
    LH = temp
    print('LH: ' + LH + ' and RH: ' + RH)
    i += 1
  return RH, LH

def get_binary(value):
    j = 7
    rs = 8*['0']
    result = ''
    while value > 1:
        rs[j]= str(value % 2)
        value //= 2
        j -= 1
        if j < 0:
            break
        if value == 1:
            rs[j] = '1'
    for i in rs:
        result += i
    return result

def get_decimal(bin):
    i = len(bin) - 1
    j = 0
    value = 0
    while j < len(bin):
        if i == 0 and bin[j] == '0':
            break
        value += pow(int(bin[j])*2,i)
        j += 1
        i -= 1
    return value
#the function below does the sum of binary block and the key and mod 256 (it does not show in the code, but it just does not take any digit beyond 8 bits)
def sum_bin(block, key):
    sum = len(block)*['']
    i = 0
    carry = 0
    j = len(block) - 1
    while (i < len(block)):
        if carry == 0:
            if block[j] == '1' and key[j] == '1':
                carry = 1
                sum[j] = '0'
            else:
                carry = 0
                sum[j] = str(int(block[j]) + int(key[j]))
        else:
            if block[j] == '1' and key[j] == '1':
                carry = 1
                sum[j] = '1'
            elif block[j] == '1' or key[j] == '1':
                carry = 1
                sum[j] = '0'
            else:
                carry = 0
                sum[j] = '1'
        j -= 1
        i += 1
    result = ''
    for i in sum:
        result += str(i)
    print('Sum of ' + block + ' and ' + key + ' is: ' +result)
    return result


def xor(block, sum):
    r = len(block)*['']
    i = 0
    while (i < len(block)):
        if block[i] == sum[i]:
            r[i] = '0'
        else:
            r[i] = '1'
        i += 1
    result = ''
    for i in r:
        result += i
    print('Xor of ' + block + ' and ' + sum + ' is: ' +result)
    return result

#print(xor('00111111', '01111111'))
text = input('Enter the text block (2 bytes): ')
print('1: ', ord(text[0]), ' and 2: ', ord(text[1]))
C1 = get_binary(ord(text[0]))
C2 = get_binary(ord(text[1]))
print('Binary values: ' + C1 + ' and ' + C2) 
A, B = feistel_cipher(C1, C2, 2)
print('\nResults: ' + A + ' and ' + B)
print('Decimal values: ', get_decimal(A), ' and ', get_decimal(B))
print(chr(get_decimal(A)) + chr(get_decimal(B)))