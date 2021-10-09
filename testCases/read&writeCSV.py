import csv
import os
import pandas as pd

current_dir = os.getcwd()
os.chdir('..')
base_dir = os.getcwd()
products_listing_path = os.path.join(base_dir, "CSV files", "Jan_2021_billings.csv")
billings_path = os.path.join(base_dir, "CSV files", "products_listing.csv")

# reading two csv files
products_listing = pd.read_csv(products_listing_path)
billings = pd.read_csv(billings_path)

# remove columns and rows with nan for file1
prod_list = products_listing.dropna(axis=1, how='all')
final_prod_list = prod_list.dropna(axis=0, how='all')

# remove columns and rows with NaN for file2
bill = billings.dropna(axis=1, how='all')
final_billing = bill.dropna(axis=0, how='all')

# Join and fetch only matching data
result_set = pd.merge(final_prod_list, final_billing,
                      on='product_code',
                      how='inner')

final_result = result_set[['customer_id', 'cust_name', 'product_name', 'product_code']]

final_result.to_csv(os.path.join(base_dir, "CSV files", "final_data.csv"))
