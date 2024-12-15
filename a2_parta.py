#    Main Author(s): Archi Mukeshbhai Kakadiya
#    Main Reviewer(s): Mohdeep Singh, Ayush Patel

class HashTable:

	"""
    	A hash table implementation using open addressing for collision resolution.
    
    	Attributes:
    	- h_capacity (int): The maximum number of elements the hash table can currently hold.
    	- h_table (list): An array representing the hash table's buckets, storing key-value pairs as tuples.
    	- h_size (int): The current number of key-value pairs in the hash table.
    	"""

	def __init__(self, cap=32):
		"""
	        Initializes the hash table with a given capacity (default is 32), size, and an array to hold elements.
	        
	        Parameters:
	        - cap (int): Initial capacity of the hash table.
	        """
		self.h_capacity = cap
		self.h_table = [None] * self.h_capacity
		self.h_size = 0

	def insert(self,key, value):
		"""
	        Inserts a key-value pair into the hash table. 
			key already exists ? insertion fails
	        load factor exceeds 0.7 ? Automatically resizes the table
	        
	        Parameters:
	        - key: The key to insert.
	        - value: The value associated with the key.
	        
	        Returns:
	        - bool: the insertion is successful ? True
			the key already exists or the table is full ? False
	        """
		index = self._hash(key)
		o_index = index

		while self.h_table[index] is not None:
			if self.h_table[index][0] == key:
				return False
			index = self._probe(index)
			if index == o_index:
				return False
		
		self.h_table[index] = (key, value)
		self.h_size += 1

		if self.h_size / self.h_capacity > 0.7:
			self._resize()
		return True

	def modify(self, key, value):
		"""
	        Modifies the value associated with an existing key in the hash table.
	        
	        Parameters:
	        - key: The key to modify.
	        - value: The new value to associate with the key.
	        
	        Returns:
	        - bool: the key is found and modified ? True : False
	        """
		index = self._hash(key)
		o_index = index

		while self.h_table[index]:
			if self.h_table[index][0] == key:
				self.h_table[index] = (key, value)
				return True
			index = self._probe(index)
			if index == o_index:
				return False
		return False

	def remove(self, key):
		"""
	        Removes a key-value pair from the hash table. 
		Rehashes subsequent elements to maintain table integrity.
	        
	        Parameters:
	        - key: The key to remove.
	        
	        Returns:
	        - bool: the key is found and removed ? True : False
	        """
		index = self._hash(key)
		o_index = index

		while self.h_table[index]:
			if self.h_table[index][0] == key:
				self.h_table[index] = None
				self.h_size -= 1 

				n_index = (index + 1) % self.h_capacity
				while self.h_table[n_index]:
					r_key, r_value = self.h_table[n_index]
					self.h_table[n_index] = None
					self.h_size -= 1
					self.insert(r_key, r_value)
					n_index = (n_index + 1) % self.h_capacity
				return True

			index = self._probe(index)
			if index == o_index:
				return False
		return False

	def search(self, key):
		"""
	        Searches for the value associated with a given key in the hash table.
	        
	        Parameters:
	        - key: The key to search for.
	        
	        Returns:
	        - The value associated with the key if found, or None otherwise.
	        """
		index = self._hash(key)
		o_index = index

		while self.h_table[index]:
			if self.h_table[index][0] == key:
				return self.h_table[index][1]
			index = self._probe(index)
			if index == o_index:
				return None
		return None

	def capacity(self):
		"""
	        Retrieves the current capacity of the hash table.
	        
	        Returns:
	        - int: The current capacity of the hash table.
	        """
		return self.h_capacity

	def __len__(self):
		"""
	        Retrieves the current number of key-value pairs in the hash table.
	        
	        Returns:
	        - int: The number of elements in the hash table.
	        """
		return self.h_size
	
	def _hash(self, key):
		"""
	        Hashes a key to produce an index within the table's capacity.
	        
	        Parameters:
	        - key: The key to hash.
	        
	        Returns:
	        - int: The index for the key.
	        """
		return hash(key) % self.h_capacity
	
	def _probe(self, index):
		"""
	        Performs linear probing to find the next index in case of a collision.
	        
	        Parameters:
	        - index (int): The current index.
	        
	        Returns:
	        - int: The next index to check.
	        """
		return (index + 1) % self.h_capacity

	def _resize(self):
		"""
	        Resizes the hash table to twice its current capacity and rehashes all existing elements.
	        """
		n_capacity = self.h_capacity * 2
		n_table = [None] * n_capacity

		for item in self.h_table:
			if item:
				key, value = item
				index = hash(key) % n_capacity
				while n_table[index]:
					index = (index + 1) % n_capacity
				n_table[index] = (key, value)
		
		self.h_table = n_table
		self.h_capacity = n_capacity
