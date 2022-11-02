c = []

def go():
    
    w = int(input("Enter values\n"))
    c.append(w)
    main()
        
def push():
    
    n = int(input("Enter the position\n"))
    w = int(input("Enter values\n"))
    c.insert(n,w)
    main()
    
def pop():
    
    print("press 1 for remove by position or press 2 for by object\n")
    x = int(input())
    if x==1 :
        m = int(input("Enter the position\n"))
        c.pop(m)
    elif x==2:
        t = int(input("Enter the Object\n"))
        c.remove(t)
    else:
        main()        
        
    main()
    
def display():
    
    print("here are your values\n")
    for o in range(len(c)):
        print(c[o])
    main()
    
def search():
    
    print("enter the value for search\n")
    a = 0
    s = int(input())
    while True:
        a = a+1
        if c[0]==s:
            print("found at 1 th position")
            break
        elif c[a]==s:
            print("found at",a+1,"th position")
            break
    main()
    
def main():
    
    print("\nPress the value to perform those functions in down there--\n")
    print("0 for Enter in oneshot")
    print("1 for insert")
    print("2 for remove")
    print("3 for display")
    print("4 to search")
    print("press q & Enter\n")
    n = input()
    while n != '5'  :
        
        if n == '0':
            go()
        elif n == '1':
            push()
        elif n== '2':
            pop()
        elif n== '3':
            display()
        elif n== '4':
            search()
        elif n == 'q':
            print("Hope your expireance was good!!")
            break
        else :
            print("sorry does'nt work")
            main()
        break
        
main()
#****************************************************************************************************************************************************************

# This is a one liner for compressed versions to deploy!!
exec("""\nc = []\n\ndef go():\n    \n    w = int(input("Enter values\\n"))\n    c.append(w)\n    main()\n        \ndef push():\n    \n    n = int(input("Enter the position\\n"))\n    w = int(input("Enter values\\n"))\n    c.insert(n,w)\n    main()\n    \ndef pop():\n    \n    print("press 1 for remove by position or press 2 for by object\\n")\n    x = int(input())\n    if x==1 :\n        m = int(input("Enter the position\\n"))\n        c.pop(m)\n    elif x==2:\n        t = int(input("Enter the Object\\n"))\n        c.remove(t)\n    else:\n        main()        \n        \n    main()\n    \ndef display():\n    \n    print("here are your values\\n")\n    for o in range(len(c)):\n        print(c[o])\n    main()\n    \ndef search():\n    \n    print("enter the value for search\\n")\n    a = 0\n    s = int(input())\n    while True:\n        a = a+1\n        if c[0]==s:\n            print("found at 1 th position")\n            break\n        elif c[a]==s:\n            print("found at",a+1,"th position")\n            break\n    main()\n    \ndef main():\n    \n    print("\\nPress the value to perform those functions in down there--\\n")\n    print("0 for Enter in oneshot")\n    print("1 for insert")\n    print("2 for remove")\n    print("3 for display")\n    print("4 to search")\n    print("press q & Enter\\n")\n    n = input()\n    while n != '5'  :\n        \n        if n == '0':\n            go()\n        elif n == '1':\n            push()\n        elif n== '2':\n            pop()\n        elif n== '3':\n            display()\n        elif n== '4':\n            search()\n        elif n == 'q':\n            print("Hope your expireance was good!!")\n            break\n        else :\n            print("sorry does'nt work")\n            main()\n        break\n        \nmain()\n""")
#****************************************************************************************************************************************************************

# we 
def mac(q1,q2):
    v = 1
    
    for noe in range(0,q2):
        v = v * q1
        print(noe)
    print(v)

mac(2,344344)

#****************************************************************************************************************************************************************



weq = 22/7
print(weq)
        
#****************************************************************************************************************************************************************


x = [2]
y = x
print(x is y)

#****************************************************************************************************************************************************************

def sum():
    er = int(input("give 1"))
    me = int(input("give 2"))
    print(me + er)

def goodtogo(doit):
    doit()

