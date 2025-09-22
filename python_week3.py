# Function to calculate discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price


# Main program
try:
    # Prompt the user for input
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The final price after discount is: {final_price}")
    else:
        print(f"No discount applied. The original price is: {final_price}")

#Wrapped input in try/except → prevents ValueError crashes.
except ValueError:
    print("Invalid input! Please enter numbers only.")
