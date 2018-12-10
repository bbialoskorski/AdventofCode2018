import sys


def visit_tree(index, tree):

    num_children = tree[index]
    metadata_count = tree[index + 1]

    metadata_sum = 0
    child_index = index + 2
    length = 2 + metadata_count

    for child in range(num_children):

       child_sum, child_length = visit_tree(child_index, tree)

       metadata_sum += child_sum
       length += child_length
       child_index += child_length

    for i in range(metadata_count):

        metadata_sum += tree[child_index + i]

    return metadata_sum, length
        

def sol():

    license = sys.stdin.readline()

    license = license[:len(license) - 1].split(' ')

    tree = list()

    for number in license:

        tree.append(int(number))

    metadata_sum, length = visit_tree(0, tree)

    print(metadata_sum)

sol()
