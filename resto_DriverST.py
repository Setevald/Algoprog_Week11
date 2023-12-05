from resto_ClassST import restaurant 

def create_item_list():
    item_list = []
    num_items = int(input("How many items will you order today?"))

    while num_items < 1:
        print("Number of items must be at least 1.")
        num_items = int(input("How many items will you order today?"))

    for _ in range(num_items):
        food_name = input("Enter the name of the item: ")
        pounds = float(input("Enter the amount of the item in pounds: "))

        while pounds <= 0:
            print("Amount of pounds must be greater than 0.")
            pounds = float(input("Enter the amount of the item in pounds: "))

        order = restaurant(food_name, pounds)
        item_list.append(order)
    return item_list


def display_list_content(item_list):
    for item in item_list:
        print(item)


def calculate_total_cost(item_list):
    total_cost = sum(item.getPrice_ST() for item in item_list)
    return total_cost


def main():
    Items = create_item_list()
    display_list_content(Items)

    total_cost = calculate_total_cost(Items)
    print(f"Total cost of all items: ${total_cost:.2f}")


if __name__ == "__main__":
    main()