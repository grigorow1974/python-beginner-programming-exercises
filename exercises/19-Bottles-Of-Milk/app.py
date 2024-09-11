# ✅↓ Write your code here ↓✅
def number_of_bottles():
    x = 99
    while x >= 0:
        if x == 1:
            print ('1 bottle of milk on the wall, 1 bottle of milk')
            print('Take one down and pass it around, no more bottles of milk on the wall')
        elif x==0:
            print ('No more bottles of milk on the wall, no more bottles of milk')
            print ('Go to the store and buy some more, 99 bottles of milk on the wall')
        else:
            print (f'{x} bottles of milk on the wall, {x} bottles of milk')
            print(f'Take one down and pass it around, {x-1} bottles of milk on the wall')
        x -= 1
number_of_bottles()