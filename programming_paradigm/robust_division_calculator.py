#A calculator that robustly handlles errors like zero division andnon-numeric inputs

def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        return f"The result of the division is {result}"
        
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."
        
    except ValueError:
        return "Error: Please enter numeric values only."