import pandas as pd

def main():
    # The file name is hardcoded and assigned to fp.
    fp = 'C:\\Users\\Atharva Choudhari\\Research\\data\\retail_db_json\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e'

    df = pd.read_json(fp, lines=True)

    # print(df.count())
    # print(df.describe())
    # print(df.columns)
    # print(df.dtypes)
    # print(df[['order_item_order_id', 'order_item_subtotal']])
    # print(df['order_item_order_id'] == 2)
    print(df[df['order_item_order_id'] == 2])


if __name__ == "__main__":
    main()