goodtogo(sum)

#****************************************************************************************************************************************************************


mew = open('mac.txt', '+a')  

mew.write('this is waht seems like')
#****************************************************************************************************************************************************************




def rest(c,d):
    a = c+d
    print(a)

rest(33,44)

#****************************************************************************************************************************************************************

import math

def square(x):
    result = []
    for y in x:
        result.append(math.pow(y,2.0))
    return result 

print(square([1,2,3]))

#****************************************************************************************************************************************************************



    
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
#****************************************************************************************************************************************************************



aeeeeeee = [1,12,3,43,443,5,46,546,33,7,8,89,89]
aeeeeeee.sort()
print(aeeeeeee)
#****************************************************************************************************************************************************************

def calculateTotalSum(*arguments):
    totalSum = 0
    for number in arguments:
        totalSum += number
    print(totalSum)
 
#****************************************************************************************************************************************************************

def sum(m):
    i = 0
    while m != 0 :
        x = m % 10
        i = i + x
        m = m // 10

    print("\n")
    return i

#****************************************************************************************************************************************************************

def digital_root(n):
    x = str(n)
    r = 0
    while len(x) > 1:
        r = 0
        for i in range(len(x)):
            r = r + int(x[i])
        x = str(r)
    return r

#****************************************************************************************************************************************************************
  
def dit(*arg):
    arg = []

    arg.sort()
    print(arg)


#****************************************************************************************************************************************************************


def addition(n):
    return n + n
  
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))
#****************************************************************************************************************************************************************


def ditw(*arg):    
    d = [None]*len(arg)
    for i in range(0, len(arg)):    
        d[i] = arg[i] 

#****************************************************************************************************************************************************************

def qwe(*argq):    
    alist = [None]*len(argq)
    for i in range(0, len(argq)):    
        alist[i] = argq[i] 
    mergeSort(alist)
    


def mergeSort(alist):
    
    print("Splitting: ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

    print(alist)

mergeSort([234,26,56,75,67,444,788,7,5,43343])
#****************************************************************************************************************************************************************


def qwe(*argq):    
    alist = [None]*len(argq)
    for i in range(0, len(argq)):    
        alist[i] = argq[i] 
    c = len(alist)
    q = 0
    d = 0
    for f in range(c):
        x = alist[f]
        if x.isalpha() :
            q = q+1
        elif x.isdigit() :
            d = d+1
    print("numbers of alpha",q)
    print("numbers of digit",d)


qwe("45","4343","gre","46") 


    
#****************************************************************************************************************************************************************
 
a = 'fsdfsdf'

if a.isalpha() :
    print("is a alpha")
elif a.isdigit() :
    print("is a digit")




#****************************************************************************************************************************************************************
        
        
def qwe(*opse): 
    ops = [None]*len(opse)
    for i in range(0, len(opse)):    
        ops[i] = opse[i]    
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))

        return sum(stack)

#****************************************************************************************************************************************************************

