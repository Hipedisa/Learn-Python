def main():
    x = float(input("x = "))
    print(f"x squared is: {square(x)}")

def square(n: float = "2"):
    return pow(n, 2)

main()