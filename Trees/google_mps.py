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
        for node in tree.keys():
            if tree[node].keys() == None:
                print(node)
                return Node(node)
            childs.append(self.parse(tree[node]))
        n = Node(tree)
        n.childs = childs
        return n    
        	
    def find(self,node,place):
        #print(node.Name)
        if not node.childs:
           return
        for node in node.childs:
            if place == node.Name:
               print("palce found")
               exit()
            self.find(node,place)
     
    def srch(self,place):
       self.root = self.parse(tree)
       self.find(self.root,place)
        
	
s = Search(tree)
s.srch("vij")
