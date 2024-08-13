# Available products and their prices
products = {
    "apple":1.20,
    "banana":2.34,
    "orange":12.45,
    "bread":23.78,
    "milk":90.23
}

# set to store items in the cart
cart = set()

def display_products():
    """Display available products"""
    print("\n--Available Products ---")
    for Product,price in products.items():
        print(f"{Product.title()} - ${price:.2f}")
        
def add_to_cart():
    """Display available products"""
    display_products()
    item = input("Enter the product name to add to your cart :").lower()
    if item in products:
        cart.add(item)
        print(f"{item.title()} has been added tom your cart.")
    else:
        print("Product not found. Please select from the available products.")


def remove_from_cart():
    """Removes an item from the cart."""
    if not cart:
        print("your Cart is empty")
        return
    view_cart()
    item = input("Enter thr product name to remove from your cart :").lower()
    if item in cart:
        cart.remove(item)
        print(f"{item.title()} has been removed from your cart.")
    else:
        print("Product not found in your cart.")
        
def view_cart():
    """Display items in the cart and calculates the total price."""
    if not cart:
        print("Your Cart is empty.")
        return
    print("\n---Your Cart ---")
    total  = 0
    for item in cart:
        price = products[item]
        total += price
        print(f"{item.title()} - ${price:.2f}")
    print(f"Total pric: ${total:.2f}")
    
def checkout():
    """Calculate the total price and checks out."""
    view_cart()
    if cart:
        print("Thank you for shopping with us")
        cart.clear()
        
def main_menu():
    """Display the main menu and processes user input."""
    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice :")
        
        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("GoodBye")
            break
        else:
            print("Invalid choice. please try again.")

if __name__ == "__main__":
    main_menu()        