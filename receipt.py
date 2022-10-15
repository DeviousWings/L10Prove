import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()




def main():
    products_dicrionary = read_dict("products.csv", 0)
    # 1. Print the store name at the top of the receipt.
    print("Inkom Emporium")
    print()

    print("Requested Items")    
    with open("request.csv", 'rt') as request_list:
        reader = csv.reader(request_list)
        next(reader)
    
    
        for row_list in reader:
            key_value = row_list[0]
            product_quantity = row_list[1]
            row_list = products_dicrionary[key_value]
            description = row_list[1]
            price = row_list[2]
            
            
            
            # 2. Print the list of ordered items.
            print(f"{description}: {int(product_quantity)} @ ${price}")
    

        print()
        quantity = total(products_dicrionary)
        # 3. Sum and print the number of ordered items.
        # Number of Items: 12
        print(f"Number of items: {quantity}")
    

    print()
    # 7. Print a thank you message.
    # Use an f-string to print the current
    # day of the week and the current time.
    # Wed Nov  4 05:10:30 2020
    print("Thank you for shopping at the Inkom Emporium.")
    # 8. Get the current date and time from your computer's operating system and print the current date and time.
    print(f"{current_date_and_time:%a %b %I:%M %p}")
    
    # 9. Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
    
"""    Program should read
    Inkom Emporium
    
    wheat bread: 2 @ 2.55
    1 cup yogurt: 4 @ 0.75
    32 oz granola: 1 @ 3.21
    twix candy bar: 2 @ 0.85
    1 cup yogurt: 3 @ 0.75

    Number of Items: 12
    Subtotal: 15.26
    Sales Tax: 0.92
    Total: 16.18"""

    # Thank you for shopping at the Inkom Emporium.
    # Wed Nov  4 05:10:30 2020

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    return_dictionary = {}
    
    with open(filename, 'rt') as products_dicrionary:
        reader = csv.reader(products_dicrionary)
        #This skips to the row '1'  and not look at the row '0'
        next(reader)
        
        for current_row in reader:
            return_dictionary[current_row[0]] = current_row
            
    return return_dictionary
#Indexes for inner lists in the products list
NAME_INDEX = 0
quantity_INDEX = 1

# Indexes fo rinner lists in the request lists
ID_INDEX = 0
REQUEST_INDEX = 1

def total(products_dicrionary):
    # 3. Sum and print the number of ordered items.
    # Number of Items: 12
    sum = 0
    # Get the quantity for the symbol from the dictionary.
    for inner_list in products_dicrionary:
        name = inner_list[ID_INDEX]
        quanitiy = inner_list[REQUEST_INDEX]
    
    # Add the quantity together
        total_items = products_dicrionary[name][quantity_INDEX]
        sum = sum(total_items)
        
        
    return sum

        
    # 4. Sum and print the subtotal due.
    # Subtotal: 15.26
    # 5. Compute and print the sales tax amount. Use 6% as the sales tax rate.
    # Sales Tax: 0.92
    # 6. Compute and print the total amount due.
    # Total: 16.18
    
    
if __name__ == '__main__':
    main()