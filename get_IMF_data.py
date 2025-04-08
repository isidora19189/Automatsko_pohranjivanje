import json
import pandas as pd

import opste_indicators as oi
from opste_DataGetter import DataGetter

data_loaded = False

if not data_loaded:
    data_getter = DataGetter()
    for indicator in oi.indicators:
        print("Gathering data for " + indicator + "...")
        data_getter.set_url(data_getter.make_url(indicator))
        data_getter.gather_data()
        data_getter.save_data('./indicators/' + indicator + '.json')
    print("All data gathered.")

final_df = pd.DataFrame()
for indicator in oi.indicators:
    with open('./indicators/' + indicator + '.json', 'r') as file:
        data = json.load(file)
        # Create a DataFrame from the JSON data
        df = pd.DataFrame(data)
        df = pd.DataFrame(df['values'][indicator])
        df = df.transpose()
        df.reset_index(inplace=True)
        df.rename(columns={'index': 'Country'}, inplace=True)
        df.insert(0, 'Unit', oi.indicator_dict[indicator]['unit'])
        df.insert(0, 'Descriptor', oi.indicator_dict[indicator]['label'])
        df.insert(0, 'Indicator', indicator)
        final_df = pd.concat([final_df, df], ignore_index=False)
        print("Data for " + indicator + " added to the final output...")
    
final_df.to_excel('excel/imf_output.xlsx', index=False)
print("Job finished. Check excel folder for output.")