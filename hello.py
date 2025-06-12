def main():
    first, last = input("enter your full name nigga: ").strip().title().split(" ")
    hello(first)

def hello(to):
    print(f"hello, {to}!")

main()