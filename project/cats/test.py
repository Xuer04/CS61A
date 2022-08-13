from cats import shifty_shifts


def pawssible_patches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""
    if start == goal:
        return 0
    elif start == "":
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(goal)
        # END

    elif goal == "" or limit < 0:
        # BEGIN
        "*** YOUR CODE HERE ***"
        return len(start)
        # END

    else:
        add_diff = shifty_shifts(start, goal[1:], limit - 1)
        remove_diff = shifty_shifts(start[1:], goal, limit - 1)
        substitute_diff = shifty_shifts(start[1:], goal[1:], limit - 1)
        # BEGIN
        "*** YOUR CODE HERE ***"
        print(f"add_diff: {add_diff}")
        print(f"remove_diff: {remove_diff}")
        print(f"substitute_diff : {substitute_diff }")
        return min(add_diff, remove_diff, substitute_diff)
        # END

print(pawssible_patches("ward", "wary", 10))
