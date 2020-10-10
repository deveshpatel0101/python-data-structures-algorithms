from .stack import Stack


def start():
    stack = Stack()
    while True:
        try:
            print("\n1. PUSH")
            print("2. POP")
            print("3. PEEK")
            print("4. DISPLAY")
            print("5. isEmpty")
            print("6. EXIT")
            choice = int(input("\nEnter your choice: "))

            if choice == 1:
                item = int(input("Enter the value you want to push: "))
                stack.push(item)
            elif choice == 2:
                item = stack.pop()
                print("Value popped:", item[0])
            elif choice == 3:
                item = stack.peek()
                print("Value peeked:", item)
            elif choice == 4:
                print(stack.display())
            elif choice == 5:
                print(stack.is_empty())
            elif choice == 6:
                break
            else:
                print("Command not recognized.")
        except Exception as error:
            print(error)


if __name__ == '__main__':
    start()
