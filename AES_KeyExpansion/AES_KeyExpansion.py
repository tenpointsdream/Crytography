sBoxLookUp = [['63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'],
              ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'],
              ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'],
              ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'],
              ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'],
              ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'],
              ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'],
              ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'],
              ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'],
              ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'],
              ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'],
              ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'],
              ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8D', '8A'],
              ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'],
              ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'],
              ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]

RC = ['01', '02', '04', '08', '10', '20', '40', '80', '1B', '36']

def rotate(input):
    output = [None]*len(input)
    i = 0
    while (i < 3):
        output[i] = input[i + 1]
        i += 1
    output[3] = input[0]
    return output 

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

def SubWord(output, input):
    for i in range(len(input)):
      text = input[i]
      j, k = text[0], text[1]
      output[i] = sBoxLookUp[hexToDec(j)][hexToDec(k)]

def getBin_8bits(hex):
  result = ''
  if len(hex) == 2: 
    l1, l2 = hex[0], hex[1]
    result += hexToBin(hexToDec(l1))
    result += hexToBin(hexToDec(l2))
  else:
    l = hex[0]
    result += '0000'
    result += hexToBin(hexToDec(l))
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

def SubWord_RC(input, round):
    output = ['']*len(input)
    i = 1
    while i < 4:
        output[i] = input[i]
        i += 1
    output[0] = getHex_1byte(xor(getBin_8bits(input[0]), getBin_8bits(RC[round])))
    return output

def keyExpansion(input):
    w0 = [input[0], input[1], input[2], input[3]]
    w1 = [input[4], input[5], input[6], input[7]]
    w2 = [input[8], input[9], input[10], input[11]]
    w3 = [input[12], input[13], input[14], input[15]]
    output = []
    round = 0
    output = w0 + w1 + w2 + w3
    current = ['']*4
    #previous = ['']*4
    j = 0
    z = []
    k = 0
    while round < 10:
        w3 = output[-4:]
        if j == 0:
            if round > 0:
                k -= 1
            w0 = [output[(round + k)*4], output[(round + k)*4 + 1], output[(round + k)*4 + 2], output[(round + k)*4 + 3]]
            k += 1
            rotWord = rotate(w3)
            subWord = rotWord
            SubWord(subWord, rotWord)
            z = SubWord_RC(subWord, round)
            print('Round ', round, ': ', z)
            for i in range(4):
                current[i] = getHex_1byte(xor(getBin_8bits(z[i]), getBin_8bits(w0[i])))
        elif j == 1:
            w1 = [output[(round + k)*4], output[(round + k)*4 + 1], output[(round + k)*4 + 2], output[(round + k)*4 + 3]]
            k += 1
            z = output[-4:]
            for i in range(4):
                current[i] = getHex_1byte(xor(getBin_8bits(z[i]), getBin_8bits(w1[i])))
        elif j == 2:
            z = output[-4:]
            w2 = [output[(round + k)*4], output[(round + k)*4 + 1], output[(round + k)*4 + 2], output[(round + k)*4 + 3]]
            k += 1
            for i in range(4):
                current[i] = getHex_1byte(xor(getBin_8bits(z[i]), getBin_8bits(w2[i])))
        else:
            z = output[-4:]
            w3 = [output[(round + k)*4], output[(round + k)*4 + 1], output[(round + k)*4 + 2], output[(round + k)*4 + 3]]
            k+=1
            for i in range(4):
                current[i] = getHex_1byte(xor(getBin_8bits(z[i]), getBin_8bits(w3[i])))
        j += 1
        output += current
        if j == 4:
            j = 0
            round += 1
    return output
input = ['0F', '15', '71', 'C9', '47', 'D9', 'E8', '59', '0C', 'B7', 'AD', 'D6', 'AF', '7F', '67', '98']
output = keyExpansion(input)
print(output)
print('Length of output array: ', len(output))