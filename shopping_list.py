
# PLP Python Week 7 - Part B: Shopping List Manager

shopping_list = []

while True:
    print("\n===== SHOPPING LIST MANAGER =====")
    print("Choose: add / remove / show / done")

    choice = input("Enter your choice: ").strip().lower()

    if choice == "add":
        item = input("Enter the item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(f"'{item}' has been added.")
        else:
            print("Item cannot be empty.")

    elif choice == "remove":
        item = input("Enter the item to remove: ").strip()

        # Check whether the item exists before removing it
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("\nYour shopping list:")

            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Invalid choice. Enter add, remove, show, or done.")
