class BikeProduct():
    # class attrubute (this can be accessed by class as well as instance)
    discount =0.08

    def __init__(self,colour,rate_per_item: int,no_of_item = 0) -> None:
        # assert:
        assert rate_per_item>0,f"{rate_per_item} is negative"
        assert no_of_item>0

        # Instance Attributes
        self.colour = colour
        self.no_of_item=no_of_item
        self.rate_per_item=rate_per_item
    #  For intance method, there is no need to create parameters except self, with that all the isntnce attributes can be accessed
    def calcluate_price(self) -> float:
        return self.no_of_item * self.rate_per_item
    
    def process_discount(self):
        return self.calcluate_price()*self.discount
    
    @classmethod
    def change_discount(cls,new_discount):
         cls.discount = new_discount
         return cls.discount
    
    @staticmethod
    def do_nothing():
        print(f"Access Class Attribute -{BikeProduct.discount} ")

# /*Accessibility: Static methods can be called both by using the class name and by using an instance of the class.
# No Access to Instance or Class Context: Static methods do not have access to the instance (self) or class (cls) context. They only have access to the parameters passed to them.

  
bike1 = BikeProduct("Green",10,10)
# bike1.colour = "Green"
# bike1.no_of_item = 3
# bike1.rate_per_item =10
bike1.discount = 0.05
bike1.do_nothing()
BikeProduct.do_nothing()
print(f"{bike1.colour} bike costs {bike1.calcluate_price()} and discount is {bike1.process_discount()}")

bike2 = BikeProduct("Blue",5,10)
# bike2.colour = "Blue"
# bike2.no_of_item = 5
# bike2.rate_per_item =10
print(f"{bike2.colour} bike costs {bike2.calcluate_price()}and discount is {bike2.process_discount()}")

# You can do the above way but the same attributes is created every time manually (that is extra three lines of code) and will be challenginging to maintain
# so the best way is to create a constructir using __init__ which can initialize all the instance variable when the object is created

"""
Types of Variables:
Global Variable: Defined outside all functions and classes and accessible from any part of the code.
Local Variable: Defined inside a function or block and only accessible within that function or block.
Class Variable (Class Attribute): Defined within a class but outside any instance methods. Shared among all instances of the class.
Instance Variable (Instance Attribute): Defined within instance methods and unique to each instance of the class.
"""

print(f"{BikeProduct.change_discount(11)}")

