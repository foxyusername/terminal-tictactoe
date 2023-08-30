#value means x or y

#make array of x and y for game
#draw a board of game with x and y values

#aks user in which quadrat to put value
#check if that quadrat is already filled
#insert value into desired index
#change choice(if x change it to y , if y chnage to x)
#draw it again
#**REPEAT**


#write winning condition and draw condition
#display winning message

list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']

def drawBoard():
    print('\n')

    #row 1

    print(' _______',end="")
    print('  _______',end="")
    print('  _______',end="\n")

    print('|       |',end="")
    print('|       |',end="")
    print('|       |',end="\n")

    print(f'|   {list[0]}   |',end="")
    print(f'|   {list[1]}   |', end="")
    print(f'|   {list[2]}   |',end="\n")

    print('|_______|',end="")
    print('|_______|',end="")
    print('|_______|',end="\n")

    #row 2

    print('|       |',end="")
    print('|       |',end="")
    print('|       |',end="\n")

    print(f'|   {list[3]}   |', end="")
    print(f'|   {list[4]}   |', end="")
    print(f'|   {list[5]}   |', end="\n")

    print('|_______|',end="")
    print('|_______|',end="")
    print('|_______|',end="\n")

    #row 3

    print('|       |',end="")
    print('|       |',end="")
    print('|       |',end="\n")

    print(f'|   {list[6]}   |', end="")
    print(f'|   {list[7]}   |', end="")
    print(f'|   {list[8]}   |',end="\n")

    print('|_______|',end="")
    print('|_______|',end="")
    print('|_______|',end="\n")

    print('\n')

value='Y'

winningCondition=[
 [0,1,2],[3,4,5],[6,7,8],  #vercical
 [0,3,6],[1,4,7],[2,5,8],  #horizontal
 [0,4,8],[2,4,6]           #diagonal
]

#checking the value (X or Y)
def checkValue():
     global value

     if value=='X':
        value='Y'
     else:
        value='X'
        
def gameOver():
    global value
    global list
    
    value='Y'
    list=[' ',' ',' ',' ',' ',' ',' ',' ',' ']               

while True:
      checkValue()
    
      try:
         index=int(input(f'{value} turn. say index '))-1
      except ValueError:
         print('index must be number')

      try:
         if list[index]==' ':
            list[index]=value
            drawBoard()
         else :
            checkValue()
      except :
             print('number must be between 0 and 9')

      for [a,b,c] in winningCondition :
        if value==list[a] and value==list[b] and value==list[c] :
            print(f'CONGRATULATIONS {value} WON THE GAME')
            gameOver()
            break

      try:
          list.index(' ')+1
      except ValueError:
          print('!!GAME WAS DRAW!!')
          gameOver()
          break
    