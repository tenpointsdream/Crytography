
def trimBinBlock(Bin9):
  result = ''
  for i in range(8):
    result += Bin9[i+1]
  return result

def xor(block1, block2):
  r = len(block1) * ['']
  i = 0
  while (i < len(block1)):
    if block1[i] == block2[i]:
      r[i] = '0'
    else:
      r[i] = '1'
    i += 1
  result = ''
  for i in r:
    result += i
  #print('Xor of ' + block1 + ' and ' + block2 + ' is: ' + result)
  return result

def decToHex(value):
  if value == 10:
    return 'A'
  elif value == 11:
    return 'B'
  elif value == 12:
    return 'C'
  elif value == 13:
    return 'D'
  elif value == 14:
    return 'E'
  elif value == 15:
    return 'F'
  else:
    return str(value)
  
def hexToDec(letter):
  if letter == 'A' or letter == 'a':
    return 10
  elif letter == 'B' or letter == 'b':
    return 11
  elif letter == 'C' or letter == 'c':
    return 12
  elif letter == 'D' or letter == 'd':
    return 13
  elif letter == 'E' or letter == 'e':
    return 14
  elif letter == 'F' or letter == 'f':
    return 15
  else:
    return int(letter)

def hexToBin(value):
  j = 3
  rs = 4 * ['0']
  result = ''
  while value >= 1:
    rs[j] = str(value % 2)
    value //= 2
    j -= 1
    if j < 0:
      break
    if value == 1:
      rs[j] = '1'
  for i in rs:
    result += i
  return result

def getBin_9bits(hex):
  result = ''
  if len(hex) == 2: 
    l1, l2 = hex[0], hex[1]
    result += '0'
    result += hexToBin(hexToDec(l1))
    result += hexToBin(hexToDec(l2))
  elif len(hex) == 1:
    l = hex[0]
    result += '00000'
    result += hexToBin(hexToDec(l))
  else:
    l1, l2 = hex[1], hex[2]
    result += '1'
    result += hexToBin(hexToDec(l1))
    result += hexToBin(hexToDec(l2))
  return result

def getHex_1byte(Bin8):
  result1 = 0
  result2 = 0
  result = ''
  i = 0
  j = 3
  while i < 4:
    if Bin8[i] == '1':
        result1 += 2**j
    j -= 1
    i += 1
  i = 4
  j = 3
  
  while i < 8:
    if Bin8[i] == '1':
        result2 += 2**j
    j -= 1
    i += 1
  result = decToHex(result1) + decToHex(result2)
  return result

galois_2p8 = '100011011'

def xor_gf(bin9):
    if bin9[0] == '1':
        #xor galois field
        bin9 = xor(bin9, galois_2p8)
    return bin9

def galois_multi(value, multiplier):
    x = value
    x2 = value
    org_x = getBin_9bits(str(hex(x2)[2:]).upper())
    #print(org_x)
    #shift
    x = x << 1
    y = getBin_9bits(str(hex(x)[2:]).upper())
    if y[0] == '1':
        #xor galois field
        y = xor(y, galois_2p8)
    if multiplier == 9:
        #print(y)
        y = trimBinBlock(y)
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        #xor galois field
        if y[0] == '1':
            y = xor(y, galois_2p8)
        y = trimBinBlock(y)
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        #xor itself
        return trimBinBlock(xor(y, org_x))
    elif multiplier == 11:
        y = trimBinBlock(y)
        #print(y)
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        #xor itself
        y = trimBinBlock(xor(y, org_x))
        #print(y)
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        #print(y)
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        #xor itself
        return trimBinBlock(xor(y, org_x))
    elif multiplier == 13:
        #xor itself
        y = trimBinBlock(xor(y, org_x))
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        y = trimBinBlock(y)
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        #xor itself
        return trimBinBlock(xor(y, org_x))
    elif multiplier == 14:
        #xor itself
        y = trimBinBlock(xor(y, org_x))
        #print(y)
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        #xor itself
        y = trimBinBlock(xor(y, org_x))
        x3 = getHex_1byte(y)
        x4 = int(x3, base=16)
        #print(hex(x4))
        #shift
        x4 = x4 << 1
        y = getBin_9bits(str(hex(x4)[2:]).upper())
        if y[0] == '1':
            #xor galois field
            y = xor(y, galois_2p8)
        return trimBinBlock(y)
    elif multiplier == 2:
        return trimBinBlock(y)
    elif multiplier == 3:
        #xor itself
        return trimBinBlock(xor(y, org_x))
    else: 
        return trimBinBlock(getBin_9bits(str(hex(x2)[2:]).upper()))

def mixCol(output, input, inverse):
    #Mix Columns matrix
    mC = [[2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]]
    #Inverse Mix Columns matrix (in decimal form)
    iMC = [[14, 11, 13, 9],
            [9, 14, 11, 13],
            [13, 9, 14, 11],
            [11, 13, 9, 14]]
    for i in range(len(input)):
        input[i] = int(input[i], base=16)
    #input matrix column-wise
    c = [[input[0], input[4], input[8], input[12]],
        [input[1], input[5], input[9], input[13]],
        [input[2], input[6], input[10], input[14]],
        [input[3], input[7], input[11], input[15]]]
    #print(c)
    if inverse:
        row = 0
        i = 0
        j = 0
        while (i < 16):
            if j == 4:
                j = 0
                row += 1
            output[i] = getHex_1byte(xor(xor(xor(galois_multi(c[j][0] ,iMC[row][0]), galois_multi(c[j][1], iMC[row][1])), galois_multi(c[j][2], iMC[row][2])), galois_multi(c[j][3], iMC[row][3])))
            #print('This is output: ' + output[i])
            i += 1
            j += 1
    else:
        row = 0
        i = 0
        j = 0
        while (i < 16):
            if j == 4:
                j = 0
                row += 1
            output[i] = getHex_1byte(xor(xor(xor(galois_multi(c[j][0] , mC[row][0]), galois_multi(c[j][1], mC[row][1])), galois_multi(c[j][2], mC[row][2])), galois_multi(c[j][3], mC[row][3])))
            i += 1
            j += 1
output = ['']*16
input = ['47', '40', 'A3', '4C', '37', 'D4', '70', '9F', '94', 'E4', '3A', '42', 'ED', 'A5', 'A6', 'BC']
mixCol(output, input, True)
print(output)

output2 = ['']*16
input2 = ['87', 'F2', '4D', '97', '6E', '4C', '90', 'EC', '46', 'E7', '4A', 'C3', 'A6', '8C', 'D8', '95']
mixCol(output2, input2, False)
print(output2)