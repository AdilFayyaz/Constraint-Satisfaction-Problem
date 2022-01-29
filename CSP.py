"""
Naive backtracking search without any heuristics or inference.
"""

VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
domain = ["Monday", "Tuesday", "Wednesday"]
CONSTRAINTS = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "E"),
    ("C", "F"),
    ("D", "E"),
    ("E", "F"),
    ("E", "G"),
    ("F", "G")
]


def backtrack(assignment):
    """Runs backtracking search to find an assignment."""
    # Return if length of assignment is = domain size
    if len(assignment) == len(VARIABLES):
        return assignment
    # select a variable not yet assigned in the dictionary
    var = select_unassigned_variable(assignment)
    # for every domain value
    for val in domain:
        # check for consistency. If consistent, update assignment dict
        if consistent(assignment, val, var):
            assignment[var] = val
            # recursive call
            result = backtrack(assignment)
            # if result not failure, return result
            if result != None:
                 return result
        # pop from the assignment dict if backtracking was required
        assignment.pop(var, val)



def select_unassigned_variable(assignment):
    """Chooses a variable not yet assigned, in order."""
    # loop over all the variables, if they do not exist in assignment return var
    for var in VARIABLES:
        if var not in assignment.keys():
            return var


def consistent(assignment, val, var):
    """Checks to see if an assignment is consistent."""
    # make a copy of assignment
    assign2 = assignment.copy()
    assign2[var] = val
    # check against all the constraints
    for constraint in CONSTRAINTS:
        # get a list of keys in assign
        keys_list = assign2.keys()
        # for every key in assignment
        for key in assign2:
            # check if key is equal to a constraint and the value
            # on both of them must not be equal, if equal return false
            if key == constraint[0]:
                if constraint[1] in keys_list:
                    if assign2[key] == assign2[constraint[1]]:
                        return False
            if key == constraint[1]:
                if constraint[0] in keys_list:
                    if assign2[key] == assign2[constraint[0]]:
                        return False
    return True

def main():
    solution = backtrack(dict())
    print("Solution is:")
    print(solution)

# Tell python to run main method
if __name__ == "__main__": main()