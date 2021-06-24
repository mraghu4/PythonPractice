tree = {'india': {
           'ap':{
                'vij':{},
		'gun':{}
            },
           'up':{
	    },
           'tn':{
               'chennai':{}
            },
           'ka':{
               'banglore':{}
            }
	}
}


class Node:
    def __init__(self,Name):
        self.Name = Name
        self.childs = None
	

class Search:
    root = None
    tree = {}
	
    def __init__(self,tree):
        self.tree = tree
        
    def parse(self,tree):
        childs = []
        print(tree)
        print(tree.values())
        if not tree.values():
           return Node(tree)
        for node in tree.keys():
            childs.append(self.parse(tree[node]))
        n = Node(node)
        n.childs = childs
        #print(node)
        return n    
        	
    def find(self,node,place):
        if not node.childs:
           return
        for child in node.childs:
            if place == child.Name:
               print("palce found")
               exit()
            self.find(node,place)
     
    def print_tree(self,node):
        print("Node:{}".format(node.Name))
        if not node.childs:
           return
        for child in node.childs:
            print("Node:{}".format(node.Name))
            self.print_tree(child)
       


    def srch(self,place):
       self.root = self.parse(tree)
       #self.print_tree(self.root)
       #self.find(self.root,place)
        
	
s = Search(tree)
if s.srch("vij") == None:
   print("Not found")
