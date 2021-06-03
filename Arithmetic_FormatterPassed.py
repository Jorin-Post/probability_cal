file = open("test_module.txt")

def open_file():
    findL = line.find('arithmetic_arranger(["')
    if findL == 17:
      r1 = line.replace('"', '')
      r2 = r1.replace(',', '')
      r3 = r2.replace('actual = arithmetic_arranger([', '')
      r4 = r3.replace('])', '')
      r5 = r4.replace(']', '')
      nm = r5.split()
      return nm 

def make_plate(n):
  if n != None:
    
    s1 = 0
    s4 = 0
   
    nm0 = nm[0]
    nm1 = nm[1]
    nm2 = nm[2]
    l2 = len(nm[0])
    l4 = len(nm[2])

    l1 = l4 + 3 - l2
    while s1 < l1:
      s1 = s1 + 1
      print(' ', end='')

    print(nm0, '\n', nm1, nm2)

    while s4 < (l4 + 3):
      s4 = s4 + 1
      print('-', end='')
    print('')

    try:
      nm1 = int(nm[0])
      nm2 = int(nm[2])

      op = ord(nm[1])

      if not op == 43 and not op == 45:
          print("Error: Operator must be '+' or '-'.\n")
          
      if (l2 > 4 or l4 > 4):
          print("Error: Numbers cannot be more than four digits.\n")
          
      else:
          if op == 43:
            add = nm1 + nm2
            str_add = str(add)
            ladd = len(str_add)

            while ladd < (l4 + 3):
              ladd = ladd + 1
              print(' ', end='')

            print(add, '\n')
          
          if op == 45:
            sub = nm1 - nm2
            str_sub = str(sub)
            lsub = len(str_sub)

            while lsub < (l4 + 3):
              lsub = lsub + 1
              print(' ', end='')

            print(sub, '\n')
            
    except ValueError as v:
      print("Error: Numbers must only contain digits.\n")

for line in file:  
  nm = open_file()
  make_plate(nm)
print('Done!')