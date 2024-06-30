# an attempt at making a category class lol

class Category:

    def __init__(self, objects: dict, morphisms: dict, **kwargs) -> None:
        self.objects = objects
        self.morphisms = morphisms
        self.name = kwargs.get('name', None) # this doesn't work yet
    
    # the "type" of category, Set, Hom, End, etc. 
    def get_name(self) -> str:
        return self.name
    
    def get_objects(self) -> dict:
        return self.objects
    
    def get_morphisms(self) -> dict:
        return self.morphisms
    

class Functor:
    
    def __init__(self, mapping_objects: dict, mapping_morphisms: dict) -> None:
        self.mapping_objects = mapping_objects
        self.mapping_morphisms = mapping_morphisms

    def map_object(self, object):
        return self.mapping_objects.get(object, None)

    def map_morphism(self, morphism):
        return self.mapping_morphisms.get(morphism, None)
    
    def get_preimage(self, image):
        if image in self.mapping_objects.values():
            return {i for i in self.mapping_objects if 
                    self.mapping_objects[i] == image}
        else:
            return f'the preimage of {image} is empty'


# testing
cat1 = Category(objects={1 ,2 ,4}, morphisms={'f': ('A', 'B', 'C')}, name='Hom')
cat2 = Category(objects={20, 30, 40}, morphisms={'g':('U', 'V', 'W')})
functor = Functor(mapping_objects={'A':30, 'B':40, 'C':20},
            mapping_morphisms={'f':'g'})


print(cat1.get_name)
print(functor.map_object('A'))
print(functor.map_morphism('f'))
print(functor.get_preimage(12))



