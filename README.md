# inventory_snapshot
This project utilizes inventory data from `ds-redshift-scds` to compute the pallet positions for CFUs and accessories.

## Input Data

### Data Description
- **Inventory_Query_US_CA_{date}.csv:** Contains the inventory status as of {date} for the US and CA regions.
- **Product_Info.xlsx:** Contains information on Product Group, Product Family, and the conversion rate of units to pallets.
- **Site_Info.xlsx:** Contains information on whether a site is FM (Final Mile) or MM (Middle Mile).

### Data Source
- **Inventory_Query_US_CA_{date}.csv:** [PopSQL](https://app.popsql.com/queries/-NRFJeAZv00l5-w5Uk7b/inventory-query)
- **Product_Info.xlsx, Site_Info.xlsx:** [Google Drive](https://drive.google.com/drive/folders/1TXqVt623TTIwdB2KWcrA6oLyW2ymyOg8?usp=sharing)

## How to Run

1. Run the query in [PopSQL](https://app.popsql.com/queries/-NRFJeAZv00l5-w5Uk7b/inventory-query) with the desired {snapshot_date} (e.g. snapshot_date = '2023-03-20'). Save the query output as a CSV file (e.g. **Inventory_Query_US_CA_2023-03-20.csv:**).
2. In terminal, run: `python inventory_snapshot.py 2023-03-20`
3. Upload the outputfile: **Inventory_Snapshot_US_CA_2023-03-20.xlsx** to [14. Key Data Folder -> 04. Inventory Snapshots](https://drive.google.com/drive/folders/1vwk2KhRMVAHd1ukVELc_shUF_8eL45iP)
