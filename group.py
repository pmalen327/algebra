import operator
import itertools
import numpy as np

class Group:

    '''
    Definining a basic group class with the basic properties of a group.

    Construction:
        elements - a list of group elements, assumed to have no duplicates

        grp_operation - the operation to endow the group with specified by
            an operator object

        grp_identity - the identity element with respect to grp_operation specified
            by an operator object
    '''

    def __init__(self, elements: list, grp_operation: operator, grp_identity) -> None:
        self.elements = elements
        self.grp_operation = grp_operation
        self.grp_identity = grp_identity
        self.order = len(elements)

        # This is checking closure under grp_operation
        for i in range(self.order):
            for j in range(self.order):
                if i != j:
                    if grp_operation(i,j) in self.elements:
                        continue
                    else:
                        raise Exception('The set is not closed under the given group operation.')
                        
    def get_identity(self):
        return self.grp_identity

    # there must be a more elegant way to do this and use this
        # list comprehension is the way fur sure
    def get_inverse(self, item):
        for a in self.elements:
            if self.operation(a, item) != self.grp_identity:
                continue
            else:
                return a

    # Checks commutativity of each element to determine if the group is abelian or not
    # there is DEFINITELY a better way to do this but this is the idea thus far
    def is_abelian(self, operation: operator) -> bool:
        for i in range(self.order):
            for j in range(self.order):
                if i != j:
                    if operation(i,j) != operation(j,i):
                        return False
        return True

    # Given a group element, return it's orbit
    def orbit(self, element):
        pass

    # Given a group element, return it's stabilizer
    def stabilizier(self, element):
        pass

    # Return the center of the group. This is the set of elements that commute
        # with every other element. If is_abelian == True, then this just returns
        # elements.
    def center(self):
        if self.is_abelian():
            return self.elements
        pass

    def isomorphic_to(self, other):
        pass
# grp = Group([0, 1, -1], grp_operation=operator.add, grp_identity=0)