# Tree

def tree(label, branches=[]):
    """The constructor of tree."""
    for branch in branches:
        assert is_tree(branch)  # each branch must be tree.
    return [label] + list(branches)


def label(tree):
    """Return the label of a tree."""
    return tree[0]


def branches(tree):
    """Return the branches of a tree."""
    return tree[1:]


def is_tree(t):
    """Judge whether it's a valid tree."""
    if not isinstance(t, list) or len(t) < 1:
        return False
    for branch in branches(t):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Judge whether it's a leaf."""
    return not branches(tree)


def count_leaves(t):
    """Return the number of leaves of a tree."""
    if is_leaf(t):
        return 1
    else:
        branches_count = [count_leaves(b) for b in branches(t)]
        return sum(branches_count)


def leaves_label(t):
    """Return a list containing the leaf labels of a tree."""
    if is_leaf(t):
        return list(label(t))
    else:
        return sum([leaves_label(b) for b in branches(t)], [])


def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        bs = [increment_leaves(b) for b in branches(t)]
        return tree(label(t), bs)


def increment_label(t):
    """Return a tree like t but with all labels incremented."""
    bs = [increment_label(b) for b in branches(t)]
    return tree(label(t) + 1, bs)


def print_tree(t):
    """Print the struct of a tree."""
    print(label(t))
    for b in branches(t):
        print_tree(b)


def print_tree_adv(t, indent=0):
    """Print the struct of a tree with indentation."""
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree_adv(b, indent + 1)


def print_sums(t, sum_so_far=0):
    """Print the sums from root node to each leaf."""
    sum_so_far += label(t)
    if is_leaf(t):
        print(sum_so_far)
    else:
        for b in branches(t):
            print_sums(b, sum_so_far)


def sum_tree(t):
    """Return the sum of all labels of a tree."""
    if is_leaf(t):
        return label(t)
    else:
        sum_b = sum([sum_tree(b) for b in branches(t)])
        return label(t) + sum_b


def print_all_path(t):
    """Print all paths from root to leaf."""
    for path in all_path(t):
        print(path)


def all_path(t):
    """Return all paths from root to leaf."""
    if is_leaf(t):
        yield [label(t)]
    else:
        for b in branches(t):
            for path in all_path(b):
                yield [label(b)] + path

