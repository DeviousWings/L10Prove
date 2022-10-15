import csv
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

def main():
    products_dicrionary = read_dict("products.csv", 0)

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
            
            
            print(f"{description}: {product_quantity} @ ${price}")
    
    print(f"Number of Items: {sum(map(int, product_quantity.values()))}")
    
    
    print()
    # 7. Print a thank you message.
    # Use an f-string to print the current
    # day of the week and the current time.
    # Wed Nov  4 05:10:30 2020
    print("Thank you for shopping at the Inkom Emporium.")
    # 8. Get the current date and time from your computer's operating system and print the current date and time.
    print(f"{current_date_and_time:%a %b %I:%M %p}")
    

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