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

    def removeduplicate(self):
        prevnode=None
        curnode=self.head
        
        if(not curnode):
            return

        dup_list=list()  
         
        while(curnode):
            
            if(curnode.data in dup_list):
                prevnode.next=curnode.next
                curnode=None    
            else:
                dup_list.append(curnode.data)
                prevnode=curnode
            
            curnode=prevnode.next
           

l_list=linkedlist()
l_list.append("1")
l_list.append("2")
l_list.append("1")
l_list.append("4")
l_list.append("4")
l_list.append("5")
l_list.append("4")

l_list.removeduplicate()
l_list.printlist()

