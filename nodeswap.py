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

    def nodeswap(self,data1,data2):
        if(data1==data2):                      #return if both nodes are same
            return
        
        curnode1=self.head
        prevnode1=None

        while(curnode1 and curnode1.data!=data1):    #setting the values for node1
            prevnode1=curnode1
            curnode1=curnode1.next

        curnode2=self.head
        prevnode2=None

        while(curnode2 and curnode2.data!=data2):      #setting the values for node1
            prevnode2=curnode2
            curnode2=curnode2.next   

        if( not curnode1 or not curnode2):           # return if nodes are not in the list
            return     
        
        if prevnode1:                                 #checking if the node1 is not a head node and swap
            prevnode1.next=curnode2
        else:
            self.head=curnode2    
        
        if prevnode2:                                  #checking if the node2 is not a head node and swap
            prevnode2.next=curnode1
        else:
            self.head=curnode1   
        
        curnode1.next,curnode2.next=curnode2.next,curnode1.next      #final swap

l_list=linkedlist()
l_list.append("A")
l_list.append("B")
l_list.append("C")
l_list.append("D")
l_list.nodeswap("C","A")
l_list.printlist()