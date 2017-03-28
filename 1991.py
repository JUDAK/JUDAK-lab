import sys

class tree:
	def __init__(self, data, left_child = None, right_child = None):
		self.data = data
		self.left_child = left_child
		self.right_child = right_child
	def search_node(node, data):
		if node.data == data:
			return node
		if node.left_child != None:
			temp = tree.search_node(node.left_child, data)
			if temp != None:
				return temp
		if node.right_child != None:
			temp = tree.search_node(node.right_child, data)
			if temp != None:
				return temp	
		return None

def preorder(node):
	sys.stdout.write(node.data)
	if node.left_child != None:
		preorder(node.left_child)
	if node.right_child != None:
		preorder(node.right_child)

def inorder(node):
	if node.left_child != None:
		inorder(node.left_child)
	sys.stdout.write(node.data)
	if node.right_child != None:
		inorder(node.right_child)

def postorder(node):
	if node.left_child != None:
		postorder(node.left_child)
	if node.right_child != None:
		postorder(node.right_child)
	sys.stdout.write(node.data)

num = input()
root = tree(None)
for i in range(num):
	temp = raw_input()
	target = tree.search_node(root, temp[0]) 
	if target == None:
		if (temp[2] != '.') and (temp[4] != '.'): 
			root = tree(temp[0], tree(temp[2]), tree(temp[4]))
		elif (temp[2] != '.'):
			root = tree(temp[0], tree(temp[2]))
		elif (temp[4] != '.'):
			root = tree(temp[0], None, tree(temp[4]))
		else:
			root = tree(temp[0])
	else:
		if (temp[2] != '.') and (temp[4] != '.'): 
			target.left_child = tree(temp[2])
			target.right_child = tree(temp[4])		
		elif (temp[2] != '.'):
			target.left_child = tree(temp[2])
		elif (temp[4] != '.'):
			target.right_child = tree(temp[4])	
		
preorder(root)
print ' '
inorder(root)
print ' '
postorder(root)
print ' '

