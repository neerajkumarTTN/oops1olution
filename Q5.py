


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

    def is_cyclic(self):
        s=set()
        current=self.head
        while(current!=None):
            if (current in s):
                print("It is cyclic")
                break
            else:
                s.add(current)
                current=current.next
        else:
            print("not cyclic")
    def cyclic_llist(self):
        current=self.head
        while(current.next!=None):
            current=current.next
        current.next=self.head.next
list_1=LinkedList([1,2,3,4])
list_2=LinkedList([5,6,7,8,9])
print(list_1)
print(list_2)
list_1.cyclic_llist()
list_1.is_cyclic()
list_2.is_cyclic()