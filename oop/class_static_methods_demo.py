"""A script to demonstrate and solidify my understanding of 
class methods and static methods"""

class Calculator:
   
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b 
    
    @classmethod    
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b