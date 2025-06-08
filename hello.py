def main():
    first, last = input("Enter Your Full Name: ").strip().title().split(" ")
    hello(first)

def hello(to="Anonymous"):
    print(f"Hello {to}")

main()