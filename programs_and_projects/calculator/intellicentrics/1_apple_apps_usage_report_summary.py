
import pandas as pd

def total_active_devices_per_month(file_path):
    # Load the data skipping the first 3 rows of metadata
    df = pd.read_csv(file_path, skiprows=3, parse_dates=['Date'], dayfirst=False)

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])


    # Extract month and year for grouping
    df['YearMonth'] = df['Date'].dt.to_period('M')


    # Group by 'YearMonth' and sum the 'Active Devices'
    monthly_totals = df.groupby('YearMonth')['Active Devices'].sum().reset_index()

    return monthly_totals



# Sample usage
file_path = './resources/input_sec3ure_facility.csv'
result = total_active_devices_per_month(file_path)
print(result)




