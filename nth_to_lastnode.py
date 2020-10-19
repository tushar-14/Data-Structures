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

    def nth_from_last(self,n):
        total_len=self.length_list_iterative()
        curnode=self.head
        
        if(n>total_len):
            return print("invalid position")
        
        while(curnode and total_len!=n):
            curnode=curnode.next
            total_len-=1
        
        return print(curnode.data)  


l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")   

l_list.nth_from_last(1)