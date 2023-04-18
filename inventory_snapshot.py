import pandas as pd
import numpy as np
import argparse
from helpers import Helper


def main(date):
    # Create a helper object
    helper = Helper()

    # Extract the data from a source
    inventory = pd.read_csv(f'Inventory_Query_US_CA_{date}.csv')
    prod_info = pd.read_excel('Product_Info.xlsx')
    site_info = pd.read_excel('Site_Info.xlsx')
    prod2 = pd.read_csv('prod2.csv')

    # Remove whitespace from column names
    inventory = helper.remove_whitespace_from_column_names(inventory)
    prod_info = helper.remove_whitespace_from_column_names(prod_info)
    site_info = helper.remove_whitespace_from_column_names(site_info)
    prod2 = helper.remove_whitespace_from_column_names(prod2)

    # Transform the data
    # Step 0: Only look at accessories and hardware data in inventory.
    inventory = inventory[(inventory['list_item_name'] == 'CF: Accessory') | (inventory['list_item_name'] == 'CF: Hardware')]

    # Step 1: Add `Site Type` info.
    step1_st = inventory.merge(right=site_info, on='loc', how='left')
    step1_st = helper.move_column_after(step1_st, 'Site Type', 'loc')

    # Step 2: Add `Product Group` and `Product Family` info.
    step2_pgpf = step1_st.merge(right=prod_info, on='item', how='left')
    step2_pgpf = helper.move_column_after(step2_pgpf, 'Product Group', 'item')
    step2_pgpf = helper.move_column_after(step2_pgpf, 'Product Family', 'Product Group')

    # Step 3: Add `Sellable/Non Sellable` column.
    step3_sell = step2_pgpf
    step3_sell['Sellable/Non Sellable'] = step3_sell['bucket'].apply(lambda x: 'Sellable' if x == 'Sellable' or x == 'In Transit' else 'NonSellable')
    step3_sell = helper.move_column_after(step3_sell, 'Sellable/Non Sellable', 'bucket')

    # Step 4: Compute `Pallets` column.
    step4_pallets = step3_sell
    step4_pallets['Pallets'] = step4_pallets['qty']/step4_pallets['Units/Pallet']

    # Step 5: Adjust Sellable/Non Sellable multiplier info.
    step5_multiplier = step4_pallets
    step5_multiplier['multiplier'] = step5_multiplier['Sellable/Non Sellable'].apply(lambda x: 2 if x == 'NonSellable' else 1)

    # Step 6: Compute pallet positions.
    step6_positions = step5_multiplier
    step6_positions['Pallet Positions'] = np.ceil(step6_positions['Pallets']*step6_positions['multiplier'])

    # Step 7: Drop extra columns.
    result = step6_positions
    result = result.drop(columns=['warehouse_code', 'multiplier'])

    # Load the data into a destination
    result.to_excel(f'Inventory_Snapshot_US_CA_{date}.xlsx', index=False)
    result.to_csv(f'Inventory_Snapshot_US_CA_{date}.csv', index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("date", help="date to run the script")
    args = parser.parse_args()

    main(args.date)
