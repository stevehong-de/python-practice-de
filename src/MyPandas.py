import pandas as pd
import io

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# load a csv file
e_commerce_data_path_csv = "../data/data.csv"
e_commerce_csv_df = pd.read_csv(e_commerce_data_path_csv,  encoding='unicode_escape', nrows=1000)

# show columns
print("\n[show columns]\n")
print(e_commerce_csv_df.columns)
print(e_commerce_csv_df)

# <Working with Datatypes>

# show types
print("\n[show types]\n")
print(e_commerce_csv_df.dtypes)

# change types
e_commerce_csv_df = e_commerce_csv_df.convert_dtypes()

# New dtypes
print(e_commerce_csv_df.dtypes)
temp_dtype_change_df = e_commerce_csv_df.astype(
    {'Quantity': 'float64',
     'CustomerID': 'float64'
     }
)
print(temp_dtype_change_df.dtypes)

# <Appending Dataframes>
print("\n[Appending Dataframe]\n")
# load json
e_commerce_data_path_json = "../data/data_subset.json"
e_commerce_json_df = pd.read_json(e_commerce_data_path_json,  encoding='unicode_escape')

# see how many rows you should have after appending
print(len(e_commerce_csv_df) + len(e_commerce_json_df))

# Append the csv and the json to a new dataframe (append method is deprecated. Use _append instead.)
e_commerce_appended_df = e_commerce_csv_df._append(e_commerce_json_df)
print(e_commerce_appended_df)

# print out first few rows of the dataframe
print(e_commerce_appended_df.head(10))


# <Merging of dataframes>
print("\n[Merging of dataframes]\n")
my_json = '{"Country" : ["United Kingdom", "France", "Australia", "Netherlands"], "Language":["English" , "French", "English" , "Dutch"]}'
# json_df = pd.read_json(my_json) DEPRECATED
json_df = pd.read_json(io.StringIO(my_json))
print(json_df)

e_commerce_csv_df = e_commerce_csv_df.merge(json_df, on="Country")
print(e_commerce_csv_df)

# <Turning into timestamp>
print("\n[Turning into timestamp]\n")
# do a lambda to change of the timestamp from / to epoch
# before
print(e_commerce_appended_df.dtypes)

e_commerce_appended_df['InvoiceDate'] = pd.to_datetime(
    e_commerce_appended_df['InvoiceDate'])

# after
print(e_commerce_appended_df.dtypes)

# Filter out two columns "Country" and "Quantity"
print(e_commerce_appended_df.columns)

e_commerce_appended_df = e_commerce_appended_df.drop(
    ["Country", "Quantity"], axis="columns")

print(e_commerce_appended_df.columns)

# normalize the dataframe
print("\n[Normalize the dataframe]\n")
# normalize a Pandas Column with Maximum Absolute Scaling using Pandas
print(e_commerce_csv_df.head(5))


cols_to_normalize = ["Quantity", "UnitPrice"]

def absolute_maximum_scale(series):
    return series / series.abs().max()

for column in cols_to_normalize:
    e_commerce_csv_df[column] = absolute_maximum_scale(e_commerce_csv_df[column])



print(e_commerce_csv_df.head(5))


# Working with lambdas
print("\n[Working with lambdas]\n")

e_commerce_csv_df['UnitPrice'] = e_commerce_csv_df['UnitPrice'].apply(lambda s: s*100)
print(e_commerce_csv_df)


# Pivoting dataframes
print("\n[Pivoting dataframes]\n")

# pivot the previously normalized dataframe
print(e_commerce_csv_df["Country"].unique())

e_commerce_csv_df["unique_id"] = e_commerce_csv_df["InvoiceNo"] + \
    e_commerce_csv_df["StockCode"] + \
    e_commerce_csv_df["CustomerID"].astype("str")

print(e_commerce_csv_df.head(10))

e_commerce_pivoted = (e_commerce_csv_df
                      .filter(items=["unique_id", "UnitPrice", "Country"])
                      .pivot_table(
                          index="unique_id",
                          columns="Country",  # Column(s) we want to pivot.
                          # Column with values that we want to have in our new pivoted columns.
                          values="UnitPrice",
                          # Even if there is not aggregation we need to provide aggregation funciton.
                          aggfunc="mean"
                      )
                      .reset_index()
                      )
print(e_commerce_pivoted)

# store dataframe as parquet file
e_commerce_pivoted.to_parquet('../data/e_commerce_pivoted.parquet.gzip',
                              compression='gzip')

# read parquet file
read_parquet = pd.read_parquet(
    '../data/e_commerce_pivoted.parquet.gzip')

print(read_parquet.head(10))

# melting dataframes
print("\n[Melting dataframes]\n")

print(e_commerce_json_df)
melted_df = e_commerce_json_df.melt(id_vars=['InvoiceNo'])
print(melted_df)


# Flattening (normalizing of ) dataframes from nested JSONs
print("\n[Flattening (normalizing of ) dataframes from nested JSONs]\n")
json_obj = {
    'InvoiceNo': '536370',
    'Quantity': 36,
    'InvoiceDate': '12/1/2010 8:45',
    'CustomerID': 2,
    'Country': 'France',
    'item': {
        'StockCode': 'John Kasich',
        'Description': 'MINI PAINT SET VINTAGE',
        'UnitPrice': 'UnitPrice'}
}
json_df_raw = pd.DataFrame.from_dict(json_obj)
print(json_df_raw.dtypes)

json_df_normalized = pd.json_normalize(json_obj)
print(json_df_normalized.dtypes)