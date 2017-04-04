
class Stack:

     def __init__(self):
          self.items = []  
     def isEmpty(self):
          return self.items == []  
     def push(self, item):
          self.items.append(item)  
     def pop(self):
          return self.items.pop()  
     def peek(self):
          return self.items[len(self.items)-1]  
     def size(self):
          return len(self.items)


s = Stack()

str_input = "Isd(ff)(f (a)(d)d)";
n = 0;

for x in str_input:
     if (x == "("):
          s.push(x)
     elif (x == ")"):
          if (s.isEmpty()):
               break
          else:
               s.pop()
     n += 1

if (s.isEmpty() and n == len(str_input)):
     print(str_input, "is VALID")
else:
     print(str_input, "is NOT VALID")

