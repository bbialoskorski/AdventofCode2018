import sys


def visit_tree(index, tree):

    num_children = tree[index]
    metadata_count = tree[index + 1]

    node_value = 0
    children_values = list()

    child_index = index + 2
    length = 2 + metadata_count

    for child in range(num_children):

        child_value, child_length = visit_tree(child_index, tree)
        
        children_values.append(child_value)
        
        length += child_length
        child_index += child_length

    for i in range(metadata_count):

        if num_children == 0:

            node_value += tree[child_index + i]

        elif tree[child_index + i] <= len(children_values) and tree[child_index + i] > 0:
            
            node_value += children_values[tree[child_index + i] - 1]

    return node_value, length
        

def sol():

    license = sys.stdin.readline()

    license = license[:len(license) - 1].split(' ')

    tree = list()

    for number in license:

        tree.append(int(number))

    root_value, length = visit_tree(0, tree)

    print(root_value)

sol()
