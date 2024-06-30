# attemping a group object
# there are obviously some qualifying assumptions that I will need to verify

import operator
import itertools

class Group:

    def __init__(self, elements: list, grp_operation: operator, grp_identity) -> None:
        self.elements = elements
        self.grp_operation = grp_operation
        self.grp_identity = grp_identity

        # checking closure under group operation
        # for i, j in self.elements:
        #         if self.operation(i, j) not in self.elements:
        #             raise Exception('This does not define a group')
                
            # try using a comprehension for this shit, overload cartesian product mayhaps?
        # if [for i,j in self.elements if self.operation(i,j)]:
        #     return
        
    def get_identity(self):
        return self.identity
    
    def order(self):
        return len(self.elements)

    # there must be a more elegant way to do this and use this
        # list comprehension is the way fur sure
    def get_inverse(self, item):
        for a in self.elements:
            if self.operation(a, item) != self.identity:
                continue
            elif self.operation(a, item) == self.identity:
                return a

    # there is DEFINITELY a better way to do this but this is the idea thus far
    def is_abelian(self, operation: operator) -> bool:
        for i in range(self.order):
            for j in range(self.order):
                if i != j:
                    if operation(i,j) == operation(j,i):
                        continue
                    else:
                        return False
        return True


grp = Group([0, 1, -1], grp_operation=operator.add, grp_identity=0)