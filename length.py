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

    def length_list_iterative(self):             #iterative method
        curnode=self.head
        count=0
        
        while(curnode):
            count+=1
            curnode=curnode.next
        return count

    def length_list_recursive(self,headnode):         #recursive method
        if headnode is None:
            return 0

        return 1 + self.length_list_recursive(headnode.next)       

l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")   
l_list.printlist()   
print(l_list.length_list_iterative())      
print(l_list.length_list_recursive(l_list.head))  