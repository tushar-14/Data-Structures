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

    def reverse_iterative(self):      #reverse the list using iterative method
        prevnode=None
        curnode=self.head

        while(curnode!=None):
            nextnode = curnode.next
            curnode.next=prevnode
            prevnode=curnode 
            curnode=nextnode
        
        self.head=prevnode    

l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")   
l_list.reverse_iterative()
l_list.printlist()