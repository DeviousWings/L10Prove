import csv
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# Index for reader(aka request.csv)
NAME_INDEX = 0
QUANTITY_INDEX = 1

# Index for products_dicrionary(aka products.csv)
PRODUCT_CODE_INDEX = 0
PRODUCT_NAME_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    try:
        products_dicrionary = read_dict("products.csv", 0)

        print("Requested Items")
        discount = 0.1
        with open("request.csv", 'rt') as request_list:
            reader = csv.reader(request_list)
            next(reader)
        
            numbers_item = 0
            subtotal = 0.0
            sales_tax = .06
            total = 0.0

            for row_list in reader:
                key_value = row_list[0]
                product_quantity = int(row_list[1])
                row_list = products_dicrionary[key_value]
                description = row_list[1]
                price = float(row_list[2])

                numbers_item += product_quantity
                
                subtotal += (price*product_quantity)

                total_tax = sales_tax * subtotal
                total = total_tax + subtotal
                
                print(f"{description}: {product_quantity} @ ${price}")
                
            
            print()
            print(f"Number of Items: {numbers_item}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax: ${total_tax:.2f}")
            print(f"Total: ${total:.2f}")
            
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print(f"{current_date_and_time:%a %b %I:%M %p}")
        
        
 
            
    except FileNotFoundError as not_found_err:
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        print(f"The item {products_dicrionary} doesn't exist.")
        print("Run the program again and enter the" \
        " name of an existing file.")
        
    except PermissionError as perm_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(perm_err).__name__, perm_err, sep=": ")
        print(f"You don't have permission to read {products_dicrionary}.")
        print("Run the program again and enter the name" \
                " of a file that you are allowed to read.")
        
    except KeyError as keyerr:
        
        print()
        print(type(keyerr).__name__, keyerr, sep=": ")
        print(f"Error: unknown product ID in the request.csv file '{key_value}'")
        

        

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





if __name__ == '__main__':
    main()