class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self,l):
        self.head=Node(l[0])
        prev=self.head
        for i in range(1,len(l)):
            new_node=Node(l[i])
            prev.next=new_node
            prev=prev.next
    def __repr__(self):
        current=self.head
        s=""
        while(current.next!=None):
            s=s+f"{current.data} is pointing to {current.next.data}\n"
            current=current.next
        s=s+f"{current.data} is pointing to None \n"
        return (s)
list_1=LinkedList([1,2,3,4])
print(list_1)