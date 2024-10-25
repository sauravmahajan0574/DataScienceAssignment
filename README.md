# DataScienceAssignment

CRUD Operations on Sales Dataset
This project demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations on a sales dataset stored in a CSV file. The project uses Python and the Pandas library to load, manipulate, and save data back to the CSV file.

Project Structure
bash
Copy code
.
├── sales_data.csv       # Sample CSV dataset with sales records
├── crud_operations.py   # Main Python script implementing CRUD operations
└── README.md            # Project documentation
Prerequisites
Python: Version 3.6 or higher.

Pandas: This library is used for data manipulation. You can install it via pip if not already installed:

bash
Copy code
pip install pandas
Dataset Structure (sales_data.csv)
The CSV file sales_data.csv should contain sales records with columns:

SaleID: Unique identifier for each sale (e.g., 1, 2, 3).
Product: Name of the product sold (e.g., Laptop, Mouse).
Quantity: Number of units sold.
Price: Price per unit.
Customer: Customer name.
Here’s a sample of what sales_data.csv might look like:

csv
Copy code
SaleID,Product,Quantity,Price,Customer
1,Laptop,1,1000,John
2,Mouse,3,25,Sarah
3,Keyboard,2,45,Bob
4,Monitor,1,200,Jessica
5,Webcam,5,35,Michael
Running the Script
To run the script, execute the following command:

bash
Copy code
python crud_operations.py
The script will load sales_data.csv, perform CRUD operations, and save the changes back to the file.

CRUD Operations Explained
1. Create: Adding a New Record
The create_record function appends a new record to the dataset. The new record is a dictionary containing values for each column.

Example
python
Copy code
new_record = {'SaleID': 6, 'Product': 'Headphones', 'Quantity': 2, 'Price': 50, 'Customer': 'Alice'}
data = create_record(data, new_record)
Expected Output:

plaintext
Copy code
Record added:
{'SaleID': 6, 'Product': 'Headphones', 'Quantity': 2, 'Price': 50, 'Customer': 'Alice'}
2. Read: Retrieving Records
The read_record function retrieves records that match a specified condition. For example, retrieving records where Product is Headphones.

Example
python
Copy code
read_record(data, 'Product', 'Headphones')
Expected Output:

plaintext
Copy code
Records found:
   SaleID     Product  Quantity  Price Customer
5       6  Headphones         2     50    Alice
3. Update: Modifying Records
The update_record function updates fields in records that match a specific condition. For example, updating the Quantity and Price of the record where SaleID is 6.

Example
python
Copy code
update_values = {'Quantity': 3, 'Price': 55}
data = update_record(data, 'SaleID', 6, update_values)
Expected Output:

plaintext
Copy code
Record(s) with SaleID = 6 updated with {'Quantity': 3, 'Price': 55}.
4. Delete: Removing Records
The delete_record function deletes records matching a specified condition. For example, deleting the record where SaleID is 6.

Example
python
Copy code
data = delete_record(data, 'SaleID', 6)
Expected Output:

plaintext
Copy code
Record(s) with SaleID = 6 deleted.
Saving Changes
After completing the CRUD operations, the updated data is saved back to the CSV file using the save_data function. This function overwrites the original file with the new, modified dataset.

python
Copy code
save_data(data, "sales_data.csv")
Dependencies
Pandas: Used for data manipulation. Install using pip install pandas.
Issues Encountered and Solutions
File Not Found: If sales_data.csv is not found, the script prints a warning and returns an empty dataset. Ensure that sales_data.csv exists in the same directory as crud_operations.py.
Missing Columns: Ensure that the CSV file matches the expected structure (columns SaleID, Product, Quantity, Price, Customer).
Example Usage
Create a new record.
Read a specific record.
Update a record’s details.
Delete a specific record.
Each CRUD operation can be demonstrated individually or in sequence within crud_operations.py.

License
This project is open-source and available for educational purposes.

