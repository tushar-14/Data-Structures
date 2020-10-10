class Node:                        #creating of a node 
    def __init__(self , data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def printlist(self):           #printing the created linked list
        curnode = self.head
        while(curnode):
            print(curnode.data)
            curnode=curnode.next

    def append(self,data):          #insertion at end
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            return 
        
        lastnode = self.head
       
        while(lastnode.next):
            lastnode=lastnode.next
        lastnode.next=newnode    

    def prepend(self,data):                  #insert at begning
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
            

    def insertafter(self,data,position):      #insert after the given position
        newnode= Node(data)
        p=1
        prevnode=self.head
        while(p < position-1):
            prevnode=prevnode.next  
            p=p+1  

        newnode.next=prevnode.next
        prevnode.next=newnode   
    

l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")
l_list.prepend("F")
l_list.insertafter("E",2)
l_list.printlist()