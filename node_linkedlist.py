class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None 
        
class linkedlist:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        if self.tail != None:
            self.tail.next = new_node
        self.tail = new_node
    
    def delete(self,index):
        pre = None 
        node = self.head
        i = 0
        
        while node != None and i < index :
            pre = node
            node = node.next
            i = i + 1
            
        if pre == None:
            self.head = node.next
        else:
            pre.next = node.next
            
    def show(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next 
    

if __name__=="__main__":
    
    qlist = linkedlist()

    def push():
    
       w = int(input("Enter values\n"))
       qlist.add(w)
       main()
    
    def pop():
    
        q = int(input("Enter values\n"))
        qlist.delete(q)
        main()    
        
    def display():
    
        print("your entries are down here")
        qlist.show()
        main()
    
    def main():
    
        print("\nPress the value to perform those functions in down there--\n")
        print("1 for insert")
        print("2 for remove")
        print("3 for display")
        print("press q & Enter\n")
        n = input()
        while True  :
            
            if n == '1':
                push()
            elif n == '2':
                pop()
            elif n == '3':
                display()
            elif n == 'q':
                print("Hope your expireance was good!!")
                break
            else :
                print("sorry does'nt work")
                main()
                

    main()

