class Node:
    def __init__(self,val,children=None,op=None):
        self.value=val
        if children is not None:
            self.children=children
        else:
            self.children=[]
        self.op=op
    def __add__ (self,a):
        if isinstance(a,Node):
            return Node(a.value+self.value,[self,a],"add")
        else:
            self.op_args=a
            return Node(self.value+a,[self],"add")
    def __sub__(self,a):
        if isinstance(a,Node):
            return Node(self.value-a.value,[self,a],"subtract")
        else:
            self.op_args=a
            return Node(self.value-a,[self],"subtract")
    def __mul__(self,a):
        if isinstance(a,Node):
            return Node(a.value*self.value,[self,a],"multiply")
        else:
            self.op_args=a
            return Node(self.value*a,[self],"multiply")
            self.op_args=
    def __truediv__(self,a):
        if isinstance(a,Node):
            return Node(self.value/a.value,[self,a],"division")
        else:
            self.op_args=a
            return Node(self.value/a,[self],"division")
    def __pow__(self,a):
        if isinstance(a,Node):
            return Node(self.value**a.value,[self,a],"exponential")
        else:
            self.op_args=a
            return Node(self.value**a,[self],"exponential")
            
a