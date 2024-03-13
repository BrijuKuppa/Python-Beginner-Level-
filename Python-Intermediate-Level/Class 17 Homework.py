#Practice Program-1: Type Casting
'''a=1.34556
print(str(a))'''
#Practice Program-2: More Type Casting
'''s="python"
print(f"Variable 's' to a list: {list(s)}")
print(f"Variable 's' to a tuple: {tuple(s)}")
print(f"Variable 's' to a set: {set(s)}")'''
#Practice Program-3: Union, Intersection, and Difference with Sets
'''SET1={1, 2, 3, 4, 5, 6}
SET2={3, 4, 5, 6, 7, 8, 9}
print(f"Union with 'SET1' and 'SET2': {SET1.union(SET2)}")
print(f"Intersection with 'SET1' and 'SET2': {SET1.intersection(SET2)}")
print(f"Difference with 'SET1' and 'SET2': {SET1.difference(SET2)}")
print(f"Difference with 'SET2' and 'SET1': {SET2.difference(SET1)}")'''
#Practice Program-4: Adding to Sets
'''SET1={1, 2, 3, 4, 5}
SET1.add("red")
print(SET1)'''
#Practice Program-5: Flower Class
'''class Flower:
    def __init__(self,petals,stem,leaf,expression):
        self.petals=petals
        self.stem=stem
        self.leaf=leaf
        self.expression=expression
    def emotion(self):
        print(f"Flower is {self.expression}")

Flower_ob1=Flower(6,1,2,"happy")
Flower_ob2=Flower(6,1,2,"sad")
Flower_ob1.emotion()
Flower_ob2.emotion()'''