def asd(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    if arr(n / 2) < arr((n / 2) - 1):
        return asd(arr[:n / 2])
    if arr(n / 2) < arr((n / 2) + 1):
        return asd(arr[n / 2:])
    return arr[n / 2]


#****************************************************************************************************************************************************************


def calPoints(ops):
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'c':
            stack.pop()
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'd':
            stack.append(2 * stack[-1])    
        else:
            stack.append(int(op))
    
    return sum(stack)

if __name__=='__main__':
    line = input()
    ops = line.strip().split()
    print(ops)

    print(calPoints(ops))


#****************************************************************************************************************************************************************


#1. MIT first Algo peak finding 

def asd(arr):
  n = len(arr)
  if n == 1:
    return arr[0]
  if n == 2:
    return max(arr)
  if arr[n // 2] < arr[(n // 2) - 1]:
    return asd(arr[:n // 2])
  if arr[n // 2] < arr[(n // 2) + 1]:
    return asd(arr[n // 2:])
  return arr[n // 2]

asd([34,3,4,3,4,3])
#****************************************************************************************************************************************************************

# this is for Mat
def sdf(plane):
    n = len(plane)
    middle_row = plane[n // 2]
    middle_max = max(middle_row)
    i = middle_row.index(middle_max)
    if n == 1:
        return middle_max
    if n == 2:
        return max(plane[0][i], middle_max)
    if middle_max < plane[(n // 2) - 1][i]:
        return sdf(plane[n // 2:])
    if middle_max < plane[(n // 2) + 1][i]:
        return sdf(plane[:n // 2])
    return middle_max

sdf([[54,45,54],[98,7,878],[787,6,8]])  

#****************************************************************************************************************************************************************
    
def sol(x):
    c = 0
    while x!=0:
        c = c*10 + x%10
        x=x//10
    return c
#****************************************************************************************************************************************************************

l1 = ["eat","sleep","repeat"]
 
# printing the tuples in object directly
for ele in enumerate(l1):
    print (ele)

#****************************************************************************************************************************************************************

def qwe(rr,t):
    c = 0
    p = len(rr)
    for i in range(p):
        for j in range(p):
            if rr[i] == t:
                c=c+1
            elif rr[i] + rr[j] == t:
                c=c+1
    if c == 0:
        print("not found")
    else:
        print("found")
#****************************************************************************************************************************************************************

weeq = [-1,0,1,2,3,4,5,6,7,8,9,10]
print(weeq)
print(weeq[4:],"all after pos 4th")
print(weeq[:4],"all before pos 4th")
print(weeq[:-4],"all after pos -4th")
print(weeq[-4:],"all before pos -4th")

#****************************************************************************************************************************************************************

a = bool()
b = bool()
c = bool()
a = False
b = False
c = True
if c == a and b:
    print(c,"1")
if c == a or b:
    print(c,"2")
else :
    print(c,"3")
#****************************************************************************************************************************************************************

 # I made it my self!!          

def qwe(rr,t):
    c = 0
    p = len(rr)
    for i in range(p):
        for j in range(p):
            if rr[i] + rr[j] == t:
                r = i
                e = j
    return e,r

#****************************************************************************************************************************************************************
    
#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

# Now we'll write the main function which has all the gameplay functionality.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()

#****************************************************************************************************************************************************************

# BST.

class Node:
  """
  Node of the binary search tree.
  """

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None


def bst_insert(root, value):
  """
  Insert a value into a binary search tree.
  """
  if root.value == value:
    return
  if value < root.value:
    if root.left:
      bst_insert(root.left, value)
    else:
      root.left = Node(value)
      root.left.parent = root
  if root.right is None:
    root.right = Node(value)
    root.right.parent = root
  bst_insert(root.right, value)


def bst_insert_list(arr):
  """
  Convert a list into a binary search tree.
  """
  node = Node(arr[0])
  for i in range(1, len(arr)):
    bst_insert(node, arr[i])
  return node


def bst_search(root, value):
  """
  Search a binary search tree for a value.
  """
  if root.value == value:
    return True
  if root.value > value:
    return False if root.left is None \
        else bst_search(root.left, value)
  return False if root.right is None \
      else bst_search(root.right, value)


def bst_delete(node, value):
  """
  Delete a value from a binary search tree.
  """
  if value < node.value and node.left is not None:
    bst_delete(node.left, value)
  elif value > node.value and node.right is not None:
    bst_delete(node.right, value)
  elif value == node.value:
    if node.left is None \
            and node.right is None \
            and node.parent is not None:
        if node == node.parent.left:
          node.parent.left = None
        else:
          node.parent.right = None
    elif node.left is None and node.parent:
      if node == node.parent.left:
        node.parent.left = node.right
      else:
        node.parent.right = node.right
    elif node.right is None and node.parent:
      if node == node.parent.left:
        node.parent.left = node.left
      else:
        node.parent.right = node.left
    elif node.parent:
      tmp = node.left
      while tmp.right is not None:
        tmp = tmp.right
      node.value = tmp.value
      bst_delete(tmp, tmp.value)


def print_inorder(root):
  """
  Print the elements of a BST in sorted order.
  """
  if root.left is not None:
    print_inorder(root.left)
  print('value: %2d ' % root.value)
  if root.right is not None:
    print_inorder(root.right)


def bst_invert(node):
  """
  Invert a binary search tree.
  """
  if node == None:
    return None
  node.left = bst_invert(node.right)
  node.right = bst_invert(node.left)
  return node

a = ["34","32","34","5","5","35","3"]
eqr = str()
for w in range(len(a)):
    eqr = a[w]
    print(eqr)
#****************************************************************************************************************************************************************

# array to string???
# Strings operations 
# keywords
# DSA begain here
# leetcode
#****************************************************************************************************************************************************************


def bubble(qw):
    a = len(qw)
    for i in range(0,qw):
        for j in range(j+1, qw):
            if a[i]>a[j]:

#****************************************************************************************************************************************************************

# a = b * q + r
def qwee(a,bw):
    if a > bw :
        q=0
        r=0
        while True :
            q=a//bw
            r=a%bw
            a=bw
            bw=r
            return b



#****************************************************************************************************************************************************************

sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

#****************************************************************************************************************************************************************

s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello, 
world!
"""
print(s1, s2, s3, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)
#****************************************************************************************************************************************************************


s1 = 'hello ' * 3
print(s1) # hello hello hello 
s2 = 'world'
s1 += s2
print(s1) # hello hello hello world
print('ll' in s1) # True
print('good' in s1) # False
#****************************************************************************************************************************************************************

str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2]) # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5]) # c12
print(str2[2:]) # c123456
print(str2[2::2]) # c246
print(str2[::2]) # ac246
print(str2[::-1]) # 654321cba
print(str2[-3:-1]) # 45
#****************************************************************************************************************************************************************

a, b = 5, 10
print('{0} * {1} = {2}'.format(a, b, a * b))

#****************************************************************************************************************************************************************

str3 = ['  jackfrued@126.com ']
str3.strip()
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())
#****************************************************************************************************************************************************************


list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
# 乘号表示列表元素的重复
list2 = ['hello'] * 3
print(list2) # ['hello', 'hello', 'hello']
# 计算列表长度(元素个数)
print(len(list1)) # 5
# 下标(索引)运算
print(list1[0]) # 1
print(list1[4]) # 100
# print(list1[5])  # IndexError: list index out of range
print(list1[-1]) # 100
print(list1[-3]) # 5
list1[2] = 300
print(list1) # [1, 3, 300, 7, 100]
# 通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
# 通过for循环遍历列表元素
for elem in list1:
    print(elem)
# 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)

#****************************************************************************************************************************************************************

f = [x for x in range(1, 10)]
print(f)


for i in range(0,10):
    print(f[i])

f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
import sys
f = [x ** 2 for x in range(1, 1000)]
print(getsizeof(f)) 
print(f)

#****************************************************************************************************************************************************************

f = (x ** 2 for x in range(1, 1000))

for val in f:
    print(val)

#****************************************************************************************************************************************************************


t = ('骆昊', 38, True, '四川成都')
print(t)
# 获取元组中的元素
print(t[0])
print(t[3])

#****************************************************************************************************************************************************************


from time import sleep


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()

#****************************************************************************************************************************************************************

import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()

#****************************************************************************************************************************************************************

for i in range(0,10):
  print(i)

#****************************************************************************************************************************************************************


year = int(input ('Please enter year: '))

is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)


#****************************************************************************************************************************************************************

weeq = [-1,0,1,2,3,4,5,6,7,8,9,10]
i = len(weeq)
d = i//2
for c in range(d,i,2):
    print(weeq[c])
#or
print(weeq[d::2])

#****************************************************************************************************************************************************************

q= [i for i in range(10)]
print(q)# 0 to 9
    
q= [i for i in range(1,11)]
print(q)

#****************************************************************************************************************************************************************


def qwe(q):
    e = [i for i in range(len(q))]
    print(e)
#****************************************************************************************************************************************************************


def dsa():
    c = input()
    print(c)
    print(type(c))
#****************************************************************************************************************************************************************

def fre():
    a = input()
    c = 1
    for i in range(len(a)):
        if 'a' or 'e' or 'i' or 'o' or 'u' in a: 
            c = c + 1
    print(c) 
#****************************************************************************************************************************************************************

L = [54,45,54,6,7,5,7,543]

for i in range(1, len(L)):
    for j in range(0, i):
        if L[i - j] < L[i - j - 1]:
            L[i - j],  L[i - j - 1] = L[i - j - 1], L[i - j]
print(L)

#****************************************************************************************************************************************************************

"""
os
sys
math
random
data time
JSON
"""
def bs(d,t):
    l = 1
    h = len(d)
    while(l<=h):
        mid = l+h//2
        if t==d[0]:
            print("1","found on position")
            break
        elif t==d[mid]:
            print(mid+1,"found on position")
            break
        elif t<d[mid]:
            h = mid - 1 
        else:
            l = mid - 1

#****************************************************************************************************************************************************************

def ArrayChallenge(strArr):
    q = strArr[0]
    w = strArr[1].split(',')
    e1 = []
    e2 = []
    for i in range(len(w)):
        r = q.split(w[i])
        if len(r) == 2:
            k = r[0] + r[1]
            e1.append(k)
    for j in range(len(e1)):
        if w.count(e1[j]) != 0:
            e2.append(e1[j])
    l = []
    if e2 == []:
        l = 'not working'
    else:
        for i in range(len(e2)):
            for j in range(len(e2)):
                n = e2[i] + e2[j]
                if n == q:
                    l.append(e2[i])
                    l.append(e2[j])
                    l=','.join(l)
    return l

#****************************************************************************************************************************************************************
def ArrayChallenge(arr):
   n = len(arr)
   if n == 1:
     return arr[0]
   if n == 2:
     return min(arr)
   if arr[n // 2] > arr[(n // 2) - 1]:
     return ArrayChallenge(arr[:n // 2])
   if arr[n // 2] > arr[(n // 2) + 1]:
     return ArrayChallenge(arr[n // 2:])
   return arr[n // 2] 


#****************************************************************************************************************************************************************




asdfg = ["b a s e b a l l", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]

q = asdfg[0].split(' ')
w = asdfg[1].split(',')


#****************************************************************************************************************************************************************

# not for adds
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


my_url = 'https://www.speedtest.net/'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

qw = page_soup.find_all("div",{"class":"creative-container"})
print 


#****************************************************************************************************************************************************************

import requests, lxml, urllib.parse
from bs4 import BeautifulSoup
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 "
    }

params = {'q': 'сoffee buy'}

html = requests.get(f'https://www.google.com/search?q=',
                    headers=headers,
                    params=params).text

soup = BeautifulSoup(html, 'lxml')

for container in soup.findAll('div', class_='RnJeZd top pla-unit-title'):
  
    title = container.text

 
    startOfLink = 'https://www.googleadservices.com/pagead'

    endOfLink = container.find('a')['href']

    ad_link = urllib.parse.urljoin(startOfLink, endOfLink)

    
    print(f'{title}\n{ad_link}\n')


#****************************************************************************************************************************************************************



import requests, lxml, urllib.parse
from bs4 import BeautifulSoup
headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {'q': ''}

html = requests.get(f'https://www.speedtest.net',
                    headers=headers,
                    params=params).text

soup = BeautifulSoup(html, 'lxml')

for container in soup.findAll('div', class_='RnJeZd top pla-unit-title'):
  
    title = container.text

 
    startOfLink = 'https://www.googleadservices.com/pagead'

    endOfLink = container.find('a')['href']

    ad_link = urllib.parse.urljoin(startOfLink, endOfLink)

    
    print(f'{title}\n{ad_link}\n')


#****************************************************************************************************************************************************************


def intotal(a):
    o=[]
    d = len(a)
    for i in range(d):
        m = a[i]
        c = 0
        for j in range(d):
    
            if m==a[j]:
                c = c + 1
                if c > 1: 
                    break
        if c == 1:
            o.append(m)

    return o


    
intotal([2,2,3,54,7,3567,356,7,5637,56,6678,453,545,232,45,654,654])

#****************************************************************************************************************************************************************



d = 'qwerthgjgfds'
s = []
for a in d:
    print(a)

#****************************************************************************************************************************************************************
#1

ls=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
dict={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
ls2=[]
 
def func(no,res):
    for i in range(0,len(ls)):
        if no in ls:
            res=dict[no]
            rem=0
            break
        if ls[i]<no:
            quo=no//ls[i]
            rem=no%ls[i]
            res=res+dict[ls[i]]*quo
            break
    ls2.append(res)
    if rem==0:
        pass
    else:
        func(rem,"")
 
 
if __name__ == "__main__":
    func(26, "")
    print("".join(ls2))

#****************************************************************************************************************************************************************
l = [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]

def occ(e):
    a = []
    d = len(e)
    for i in range(d):
        flg = 0
        for j in range(d):
            if e[i] == e[j]:
                flg = flg + 1

            
#****************************************************************************************************************************************************************

import numpy as np
a = np.random.randint(0,9,(7000,7000))
print(a)
r = a
q=r*r
print(q)
a=q*q*q*q*r-q-q-q-q-q-q+r+r*q*q*q*q*q*q*q*q*q*q*q
print(a)
#****************************************************************************************************************************************************************

import numpy as n
a = [1,5,3]
b = [4,2]
c = a + b
c.sort()
e = n.median(c)
print(e)
#****************************************************************************************************************************************************************

import numpy as n
def arrayee(num1, num2):
    c = num1 + num2
    c.sort()
    e = n.median(c)
    print(e)
    
arrayee([1,3],[2])
#****************************************************************************************************************************************************************

import numpy as n
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        c = nums1 + nums2
        c.sort()
        e = n.median(c)
        return e

if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([3], [1, 2]))

#****************************************************************************************************************************************************************



def St(str1,str2):
    d = len(str1)
    b = len(str2)
    w = False
    m = 0
    if d == b:
        for e in str1:
            for s in str2:
                if e == s:
                    m = m +1
            if m == d:
                w = True
                break
            
    return str1,w 
#****************************************************************************************************************************************************************

def St(str1,str2):
    d = len(str1)
    b = len(str2)
    w = False
    m = 0
    if d == b:
        for e in str1:
            for s in str2:
                if e == s:
                    m = m +1
            if m == d:
                w = True
                break
            
    return w
  
print(St('ecro','roce'))
#****************************************************************************************************************************************************************

ar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
qq = enumerate(ar)
print(list(qq))

def due(q):
#****************************************************************************************************************************************************************


def create_letter_num_dict():
    letters = "abcdefghijklmnopqrstuvwxyz"
    nums = range(1, 27)
    letter_num_dict = {key: value for key, value in zip(letters, nums)}
    return letter_num_dict
    
    
    {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}


qw = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

def NumberEncoding(a_string):
  letter_num_encoder = qw
  encoded_string =''
  for char in a_string.lower():
    if char.isalpha():
      encoded_string += str(letter_num_encoder[char])
    else:
      encoded_string += char
  return encoded_string


NumberEncoding("hello 45")
#****************************************************************************************************************************************************************


def StockPicker(arr):
	cost = 0
	maxcost = 0
	
	mini = arr[0]
	for i in range(len(arr)):
		mini = min(mini, arr[i])
		cost = arr[i] - mini
		maxcost = max(maxcost, cost)
	return maxcost
	
print(StockPicker([10, 12, 4, 5, 9]))

#****************************************************************************************************************************************************************
a = [1,2,3,4]



def cer(a):
    c = a[1:]
    sand = a[0]
    c.sort(reverse=True)    
    w = len(c)

#****************************************************************************************************************************************************************




class Solution(object):
     def findMedianSortedArrays(self, nums1, nums2):

         p1 = p2 = 0
         ls1 = len(nums1)
         ls2 = len(nums2)
         all_nums = []
         median = 0.0
         while p1 < ls1 and p2 < ls2:
             if nums1[p1] < nums2[p2]:
                 all_nums.append(nums1[p1])
                 p1 += 1
             else:
                 all_nums.append(nums2[p2])
                 p2 += 1
         if p1 < ls1:
             while p1 < ls1:
                 all_nums.append(nums1[p1])
                 p1 += 1
         if p2 < ls2:
             while p2 < ls2:
                 all_nums.append(nums2[p2])
                 p2 += 1
         # print all_nums
         if (ls1 + ls2) % 2 == 1:
             median = all_nums[(ls1 + ls2) / 2]
         else:
             median = 1.0 * (all_nums[(ls1 + ls2) / 2] + all_nums[(ls1 + ls2) / 2 - 1]) / 2
         return median 



if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.findMedianSortedArrays([1, 1], [1, 2]))

#****************************************************************************************************************************************************************


def thermal(we):
    so = len(we)
    wq = sd
#****************************************************************************************************************************************************************


def rep(a):



q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
k = len(q)
qwe = ''
for i in range(k):
    qwe = qwe + q[i]

print(qwe)

q
e = str(q)
print(e)
str 
for qr in e:
    print(qr)


def rccc(a):
    for q in a:
        a = q.copy()
#****************************************************************************************************************************************************************

def era(a):
    ste = ''
    for i in a:
        flg = 0
        for w in a:
            print(w)
            
    

 era('324refdd')


a = ['ew','rf','ewr','ewrw','ewerdre','rf']
q = a.copy()
a.pop()
print(a)
q


    
def pww(x,n):
    c  = 1.0
    if n is float():


    for i in range(n):
        c = c * x
    print(c)

#****************************************************************************************************************************************************************

s1 = 80
S2 = 8490

a = 9

sandeepkroec@gmail.com


def dup(a):
    q = []
    s = len(a)
    for i in a:
        for j in a:
            if i == j:
                q.append(j)
    print(q)


#****************************************************************************************************************************************************************

from collections import Counter
a = []

def gen(rt):
    
    print("please enter users one by one")
    for i in range(rt+1):
        tw = input()
        a.append(tw)
    
    s = a[-1]
    if s == '':
        a.pop()
        exc()
    elif s.isdigit():
        s = int(s)
        v = s
        a.pop()        
        gen(v)
    else:
        theta()


def exc():
        tweet_names = a.copy()
        uniq_names = [pref_names.split()[0] for
            pref_names in tweet_names]
        times = Counter(uniq_names)
        repeat = times.values()
        for element in set(repeat):
            dupl = ([(key, value) for
                key, value in sorted(times.items()) if
                value == element])

            if len(dupl) > 1:
                for (key, value) in dupl:
                    print (key,'',value)
            max_value = max(times.values())
            temp_max_result = [(key, value) for
                    key, value in sorted(times.items()) if
                    value == max_value]

            if temp_max_result != dupl:
                for (key,value) in temp_max_result:
                    print (key,'',value)
    


def theta():

    w = int(input("please enter number of tweets\n"))
    rt = int(input("please enter the numbers of usernames\n")) 
    gen(rt)


    
theta()

#****************************************************************************************************************************************************************

import requests
# Please Enter the Value 
frontend_address = 'google.com'
m = []
n = []
flag = 0
def storing(red,sew):

    w = red.copy()
    m.append(w)
    e = sew.copy()
    n.append(e)
    return(m,n)

       
def req():
    r = requests.get("https://"+frontend_address)
    #print(r.status_code)
    #print(r.ok)
    if r.ok == False:
        flag = 1
    return 
                
def superfunc(q,t):
    
    req()
    if flag == 1:
        storing(q,t)
    else:
        return m,n


 
#****************************************************************************************************************************************************************


import numpy as np
import pandas as pd 
from keras.preprocessing.image import ImageDataGenerator, load_img
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random
import os

#1

ls=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
dict={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
ls2=[]
 
def func(no,res):
    for i in range(0,len(ls)):
        if no in ls:
            res=dict[no]
            rem=0
            break
        if ls[i]<no:
            quo=no//ls[i]
            rem=no%ls[i]
            res=res+dict[ls[i]]*quo
            break
    ls2.append(res)
    if rem==0:
        pass
    else:
        func(rem,"")
 
 
if __name__ == "__main__":
    func(26, "")
    print("".join(ls2))

#O(n)
#****************************************************************************************************************************************************************

def min(x, y):
	return x if(x < y) else y
	
def max(x, y):
	return x if(x > y) else y

def findLength(arr, n):
	
	max_len = 1
	for i in range(n - 1):
	
	

		mn = arr[i]
		mx = arr[i]

		for j in range(i + 1, n):
		

			mn = min(mn, arr[j])
			mx = max(mx, arr[j])


			if ((mx - mn) == j - i):
				max_len = max(max_len, mx - mn + 1)
		
	return max_len


arr = [1, 56, 58, 57, 90, 92, 94, 93, 91, 45]
n = len(arr)
print("Length of the longest contiguous subarray is ",findLength(arr, n))
									
#O(n)
#****************************************************************************************************************************************************************


def getOddOccurrence(arr, arr_size):
	
	for i in range(0,arr_size):
		count = 0
		for j in range(0, arr_size):
			if arr[i] == arr[j]:
				count+=1
			
		if (count % 2 != 0):
			return arr[i]
		
	return -1
	
	
arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2 ]
n = len(arr)
print(getOddOccurrence(arr, n))
#O(n^2)


#****************************************************************************************************************************************************************
def fabo(q):
    b = 1 
    a = 0
    for i in range(0,q-1):
        c = a + b
        print(c)
        a = b
        b = c

if __name__ == '__main__':
    fabo(999999)

#****************************************************************************************************************************************************************



def printSubStr(str, low, high):
	
	for i in range(low, high + 1):
		print(str[i], end = "")


def longestPalSubstr(str):
	
	n = len(str)

	maxLength = 1
	start = 0

	for i in range(n):
		for j in range(i, n):
			flag = 1
			
			for k in range(0, ((j - i) // 2) + 1):
				if (str[i + k] != str[j - k]):
					flag = 0

			if (flag != 0 and (j - i + 1) > maxLength):
				start = i
				maxLength = j - i + 1
				
	print("Longest palindrome subString is: ", end = "")
	printSubStr(str, start, start + maxLength - 1)

	return maxLength

if __name__ == '__main__':

	str = "fdfykguhijlhgfdsgdhgfjgkkjyfht"
	
	print("\nLength is: ", longestPalSubstr(str))
#O(n^3)
#****************************************************************************************************************************************************************

def printRLE(st):

	n = len(st)
	i = 0
	while i < n- 1:

		count = 1
		while (i < n - 1 and st[i] == st[i + 1]):
			count += 1
			i += 1
		i += 1

		print(st[i - 1] + str(count),end = "")

if __name__ == "__main__":

	st = 'wwwwaaadexxxxxxywww'
	printRLE(st)

#O(n^2)


#****************************************************************************************************************************************************************
def mergeSort(alist):
    
    print("Splitting: ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

    print(alist)

mergeSort([4,3,5,2,0,9,1,5,1])


#****************************************************************************************************************************************************************

def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
for value in simpleGeneratorFun(): 
    print(value)
#****************************************************************************************************************************************************************

def sum(a,b):
    try:
        return a + b
    except NameError:
        print("Name not defined")
    except TypeError:
        print("Error in varible type")
    else:
        print("there is another issue")

sum(23,"2")
#****************************************************************************************************************************************************************
hjk = 0
while True:
    hjk = hjk + 1
    flg = 0
    for c in range(1,11):
        if hjk%c== 0:
            flg = flg + c
            if flg == 55:
                print(hjk)
                
#****************************************************************************************************************************************************************
my own venture
