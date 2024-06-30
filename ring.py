from group import Group
import operator
import itertools

# this extends Group but adds additional structure, namely the additive operation,
    # commutativity, and if it is unital

class Ring(Group):

    # the grp prefix applies to the operations and elements concerning the base grou
    # the ring prefix applied to the additional operations and elements required
        # to make the group into a ring

    def __init__(self, elements: list, grp_operation: operator, ring_operation: operator, 
                 grp_identity, ring_identity) -> None:
        super().__init__(self, elements, grp_operation, grp_identity)
        self.add_operation = ring_operation
        self.add_identity = ring_identity

    def is_commutative(self):
        return self.is_abelian(operation=self.grp_operation)

group = Group(elements=[1,2,3,4,1,2,3,1,-1,-2,-3,-4,0], grp_operation=operator.mul, grp_identity=1) 

# this should inherit grp_operation and grp_identity
ring = Ring(group, ring_operation=operator.add, ring_identity=0)

