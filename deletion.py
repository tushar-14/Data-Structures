class Node:                        #creating of a node 
    def __init__(self , data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):          #insertion 
        newnode = Node(data)

        if self.head == None:
            self.head = newnode
            return 
        
        lastnode = self.head
       
        while(lastnode.next):
            lastnode=lastnode.next
        lastnode.next=newnode 


    def printlist(self):           #printing the created linked list
        curnode = self.head
        while(curnode):
            print(curnode.data)
            curnode=curnode.next

    def deletenode(self,key):
        curnode=self.head

        if curnode and curnode.data == key:         #if node to be deleted is head
            self.head=curnode.next
            curnode=None
            return
        
        prevnode=None
        while(curnode and curnode.data != key):    
            prevnode=curnode
            curnode=curnode.next
        if(curnode is None):                                 #if the node to be deleted is not present
            print("Element ({}) not found".format(key))
        else:                                        
            prevnode.next=curnode.next                      #deleting the required node
            curnode.next=None   
            print("Element ({}) succesfully deleted".format(key))     

l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")   
l_list.printlist()    
l_list.deletenode("C") 
l_list.deletenode("d")    