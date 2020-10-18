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

    def occurance_itterative(self,key):
        curnode=self.head
        values=0

        if(not curnode):
            return print("empty list")
       
        while(curnode):
            if(curnode.data==key):
                values+=1
            curnode=curnode.next
        
        return values

    def occurance_recursive(self,node,key):
        if(not node):
            return 0
        if(node.data==key):
            return 1 + self.occurance_recursive(node.next,key)
        else:
            return self.occurance_recursive(node.next,key)

l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")

print(l_list.occurance_recursive(l_list.head,"D"))