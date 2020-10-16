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

    def rotate(self,key):           #  rotate the list from the given key
        p=self.head
        q=p
        count=1

        if(key==None):
            return

        while(q.next!=None):        # traversing q to the end and p pointing to the key
            if(count==key):
                p=q
            count+=1    
            q=q.next

        if(p==self.head):
            return print("out of index")

        q.next=self.head
        self.head=p.next
        p.next=None

l_list=linkedlist()
l_list.append("1")
l_list.append("2")
l_list.append("3")
l_list.append("4")
l_list.append("5")
l_list.append("6")

l_list.rotate(5)
l_list.printlist()





