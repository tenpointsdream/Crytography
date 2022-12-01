def sBoxShift(output, input, left_right):
  if left_right == False:
    row = 0
    i = 0
    reserved = [None]*4
    while True: 
      if i == 4:
        shiftRight(output, reserved, row)
        i = 0
        row += 1
        reserved = [None]*4
      if row == 4:
        break
      reserved[i] = input[4*row + i]
      i += 1
  else:
    row = 0
    i = 0
    reserved = [None]*4
    while True: 
      if i == 4:
        shiftLeft(output, reserved, row)
        i = 0
        row += 1
        reserved = [None]*4
      if row == 4:
        break
      reserved[i] = input[4*row + i]
      i += 1

def shiftLeft(output, reserved, row):
  if row == 0:
    for i in range(4):
      output[i] = reserved[i]
  elif row == 1:
    for i in range(3):
      output[i+4] = reserved[i + 1]
    output[7] = reserved[0]
  elif row == 2:
    for i in range(2):
      output[i+8] = reserved[i + 2]
    for i in range(2):
      output[i+10] = reserved[i]
  else:
    for i in range(3):
      output[i+13] = reserved[i]
    output[12] = reserved[3]

def shiftRight(output, reserved, row):
  if row == 0:
    for i in range(4):
      output[i] = reserved[i]
  elif row == 1:
    for i in range(3):
      output[i+5] = reserved[i]
    output[4] = reserved[3]
  elif row == 2:
    for i in range(2):
      output[i+8] = reserved[i + 2]
    for i in range(2):
      output[i+10] = reserved[i]
  else:
    for i in range(3):
      output[i+12] = reserved[i+1]
    output[15] = reserved[0]
input = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
output = [None]*16
sBoxShift(output, input, True)
output2 = [None]*16
print(output)
sBoxShift(output2, input, False)
print(output2)