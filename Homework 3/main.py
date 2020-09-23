''' # 1 '''
class Queue:

  def __init__(self):
      self.queue = list()

  #Add
  def insert(self,data):
     self.queue.insert(0,data)          

  #Remove
  def remove(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ('empty')

  #print
  def printQueue(self):
      return self.queue

myQueue = Queue()
print(myQueue.insert(1)) 
print(myQueue.insert(2)) 
print(myQueue.insert(3)) 
print(myQueue.insert(4)) 
print(myQueue.insert(5))     
print(myQueue.remove())  
print(myQueue.remove())  
print(myQueue.remove())  
print(myQueue.remove())  
print(myQueue.remove())  
print(myQueue.remove()) 

''' #2'''

def is_a_palindrome(s): 
    return s == s[::-1]

s = input('Enter text to check')
answer = is_a_palindrome(s) 

if answer == True:
    print('True')
else:
    print('False')

'''#3'''

myStack = []

myStack.append('a')
myStack.append('b')
myStack.append('c')

def remove():
    if len(myStack) > 0:
        mystack.pop
    return ('empty')

myStack
['a', 'b', 'c']

myStack.remove('a')
myStack.remove('b')
myStack.remove('c')
myStack.remove('c')


'''#4'''

Class Queue(object):
    def __init__(self):
        self.qlist = []

    def insert(self, element):
        self.qlist.append(element)

    def remove(self):
        if self.qlist == []:
            print 'Empty'
        else:
            element = self.qlist[0]
            self.qlist.remove(element)
            return element
            
