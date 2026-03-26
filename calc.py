def main():
    print("Let's implement division. Type two numbers for x and y")
    
    x = int(input("x > "))
    y = int(input("y > "))
    
    print("%d / %d = %0.3f" % (x, y, divide(x, y)))
    print("%d + %d = %d" % (x, y, add(x, y)))
    
    
def add(a, b):
    return a + b
    
    

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print ("Error: cannot divide by zero.")
        

if __name__ == "__main__":
    main()
