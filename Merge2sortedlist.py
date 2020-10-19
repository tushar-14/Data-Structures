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

    def mergesorted(self,list2):
        p=self.head
        q=list2.head
        s=None
 
        if not p:                        #if list1 is null, return list2
            return q
        if not q:                        #if list2 is null, return list1
            return p

        if(p.data < q.data):             #setting the new head
            s=p
            p=s.next
        else:
            s=q
            q=s.next
        
        newhead=s                        #new head of the list is stored
        
        while p and q: 
            if p.data <= q.data:         #modifying the list
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next     
        
        if not p:                        #if reached end of list 1
            s.next=q
        if not q:                        #if reached end of list 2
            s.next=p    
  
        return newhead                   #return the new head
        
l_list1=linkedlist()
l_list2=linkedlist()

l_list1.append("1")
l_list1.append("5")
l_list1.append("7")
l_list1.append("9")   
l_list1.append("10") 

l_list2.append("2")
l_list2.append("3")
l_list2.append("4")
l_list2.append("6")   
l_list2.append("8") 

#l_list1.printlist() 
#l_list2.printlist()

l_list1.mergesorted(l_list2)
l_list1.printlist()