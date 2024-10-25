import pandas as pd

def load_data(sales_data.csv):
    try:
        data = pd.read_csv(sales_data.csv)
        print("Dataset loaded successfully.")
        return data
    except FileNotFoundError:
        print(f"File not found at {sales_data.csv}. Please check the path.")
        return pd.DataFrame()

def save_data(data, sales_data.csv):
    data.to_csv(sales_data.csv, index=False)
    print("Dataset saved successfully.")

# 1. Create
def create_record(data, new_record):
    data = pd.concat([data, pd.DataFrame([new_record])], ignore_index=True)
    print(f"Record added:\n{new_record}")
    return data

# 2. Read
def read_record(data, column, value):
    filtered_data = data[data[column] == value]
    if filtered_data.empty:
        print(f"No record found with {column} = {value}.")
    else:
        print(f"Records found:\n{filtered_data}")
    return filtered_data

# 3. Update
def update_record(data, column, value, update_values):
    condition = data[column] == value
    if condition.any():
        data.loc[condition, list(update_values.keys())] = list(update_values.values())
        print(f"Record(s) with {column} = {value} updated with {update_values}.")
    else:
        print(f"No record found with {column} = {value} to update.")
    return data

# 4. Delete
def delete_record(data, column, value):
    initial_count = data.shape[0]
    data = data[data[column] != value]
    final_count = data.shape[0]
    if initial_count == final_count:
        print(f"No record found with {column} = {value} to delete.")
    else:
        print(f"Record(s) with {column} = {value} deleted.")
    return data


def main():
    file_path = "sales_data.csv"
    data = load_data(sales_data.csv)
    if data.empty:
        return 

    new_record = {'SaleID': 6, 'Product': 'Headphones', 'Quantity': 2, 'Price': 50, 'Customer': 'Alice'}
    data = create_record(data, new_record)

    read_record(data, 'Product', 'Headphones')

    
    update_values = {'Quantity': 3, 'Price': 55}
    data = update_record(data, 'SaleID', 6, update_values)
    data = delete_record(data, 'SaleID', 6)


    save_data(data, sales_data.csv)

if __name__ == "__main__":
    main()
