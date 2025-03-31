'''WE gonna implement a priority queue based shortest distance finder'''

def connect_nodes(nodes_dict, node1, node2, dist):
    '''It connects them in a dictionary of connected nodes'''
    if node1 not in nodes_dict:
        nodes_dict[node1] = {}  # Create an empty dictionary for node1
    if node2 not in nodes_dict:
        nodes_dict[node2] = {}  # Create an empty dictionary for node2
    
    nodes_dict[node1][node2] = dist
    nodes_dict[node2][node1] = dist  # Assuming an undirected graph



Priority_queue = {}
min_path = None

def get_shortest_path(pres_node,end_node ): 
    '''take in the nodes and give out a shortest path.'''
    
    #get minimum path so far

    if Priority_queue:
        min_path = min(Priority_queue,key=Priority_queue.get)
    else:
        Priority_queue[pres_node] = 0 
        min_path=pres_node

    print(Priority_queue)
    for child_node,dist in Nodes_dict[pres_node].items():
        if child_node not in min_path:
            Priority_queue[min_path+child_node] = Priority_queue[min_path]+dist 
        if child_node ==end_node:
            return (min_path+child_node, Priority_queue[min_path]+dist)
    del Priority_queue[min_path]

    print(Priority_queue)
    
    #let's get the min path
    min_path = min(Priority_queue,key=Priority_queue.get)

    print('min_path',min_path)

    jump_node = min_path[-1]

    print('jump_node',jump_node)

    path, dist = get_shortest_path(jump_node,end_node)

    print( 'path:',path,'dist',dist)




        

    



    #look at children not in the min path and add them to queue 


    #remove the minimum path.
    #get the minimum path once again

    #get the jump node


    #use that jump node as start node. and repeat


    


    
        

    

     




'''let's make connections'''
#initialize the nodes first

Nodes_dict = {}

node0 = '0'
node1 = '1'
node2 = '2'
node3 = '3'
node4 = '4'
node5 = '5'
node6 = '6'


#now we build the network
connect_nodes(Nodes_dict,node0,node1,1)
connect_nodes(Nodes_dict,node0,node3,12)
connect_nodes(Nodes_dict,node1,node2,5)
connect_nodes(Nodes_dict,node2,node3,3)
connect_nodes(Nodes_dict,node2,node5,4)
connect_nodes(Nodes_dict,node3,node4,9)
connect_nodes(Nodes_dict,node5,node4,1)
connect_nodes(Nodes_dict,node4,node6,3)

#yeah, that was stupid. I could've just used it in. but, practice is a good thing yeah? also, that way, I don't have to define the
#nodes dict at the beginning.

print(Nodes_dict)

get_shortest_path(node0,node6)
