class Tree:
# Initialize an empty output list
# Initialize an list of nodes to visit and add the root node to it
# While there are nodes in the list of nodes to visit
#   Remove the first node from the list of nodes to visit
#   Add its value to the output list
#   Add its children (if any) to the BEGINNING of the list of nodes to visit
# Return the output list
  def __init__(self, root = None):
    self.root = root


  def get_element_by_id(self, id):
    ids = []
    nodes_to_visit = [self.root]
    
    while len(nodes_to_visit) > 0:
      node = nodes_to_visit.pop(0)
      ids.append(node['id'])
      nodes_to_visit = node['children'] + nodes_to_visit
      if node['id'] == id:
        return node
