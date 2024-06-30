# attemping a group object

import operator
import itertools

class Group:

    def __init__(self, elements: list, grp_operation: operator, grp_identity) -> None:
        self.elements = elements
        self.operation = grp_operation
        self.identity = grp_identity

        # checking closure under group operation
        # for i, j in self.elements:
        #         if self.operation(i, j) not in self.elements:
        #             raise Exception('This does not define a group')
                
            # try using a comprehension for this shit, overload cartesian product mayhaps?
        # if [for i,j in self.elements if self.operation(i,j)]:
        #     return
        

    def get_identity(self):
        return self.identity
    
    # there must be a more elegant way to do this and use this
        # list comprehension is the way fur sure
    def get_inverse(self, item):
        for a in self.elements:
            if self.operation(a, item) != self.identity:
                continue
            elif self.operation(a, item) == self.identity:
                return a

    def is_abelian(self) -> bool:
        pass

grp = Group([0, 1, -1], operation=operator.add, identity=0)