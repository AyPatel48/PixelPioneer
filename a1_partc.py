# Copy over your a1_partc.py file here

#    Main Author(s): Archi Mukeshbhai Kakadiya
#    Main Reviewer(s): Ayush Patel, Mohdeep Singh

class Stack:

	"""
 	A stack (LIFO) data structure implementation with dynamic resizing.
    
    	Attributes:
    	- s_stack: A list representing the stack's elements
    	- s_capacity: The maximum number of elements the stack can currently hold
    	- s_size: The current number of elements in the stack
    	"""
	
	def __init__(self, cap=10):
		"""
        	Initializes the stack with a given capacity (default is 10), size, and an array to hold stack elements
        
        	Parameters:
        	- cap (int): Initial capacity of the stack
        	"""
		self.s_stack = [None] * cap
		self.s_capacity = cap
		self.s_size = 0

	def capacity(self):
		"""
        	Returns the current capacity of the stack
        	"""
		return self.s_capacity

	def push(self, data):
		"""
       		Stack is full ? double its capacity : Add an element to the top of the stack
        
        	Parameters:
        	- data: The element to be added to the stack
        	"""
		if self.s_size == self.s_capacity:
			n_capacity = self.s_capacity * 2
			n_stack = [None] * n_capacity
			for i in range(self.s_size):
				n_stack[i] = self.s_stack[i]
			self.s_stack = n_stack
			self.s_capacity = n_capacity
		self.s_stack[self.s_size] = data
		self.s_size += 1

	def pop(self):
		"""
        	Stack is empty ? raise an error : Remove and return the top element of the stack
        
        	Returns:
        	- The top element of the stack
        	"""
		if self.is_empty():
			raise IndexError('pop() used on empty stack')
		top_value = self.s_stack[self.s_size - 1]
		self.s_stack[self.s_size - 1] = None
		self.s_size -= 1
		return top_value

	def get_top(self):
		"""
        	Stack is empty ? return None : Return the top element of the stack without removing it
        
        	Returns:
        	- The top element or None if the stack is empty
        	"""
		if self.is_empty():
			return None
		return self.s_stack[self.s_size - 1]

	def is_empty(self):
		"""
        	Checks if the stack is empty
        
        	Returns:
        	- True if the stack is empty, False otherwise
        	"""
		return self.s_size == 0

	def __len__(self):
		"""
        	Returns the current size (number of elements) in the stack
        	"""
		return self.s_size


class Queue:
	"""
    	A queue (FIFO) data structure implementation with dynamic resizing
    
    	Attributes:
    	- q_queue: A list representing the queue's elements
    	- q_capacity: The maximum number of elements the queue can currently hold
    	- q_size: The current number of elements in the queue
    	- q_front: The index of the front element in the queue
    	"""

	def __init__(self, cap=10):
		"""
        	Initializes the queue with a given capacity (default is 10), size, front and queue array elements
        
        	Parameters:
        	- cap (int): Initial capacity of the queue
        	"""
		self.q_queue = [None] * cap
		self.q_capacity = cap
		self.q_size = 0
		self.q_front = 0

	def capacity(self):
		"""
        	Returns the current capacity of the queue
        	"""
		return self.q_capacity

	def enqueue(self, data):
		"""
        	Queue is full ? double its capacity : Add an element to the back of the queue
        
        	Parameters:
        	- data: The element to be added to the queue
        	"""
		if self.q_size == self.q_capacity:
			n_capacity = self.q_capacity * 2
			n_queue = [None] * n_capacity
			for i in range(self.q_size):
				n_queue[i] = self.q_queue[(self.q_front + i) % self.q_capacity]
			self.q_queue = n_queue
			self.q_front = 0
			self.q_capacity = n_capacity
		back_value = (self.q_front + self.q_size) % self.q_capacity
		self.q_queue[back_value] = data
		self.q_size += 1

	def dequeue(self):
		"""
        	Queue is empty ? raise an error : Remove and return the front element of the Queue
        
        	Returns:
        	- The front element of the queue
        	"""
		if self.is_empty():
			raise IndexError('dequeue() used on empty queue')
		front_value = self.q_queue[self.q_front]
		self.q_queue[self.q_front] = None
		self.q_front = (self.q_front + 1) % self.q_capacity
		self.q_size -= 1
		return front_value

	def get_front(self):
		"""
        	Queue is empty ? return None : Return the front element of the queue without removing it
        
        	Returns:
        	- The front element or None if the queue is empty
        	"""
		if self.is_empty():
			return None
		return self.q_queue[self.q_front]

	def is_empty(self):
		"""
        	Checks if the queue is empty
        
        	Returns:
        	- True if the queue is empty, False otherwise
        	"""
		return self.q_size == 0

	def __len__(self):
		"""
        	Returns the current size (number of elements) in the queue
	        """
		return self.q_size



