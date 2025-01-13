#Function to perform basic arithmetic operations

def perform_operation(num1, num2, operation = ('add', 'subtract', 'multiply', 'divide') ):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                print('Invalid')
        
perform_operation(num1=None, num2=None)           
            