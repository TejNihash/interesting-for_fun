
class node:
    ''' the node representation'''
    def __init__(self,id):
        self.id = id 
        self.connections = [] 

    def connect(self,node,weight):
        self.connections.append((node,weight))  # we are linking the other node here, will it be a pointer though??
        

def connect_nodes(nodeA,nodeB,weight):
    '''easy way to connect two nodes'''

    nodeA.connect(nodeB,weight)
    nodeB.connect(nodeA,weight)

    print("nodes successfully connected!")
    return True


def print_connections(node):
    for nodule,weight in node.connections:
        print('with node:' ,nodule.id,'at weight:',weight)


marked = []
dist_dict = {}
def get_distances(node,dist_so_far=0):
    '''this function should take in a node and get me distances to all other nodes'''
    #print('marked',marked,'node on',node.id,'dist so far',dist_so_far)
    print(dict(sorted(dist_dict.items())))

    
        
    if node.id in dist_dict.keys():
        if dist_dict[node.id]>dist_so_far:
            dist_dict[node.id]=dist_so_far
        else:
            dist_so_far = dist_dict[node.id]

            
    else:
        dist_dict[node.id] = dist_so_far

    if node.id in marked:
        return
    else:

        marked.append(node.id)
    
    for connected_node,weight in node.connections:
        get_distances(connected_node,dist_so_far+weight)





node0 = node(0)
node1 = node(1)
node2 = node(2)
node3 = node(3)
node4 = node(4)
node5 = node(5)
node6 = node(6)
node7 = node(7)
node8 = node(8)

#build the network
connect_nodes(node0,node1,4)
connect_nodes(node0,node7,8)
connect_nodes(node1,node7,11)
connect_nodes(node1,node2,8)
connect_nodes(node2,node8,2)
connect_nodes(node2,node3,7)
connect_nodes(node2,node5,4)
connect_nodes(node3,node4,9)
connect_nodes(node3,node5,14)
connect_nodes(node4,node5,10)
connect_nodes(node5,node6,2)
connect_nodes(node6,node8,6)
connect_nodes(node6,node7,1)
connect_nodes(node7,node8,7)




print_connections(node1)

get_distances(node0)

print(dict(sorted(dist_dict.items())))
print(marked)

'''node0 = '0'
node1 = '1'
node2 = '2'
node3 = '3'
node4 = '4'
node5 = '5'
node6 = '6'
node7 = '7'
node8 = '8'

#now we build the network
connect_nodes(Nodes_dict,node0,node1,4)
connect_nodes(Nodes_dict,node0,node7,8)
connect_nodes(Nodes_dict,node1,node7,11)
connect_nodes(Nodes_dict,node1,node2,8)
connect_nodes(Nodes_dict,node2,node8,2)
connect_nodes(Nodes_dict,node2,node3,7)
connect_nodes(Nodes_dict,node2,node5,4)
connect_nodes(Nodes_dict,node3,node4,9)
connect_nodes(Nodes_dict,node3,node5,14)
connect_nodes(Nodes_dict,node4,node5,10)
connect_nodes(Nodes_dict,node5,node6,2)
connect_nodes(Nodes_dict,node6,node8,6)
connect_nodes(Nodes_dict,node6,node7,1)
connect_nodes(Nodes_dict,node7,node8,7)'''