class Deque:
	"""
    	A deque (double-ended queue) data structure implementation with dynamic resizing
    	Allows insertion and removal of elements from both ends
    
    	Attributes:
    	- d_deque: A list representing the deque's elements
    	- d_capacity: The maximum number of elements the deque can currently hold
    	- d_size: The current number of elements in the deque
    	- d_front: The index of the front element in the deque
    	"""

	def __init__(self, cap=10):
		"""
        	Initializes the deque with a given capacity (default is 10), size, front index, and an array to hold deque elements
        
        	Parameters:
        	- cap (int): Initial capacity of the deque
        	"""
		self.d_deque = [None] * cap
		self.d_front = 0
		self.d_size = 0
		self.d_capacity = cap

	def capacity(self):
		"""
        	Returns the current capacity of the deque
        	"""
		return self.d_capacity

	def push_front(self, data):
		"""
        	Deque is full ? double its capacity : Add an element to the front of the deque
        
        	Parameters:
        	- data: The element to be added to the front
        	"""
		if self.d_size == self.d_capacity:
			n_capacity = (2 * self.d_capacity)
			n_deque = [None] * n_capacity
			for i in range(self.d_size):
				n_deque[i] = self.d_deque[(self.d_front + i) % self.d_capacity]
			self.d_deque = n_deque
			self.d_front = 0
			self.d_capacity = n_capacity
		self.d_front = (self.d_front - 1) % self.d_capacity
		self.d_deque[self.d_front] = data
		self.d_size += 1

	def push_back(self, data):
		"""
        	Deque is full ? double its capacity : Add an element to the back of the deque
        
        	Parameters:
        	- data: The element to be added to the back
        	"""
		if self.d_size == self.d_capacity:
			n_capacity = (2 * self.d_capacity)
			n_deque = [None] * n_capacity
			for i in range(self.d_size):
				n_deque[i] = self.d_deque[(self.d_front + i) % self.d_capacity]
			self.d_deque = n_deque
			self.d_front = 0
			self.d_capacity = n_capacity
		back_value = (self.d_front + self.d_size) % self.d_capacity
		self.d_deque[back_value] = data
		self.d_size += 1

	def pop_front(self):
		"""
        	Deque is empty ? raise an error : Remove and return the front element of the Deque
        
        	Returns:
        	- The front element of the deque
        	"""
		if self.is_empty():
			raise IndexError('pop_front() used on empty deque')
		data = self.d_deque[self.d_front]
		self.d_deque[self.d_front] = None  
		self.d_front = (self.d_front + 1) % self.d_capacity
		self.d_size -= 1
		return data

	def pop_back(self):
		"""
        	Deque is empty ? raise an error : Remove and return the back element of the Deque
        
        	Returns:
        	- The back element of the deque
        	"""
		if self.is_empty():
			raise IndexError('pop_back() used on empty deque')
		back_value = (self.d_front + self.d_size - 1) % self.d_capacity
		data = self.d_deque[back_value]
		self.d_deque[back_value] = None
		self.d_size -= 1
		return data

	def get_front(self):
		"""
        	Deque is empty ? return None : Return the front element of the Deque without removing it
        
        	Returns:
        	- The front element or None if the deque is empty
        	"""
		if self.is_empty():
			return None
		return self.d_deque[self.d_front]

	def get_back(self):
		"""
        	Deque is empty ? return None : Return the back element of the Deque without removing it
        
        	Returns:
        	- The back element or None if the deque is empty.
        	"""
		if self.is_empty():
			return None
		back_value = (self.d_front + self.d_size - 1) % self.d_capacity
		return self.d_deque[back_value]

	def is_empty(self):
		"""
        	Checks if the deque is empty
        
        	Returns:
        	- True if the deque is empty, False otherwise
        	"""
		return self.d_size == 0

	def __len__(self):
		"""
        	Returns the current size (number of elements) in the deque
        	"""
		return self.d_size

	def __getitem__(self, k):
		"""
    		Index out of range ? raise an error: Returns the element at the given index 'k' in the deque
    
    		Parameters:
    		- k (int): The index of the element to be accessed

      		Returns:
    		- The element at index 'k'
      		"""
		if k < 0 or k >= self.d_size:
			raise IndexError('Index out of range')
		return self.d_deque[(self.d_front + k) % self.d_capacity]