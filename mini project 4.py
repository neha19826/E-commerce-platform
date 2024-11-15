class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart.")

    def remove_from_cart(self, product_id):
        for item in self.items:
            if item.product_id == product_id:
                self.items.remove(item)
                print(f"Removed {item.name} from cart.")
                return
        print("Product not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Items in your cart:")
            total = 0
            for item in self.items:
                print(f"- {item}")
                total += item.price
            print(f"Total: ${total:.2f}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. Cannot checkout.")
        else:
            total = sum(item.price for item in self.items)
            print("Checking out...")
            print(f"Total amount: ${total:.2f}")
            print("Order has been placed successfully.")
            self.items.clear()  # Empty the cart after checkout


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = Cart()

    def login(self, username, password):
        if self.username == username and self.password == password:
            print(f"Welcome back, {self.username}!")
        else:
            print("Invalid username or password.")


class Store:
    def __init__(self):
        self.products = [
            Product(1, "Laptop", 1000.00),
            Product(2, "Smartphone", 500.00),
            Product(3, "Headphones", 150.00),
            Product(4, "Tablet", 300.00),
            Product(5, "Smartwatch", 200.00),
        ]

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product.product_id}. {product}")

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None


def main():
    # Create a store
    store = Store()

    # Simulate user registration
    print("Welcome to the E-Commerce Platform!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Create a user (for simplicity, no real authentication logic)
    user = User(username, password)
    print(f"User {username} registered successfully.")

    # User login
    login_username = input("Enter your username to login: ")
    login_password = input("Enter your password: ")
    user.login(login_username, login_password)

    # Main shopping flow
    while True:
        print("\nSelect an option:")
        print("1. View Products")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            store.display_products()
        elif choice == '2':
            product_id = int(input("Enter the product ID to add to cart: "))
            product = store.get_product_by_id(product_id)
            if product:
                user.cart.add_to_cart(product)
            else:
                print("Product not found.")
        elif choice == '3':
            product_id = int(input("Enter the product ID to remove from cart: "))
            user.cart.remove_from_cart(product_id)
        elif choice == '4':
            user.cart.view_cart()
        elif choice == '5':
            user.cart.checkout()
        elif choice == '6':
            print("Exiting the platform. Thank you for shopping!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
