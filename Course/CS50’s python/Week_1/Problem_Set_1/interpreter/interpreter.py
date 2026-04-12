def main():

    expression = input("Expression: ")

    x, y, z = expression.split(" ")

    x, z = float(x), float(z)

    match y:
        case '+':
            print(x + z)
        case '-':
            print(x - z)
        case '/':
            print(x / z)
        case '*':
            print(x * z)
    
main()