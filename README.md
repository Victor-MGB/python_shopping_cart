Project: Shopping Cart System
Objective:
Create a shopping cart system using Python where users can:

Add items to their cart
Remove items from the cart
Calculate the total price of the items in the cart
Use sets to manage available products and ensure no duplicates in the cart.
Components of the Shopping Cart System
Products: A dictionary will store available products with their names as keys and prices as values.
Cart: A set will store the names of the products added to the user's cart to avoid duplicates.
Functions:
Display Products: Show the available products to the user.
Add to Cart: Add a selected product to the cart.
Remove from Cart: Remove a selected product from the cart.
View Cart: Display the contents of the cart and the total price.
Checkout: Calculate the total cost of items in the cart.
Main Menu: Provide options for the user to interact with the cart.



Explanation of the Code
Products Dictionary: Contains the items available for purchase with their corresponding prices.
Cart Set: Stores the items added to the cart. Using a set ensures that each item appears only once in the cart, avoiding duplicates.
Functions:
display_products(): Displays the available products to the user.
add_to_cart(): Prompts the user to enter a product name to add to their cart. If the product is available, it's added to the cart set.
remove_from_cart(): Prompts the user to remove an item from their cart. If the item is in the cart, it's removed.
view_cart(): Displays all items in the cart and calculates the total price.
checkout(): Displays the final cart contents and clears the cart after checkout.
main_menu(): The main interface that provides options for the user to interact with the shopping cart.
Key Concepts and Techniques
Sets: Used for the cart to ensure no duplicate items are added.
Dictionaries: Used to store product names and their prices, allowing easy access and look-up.
Basic I/O: Using input() to interact with the user and control the flow of the program.
Control Flow: Using loops and conditionals to navigate through the shopping cart system.