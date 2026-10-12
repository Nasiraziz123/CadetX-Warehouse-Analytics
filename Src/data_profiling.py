import pandas as pd


def info (name,table):
    print(f"name of table is : {name}")
    print(f"shape of {name} is :\n",table.shape)
    print(f"columns of {name} are :\n",table.columns.tolist())
    print(f"data types of {name} are : \n",table.dtypes)
    print(f"null values in {name} are : \n",table.isnull().sum())
    print(f"duplicated values in {name} are : \n",table.duplicated().sum())
    print(f"first 10 rows of {name} are : \n",table.head(10).to_string())

customers=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\customers.csv")

info("customers",customers)

print("unique customer are : ",customers["customer_id"].nunique())
print("length of customer table is :",len(customers))
print("duplicated customers are : ",customers["customer_id"].duplicated().sum())

print("description of numeric field of customers table : \n",customers[["credit_limit","current_balance","total_purchase_value","customer_rating"]].describe())

customers["customer_since"]=pd.to_datetime(customers["customer_since"],errors="coerce")
customers["last_purchase_date"]=pd.to_datetime(customers["last_purchase_date"],errors="coerce")

invalid_dates=customers[customers["last_purchase_date"]<customers["customer_since"]]

print("Customers whose last purchase precedes their start date::\n",len(invalid_dates))
print("invalid dates : \n",invalid_dates[["customer_id","customer_since","last_purchase_date"]])

print(customers[["customer_since","last_purchase_date"]].isna().sum())


print("\n\n")
print("*************** BRANCHES TABLE ***************")
print()
branches=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\branches.csv")

info("branches",branches)


print("unique branches are : ",branches["branch_id"].nunique())
print("total branches recorded are : ",len(branches))
print("duplicated id in branches are : ",branches["branch_id"].duplicated().sum())
print("branches id:\n",branches["branch_id"].to_list())

customer_branch_check=customers[~customers["branch_id"].isin(branches["branch_id"])]

print("customers refrencing unknown branches are : ",len(customer_branch_check))

print(customer_branch_check[["customer_id","branch_id"]])


print("\n\n")
print("*************** PRODUCTS TABLE ***************")
print()

products=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\products.csv")
info("products",products)

print("unique products id are : ",products["product_id"].nunique())

print("total product records are : ",len(products))

print("duplicated product id are :",products["product_id"].duplicated().sum())

products["last_purchase_date"]=pd.to_datetime(products["last_purchase_date"],errors="coerce")

print("last purchase date dtype: ",products["last_purchase_date"].dtypes)



print("products with invalid purchase dates are : ",products["last_purchase_date"].isna().sum())

print("earliest last purchase date are : ",products["last_purchase_date"].min())

print("latest last purchase date are : ",products["last_purchase_date"].max())

print("reorder level greater then safety stocks are :",(products["reorder_level"]>products["safety_stock"]).sum())

print("max stock level below reorder level are : ",(products["max_stock_level"]<products["reorder_level"]).sum())

print("zero or negative stock thresolds are : ")
print(products[(products["reorder_level"]<=0) |  
               (products["safety_stock"]<=0) |
               (products["max_stock_level"]<=0)][["product_id","reorder_level","safety_stock","max_stock_level"]])

print("unit cost greater then unit price are : ", (products["unit_cost"]>products["unit_price"]).sum())

print("zero or negative prices are :")
print(products[(products["unit_cost"]<=0) | products["unit_price"]<=0 | (products["last_purchase_price"]<=0)][["product_id","unit_cost","unit_price","last_purchase_price"]] )

print("margin percentage outside 0-100 are : ")

print(products[(products["margin_percentage"]<0) | (products["margin_percentage"]>100)][["product_id","margin_percentage"]])


print("unique product categories are \n",products["category"].value_counts())

print("unique machine types are \n",products["machine_type"].value_counts())

print("unique criticality levels are \n",products["criticality_level"].value_counts())

print("unique unit of measures are \n",products["uom"].value_counts())



print("\n\n")

print("*************** Supplier TABLE ***************")

suppliers=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\suppliers.csv")

info("suppliers",suppliers)

print("unique id in suppliers are :",suppliers["supplier_id"].nunique())

print("total records in suppliers are : ",len(suppliers))

print("duplicated id in suppliers are :",suppliers["supplier_id"].duplicated().sum())



print("\n\n")

print("***********inventory master table***************")

inventry_master=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\inventory_master.csv")

info("inventry_master",inventry_master)


print("duplicated branch id and product id are : ",inventry_master.duplicated(subset=["branch_id","product_id"]).sum())

print("unique product id are : ",inventry_master["product_id"].nunique())
print("unique branch id are : ",inventry_master["branch_id"].nunique())
print("unique ware house bins are : ",inventry_master["warehouse_bin"].nunique())

print("current stock above max stock are : ",(inventry_master["current_stock"]>inventry_master["max_stock"]).sum())

print(inventry_master.loc[inventry_master["current_stock"]>inventry_master["max_stock"],["product_id","branch_id","opening_stock","current_stock","max_stock"]].head(10))


print("negative stock value : ",((inventry_master["current_stock"]<0) | (inventry_master["opening_stock"]<0)).sum())

print("reorder level above max stock level : ",(inventry_master["reorder_level"]>inventry_master["max_stock"]).sum())

print("safety stock above max stock : ",(inventry_master["safety_stock"]>inventry_master["max_stock"]).sum())

print("inventry recored with unknown product id : ",(~inventry_master["product_id"].isin(products["product_id"])).sum())

print("inventry record with unknown branche id are : ",(~inventry_master["branch_id"].isin(branches["branch_id"])).sum())

print(inventry_master[["product_id","branch_id","opening_stock","max_stock","current_stock"]].sort_values("current_stock",ascending=False).head(10))

print("describing current stock : ",inventry_master["current_stock"].describe())

print("unique values in current stock are \n ",inventry_master["current_stock"].nunique())

print("describing opening stock ,reorder level,safety stock,max_stock,current stock \n",inventry_master[["opening_stock","reorder_level","safety_stock","max_stock","current_stock"]].describe())


stock_difference=(inventry_master["current_stock"]-inventry_master["opening_stock"])

print("describing stock difference : ",stock_difference.describe())







print("\n\n")
print("***********purchase order header table***************")

purchase_orders_header=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\purchase_orders_header.csv")   

info("purchase_orders_header",purchase_orders_header)

purchase_orders_header["order_date"]=pd.to_datetime(purchase_orders_header["order_date"],errors="coerce")


purchase_orders_header["expected_delivery_date"]=pd.to_datetime(purchase_orders_header["expected_delivery_date"],errors="coerce")


purchase_orders_header["received_date"]=pd.to_datetime(purchase_orders_header["received_date"],errors="coerce")



print("unique purhase order ids are : ",purchase_orders_header["po_id"].nunique())

print("total purchase order records are : ",len(purchase_orders_header))

print("duplicated purchase order id are : ",purchase_orders_header["po_id"].duplicated().sum())


print("purchase orders with invalid branch_id are : ",(~purchase_orders_header["branch_id"].isin(branches["branch_id"])).sum())

print("purchase orders with invalid supplier_id are : ",(~purchase_orders_header["supplier_id"].isin(suppliers["supplier_id"])).sum())

print(purchase_orders_header[["order_date","expected_delivery_date","received_date"]].dtypes)

print("purchase order with invalid order dates are : ",purchase_orders_header["order_date"].isna().sum())


print("purchase order with invalid expected delivery  dates are : ",((purchase_orders_header["expected_delivery_date"].isna().sum())))

print("purchase order header po status col value counts are : \n",purchase_orders_header["po_status"].value_counts())


print(purchase_orders_header.groupby("po_status")["received_date"].agg(total_order="size", missing_received_dates=lambda x: x.isna().sum()))

print("expected_delivery_date before order date are : ",(purchase_orders_header["expected_delivery_date"]<purchase_orders_header["order_date"]).sum())

print("recieved_date before order date are : ",(purchase_orders_header["received_date"]<purchase_orders_header["order_date"]).sum())

print("recieved after expected delievry date are : ",(purchase_orders_header["received_date"]>purchase_orders_header["expected_delivery_date"]).sum())


total_difference=(purchase_orders_header["grand_total"]-(purchase_orders_header["total_cost"]+purchase_orders_header["total_gst_amount"]))

print("absoulute difference")

print("description of absolute difference \n",total_difference.abs().describe())

print("the absoulte total difeerence above 1 are :",(total_difference.abs()>1).sum())





print("\n\n")

print("***********purchase orders lines table*************")


purchase_orders_lines=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\purchase_orders_lines.csv")

info("purchase_orders_lines",purchase_orders_lines)

print("unique purchase id in purchase order lines are : ",purchase_orders_lines["po_id"].nunique())

print("total_records in purchase order lines are : ",len(purchase_orders_lines))

print("invalid product id in purchase rders lines are : ",(~purchase_orders_lines["product_id"].isin(products["product_id"])).sum())

print("duplicated purchase id are ",purchase_orders_lines["po_id"].duplicated().sum())

print(purchase_orders_lines.groupby("po_id")["product_id"].agg(total_product="size"))


print("duplicate purchase order + line number are : ",purchase_orders_lines.duplicated(subset=["po_id","line_number"]).sum())

print("purchase order lines with invalid purchase id are : ",(~purchase_orders_lines["po_id"].isin(purchase_orders_header["po_id"])).sum())

print("quantity less than 0 : ",(purchase_orders_lines["quantity"]<0).sum())

print("total cost less than 0 : ",(purchase_orders_lines["unit_cost"]<0).sum())

print("total gst amount less than 0 or greater than 100 : ",((purchase_orders_lines["gst_rate"]<0) | (purchase_orders_lines["gst_rate"])>100).sum())

print("negative lines : ",(purchase_orders_lines["line_total"]<0).sum())



print("quantity less than or equal to  0 : ",(purchase_orders_lines["quantity"]<=0).sum())



print("unit cost less than or equal to 0 : ",(purchase_orders_lines["unit_cost"]<=0).sum())


print("negative gst amount : ",(purchase_orders_lines["gst_amount"]<0).sum())

print("negative line grand total : ",(purchase_orders_lines["line_grand_total"]<0).sum())


print(
    "GST rates outside 0–100:",
    (
        (purchase_orders_lines["gst_rate"] < 0)
        | (purchase_orders_lines["gst_rate"] > 100)
    ).sum()
)

expected_line_total=(purchase_orders_lines["quantity"]*purchase_orders_lines["unit_cost"])

line_total_difference=(purchase_orders_lines["line_total"]-expected_line_total)

print("absoulte difference")

print("description of absolute line difference")
print(line_total_difference.abs().describe())

print("the absoulte line difeerence above 1 are :",(line_total_difference.abs()>1).sum())

expected_gst=(purchase_orders_lines["line_total"]*purchase_orders_lines["gst_rate"]/100)

gst_difference=(purchase_orders_lines["gst_amount"]-expected_gst)

print(" description of absolute gst difference : ",gst_difference.abs().describe())

print("the absoulte gst difeerence above 1 are :",(gst_difference.abs()>1).sum())


expected_line_grand_total=(purchase_orders_lines["line_total"]+purchase_orders_lines["gst_amount"])

line_grand_total_difference=(purchase_orders_lines["line_grand_total"]-expected_line_grand_total)

print("the description of absolute grand total difference \n",line_grand_total_difference.abs().describe())

print("absoultee line grand total difference above 1 are : ",(line_grand_total_difference.abs()>1).sum())




print("\n\n")

print("********sales order header table********")

sales_orders_header = pd.read_csv(
    "C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\sales_orders_header.csv"
)

info("sales_orders_header", sales_orders_header)


print("unique so_id in sales order header are : ",sales_orders_header["so_id"].nunique())

print("total_records in sales order header are : ",len(sales_orders_header))

print("duplicate so_id in sales order header are : ",sales_orders_header["so_id"].duplicated().sum())

sales_orders_header["order_date"]=pd.to_datetime(sales_orders_header["order_date"],errors="coerce")

sales_orders_header["delivery_date"]=pd.to_datetime(sales_orders_header["delivery_date"])

print(sales_orders_header[["delivery_date","order_date"]].dtypes)

print("invalid_dates in sales order header,delivery date less than order date : ",(sales_orders_header["delivery_date"]<sales_orders_header["order_date"]).sum())

print("invalid order dates are : ",sales_orders_header["order_date"].isna().sum())

print("invalid delivery dates are : ",sales_orders_header["delivery_date"].isna().sum())

print("invalid customer id in sales order header are : ",(~sales_orders_header["customer_id"].isin(customers["customer_id"])).sum())

print("invalud branch id in sales order header are : ",(~sales_orders_header["branch_id"].isin(branches["branch_id"])).sum())



expected_grand_total = (
    sales_orders_header["total_order_value"]
    + sales_orders_header["total_gst_amount"]
)

grand_total_difference = (
    sales_orders_header["grand_total"]
    - expected_grand_total
)

print("Absolute grand-total difference:")
print(grand_total_difference.abs().describe())

print(
    "Differences above 1 currency unit:",
    (grand_total_difference.abs() > 1).sum()
)


print("value counts of sales order header order status are \n",sales_orders_header["order_status"].value_counts(dropna=False))

print("delivery_rate availabily by order status ")

status_check=sales_orders_header.groupby("order_status",dropna=False).agg(total_orders=("so_id","size"),available_delivery_date=("delivery_date","count"),missing_delivery_dates=("delivery_date",lambda x:x.isna().sum()))

print(status_check)


cancelled_orders=sales_orders_header[sales_orders_header["order_status"]=="Cancelled"]

print("first 10 rows of cancelled order are \n",cancelled_orders[["so_id","order_date","delivery_date","order_status"]].head(10).to_string(index=False))

print("cancelled order with delivery date on or after order date",(cancelled_orders["delivery_date"]>=cancelled_orders["order_date"]).sum())




print("\n\n")

print("***********sales order line************")


sales_orders_lines = pd.read_csv(
    "C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\sales_orders_lines.csv"
)

info("sales_orders_lines", sales_orders_lines)

print("unique so_id are : ",sales_orders_lines["so_id"].nunique())

print("total records are : ",len(sales_orders_lines))

print("duplicated so_id are : ",sales_orders_lines["so_id"].duplicated().sum())

print("invalid so_id in sales order lines are : ",(~sales_orders_lines["so_id"].isin(sales_orders_header["so_id"])).sum())

print("invalid product_id in sales order line are : ",(~sales_orders_lines["product_id"].isin(products["product_id"])).sum())


print("duplicate so_id,line_number combination are : ",sales_orders_lines.duplicated(subset=["so_id","line_number"]).sum())

print("unique line number per sales order are : ",sales_orders_lines.groupby("so_id")["line_number"].nunique().describe())



print("Quantity less than or equal to zero:",
      (sales_orders_lines["quantity"] <= 0).sum())

print("Unit price less than or equal to zero:",
      (sales_orders_lines["unit_price"] <= 0).sum())

print("GST rate below zero:",
      (sales_orders_lines["gst_rate"] < 0).sum())

print("GST rate above 100:",
      (sales_orders_lines["gst_rate"] > 100).sum())

print("Negative line totals:",
      (sales_orders_lines["line_total"] < 0).sum())

print("Negative GST amounts:",
      (sales_orders_lines["gst_amount"] < 0).sum())

print("Negative line grand totals:",
      (sales_orders_lines["line_grand_total"] < 0).sum())


expected_line_total = (
    sales_orders_lines["quantity"]
    * sales_orders_lines["unit_price"]
)

line_total_difference = (
    sales_orders_lines["line_total"]
    - expected_line_total
)

print("Absolute line-total difference:")
print(line_total_difference.abs().describe())

print(
    "Differences above 1 currency unit:",
    (line_total_difference.abs() > 1).sum()
)



expected_gst = (
    sales_orders_lines["line_total"]
    * sales_orders_lines["gst_rate"]
    / 100
)

gst_difference = (
    sales_orders_lines["gst_amount"]
    - expected_gst
)

print("Absolute GST difference:")
print(gst_difference.abs().describe())

print(
    "GST differences above 1 currency unit:",
    (gst_difference.abs() > 1).sum()
)

expected_line_grand_total = (
    sales_orders_lines["line_total"]
    + sales_orders_lines["gst_amount"]
)

line_grand_total_difference = (
    sales_orders_lines["line_grand_total"]
    - expected_line_grand_total
)

print("Absolute grand-total difference:")
print(line_grand_total_difference.abs().describe())

print(
    "Grand-total differences above 1 currency unit:",
    (line_grand_total_difference.abs() > 1).sum()
)


print("\n\n")

print("*****stock ledger*******")

stock_ledger = pd.read_csv(
    "C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\stock_ledger.csv"
)

info("stock_ledger", stock_ledger)

print("unique moment_id in stock ledger are : ",stock_ledger["movement_id"].nunique())
print("total records are : ",len(stock_ledger))
print("duplicate movement id are :",stock_ledger["movement_id"].duplicated().sum())

print("negative quantity are : ",(stock_ledger["quantity"]<0).sum())
stock_ledger["movement_date"]=pd.to_datetime(stock_ledger["movement_date"],errors="coerce")

print("invalid date are : ",stock_ledger["movement_date"].isna().sum())

print("invalid product id are : ",(~stock_ledger["product_id"].isin(products["product_id"])).sum())

print("invalud branh id are : ",(~stock_ledger["branch_id"].isin(branches["branch_id"])).sum())


print("moment type value counts \n",stock_ledger["movement_type"].value_counts(dropna=False))

print("reference type value counts \n ",stock_ledger["reference_type"].value_counts(dropna=False))

print(
    pd.crosstab(
        stock_ledger["movement_type"],
        stock_ledger["reference_type"]
    )
)

# Check purchase-order references
po_movements = stock_ledger[
    stock_ledger["reference_type"] == "PO"
]

print(
    "Invalid PO references:",
    (~po_movements["reference_id"].isin(
        purchase_orders_header["po_id"]
    )).sum()
)

# Check sales-order references
so_movements = stock_ledger[
    stock_ledger["reference_type"] == "SO"
]

print(
    "Invalid SO references:",
    (~so_movements["reference_id"].isin(
        sales_orders_header["so_id"]
    )).sum()
)


print("Zero quantities:", (stock_ledger["quantity"] == 0).sum())

print("\nQuantity summary by movement type:")
print(
    stock_ledger.groupby("movement_type")["quantity"]
    .agg(["count", "min", "max", "mean"])
)


# Sort transactions chronologically for each product and branch
stock_ledger = stock_ledger.sort_values(
    ["product_id", "branch_id", "movement_date", "movement_id"]
)

# Inspect the first 15 transactions for one product at one branch
sample = stock_ledger[
    (stock_ledger["product_id"] == "P001") &
    (stock_ledger["branch_id"] == "AHM001")
]

print(
    sample[
        [
            "movement_id",
            "movement_date",
            "movement_type",
            "quantity",
            "running_balance"
        ]
    ].head(15).to_string(index=False)
)


print(
    sample.loc[
        sample["movement_date"] == "2019-02-08",
        [
            "movement_id",
            "movement_type",
            "quantity",
            "running_balance"
        ]
    ].to_string(index=False)
)

stock_ledger["previous_balance"] = (
    stock_ledger
    .groupby(["product_id", "branch_id"])["running_balance"]
    .shift(1)
)

stock_ledger["expected_balance"] = stock_ledger["previous_balance"]

stock_ledger.loc[
    stock_ledger["movement_type"] == "IN", "expected_balance"
] += stock_ledger.loc[
    stock_ledger["movement_type"] == "IN", "quantity"
]

stock_ledger.loc[
    stock_ledger["movement_type"] == "OUT", "expected_balance"
] -= stock_ledger.loc[
    stock_ledger["movement_type"] == "OUT", "quantity"
]

stock_ledger["balance_mismatch"] = (
    stock_ledger["movement_type"].isin(["IN", "OUT"])
    & stock_ledger["previous_balance"].notna()
    & (
        stock_ledger["running_balance"]
        != stock_ledger["expected_balance"]
    )
)

print(
    "IN/OUT balance mismatches:",
    stock_ledger["balance_mismatch"].sum()
)


mismatches = stock_ledger[
    stock_ledger["balance_mismatch"]
]

print(
    mismatches[
        [
            "product_id",
            "branch_id",
            "movement_date",
            "movement_type",
            "quantity",
            "previous_balance",
            "expected_balance",
            "running_balance"
        ]
    ].head(15).to_string(index=False)
)

ledger_test = stock_ledger.copy()

ledger_test["movement_number"] = (
    ledger_test["movement_id"]
    .str.extract(r"(\d+)$")
    .astype(int)
)

ledger_test = ledger_test.sort_values(
    ["product_id", "branch_id", "movement_number"]
)

ledger_test["previous_balance"] = (
    ledger_test
    .groupby(["product_id", "branch_id"])["running_balance"]
    .shift(1)
)

ledger_test["expected_balance"] = ledger_test["previous_balance"]

incoming = ledger_test["movement_type"] == "IN"
outgoing = ledger_test["movement_type"] == "OUT"

ledger_test.loc[incoming, "expected_balance"] += (
    ledger_test.loc[incoming, "quantity"]
)

ledger_test.loc[outgoing, "expected_balance"] -= (
    ledger_test.loc[outgoing, "quantity"]
)

ledger_test["balance_mismatch"] = (
    ledger_test["movement_type"].isin(["IN", "OUT"])
    & ledger_test["previous_balance"].notna()
    & (
        ledger_test["running_balance"]
        != ledger_test["expected_balance"]
    )
)

print(
    "Mismatches when sorted by movement ID number:",
    ledger_test["balance_mismatch"].sum()
)


print("Movement ID examples:")
print(stock_ledger["movement_id"].head(10).to_list())

print("\nReference ID examples:")
print(stock_ledger["reference_id"].head(10).to_list())

print("\nMovement ID format counts:")
print(
    stock_ledger["movement_id"]
    .str.extract(r"^(MOV-[A-Z]+)-")[0]
    .value_counts(dropna=False)
)

print("\nReference type and movement type:")
print(
    pd.crosstab(
        stock_ledger["movement_type"],
        stock_ledger["reference_type"]
    )
)


adjustments = stock_ledger[
    stock_ledger["reference_type"] == "ADJ"
]

print("Total adjustment records:", len(adjustments))
print(
    "Unique adjustment reference IDs:",
    adjustments["reference_id"].nunique()
)
print("\nSample adjustment records:")
print(
    adjustments[
        [
            "movement_id",
            "product_id",
            "branch_id",
            "movement_date",
            "quantity",
            "reference_id",
            "running_balance"
        ]
    ].head(10).to_string(index=False)
)




print("\n\n")

print("*******invoices******")

invoices = pd.read_csv(
    "C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\invoices.csv"
)

info("invoices", invoices)

invoices["invoice_date"]=pd.to_datetime(invoices["invoice_date"],errors="coerce")

invoices["due_date"]=pd.to_datetime(invoices["due_date"],errors="coerce")

print("unique invoice id in invoices are : ",invoices["invoice_id"].nunique())

print("total_records : ",len(invoices))

print("duplicated invoice id are : ",invoices["invoice_id"].duplicated().sum())

print("invalid invoice date are : ",invoices["invoice_date"].isna().sum())
print("invalid due dates are : ",invoices["due_date"].isna().sum())

print("due date before invoice date are ",(invoices["due_date"]<invoices["invoice_date"]).sum())

print("invalid so_id are ",(~invoices["so_id"].isin(sales_orders_header["so_id"])).sum())


print("invalid customer_id are ",(~invoices["customer_id"].isin(customers["customer_id"])).sum())


print("invalid branch_id are ",(~invoices["branch_id"].isin(branches["branch_id"])).sum())

print("value count of payment status are \n",invoices["payment_status"].value_counts())


duplicate_invoices = invoices[
    invoices["invoice_id"].duplicated(keep=False)
].sort_values("invoice_id")

print("Rows with duplicated invoice IDs:", len(duplicate_invoices))

print(
    duplicate_invoices.head(20).to_string(index=False)
)


duplicate_id_counts = invoices["invoice_id"].value_counts()

print(
    "Number of invoice IDs appearing more than once:",
    (duplicate_id_counts > 1).sum()
)

print(
    "Maximum occurrences of a single invoice ID:",
    duplicate_id_counts.max()
)

print(
    "Invoice IDs appearing more than twice:",
    (duplicate_id_counts > 2).sum()
)


invoice_difference = invoices["grand_total"] - (
    invoices["total_order_value"] + invoices["total_gst_amount"]
)

print("Absolute difference summary:")
print(invoice_difference.abs().describe())

print(
    "Invoices with a difference greater than 1:",
    (invoice_difference.abs() > 1).sum()
)


print(
    "Unique sales orders in invoices:",
    invoices["so_id"].nunique()
)

print(
    "Total invoice records:",
    len(invoices)
)

print(
    "Sales orders with multiple invoice records:",
    invoices["so_id"].duplicated().sum()
)


# Count sales orders by status
print(sales_orders_header["order_status"].value_counts())

# Check whether any cancelled orders have invoices
cancelled_orders = sales_orders_header[
    sales_orders_header["order_status"] == "Cancelled"
]

print(
    "Cancelled orders:",
    len(cancelled_orders)
)

print(
    "Cancelled orders with invoices:",
    cancelled_orders["so_id"].isin(invoices["so_id"]).sum()
)


invoice_order_check = invoices.merge(
    sales_orders_header[
        ["so_id", "total_order_value", "total_gst_amount", "grand_total"]
    ],
    on="so_id",
    how="left",
    suffixes=("_invoice", "_sales_order")
)

print(
    "Order value mismatches:",
    (
        (invoice_order_check["total_order_value_invoice"]
         - invoice_order_check["total_order_value_sales_order"]).abs() > 1
    ).sum()
)

print(
    "GST amount mismatches:",
    (
        (invoice_order_check["total_gst_amount_invoice"]
         - invoice_order_check["total_gst_amount_sales_order"]).abs() > 1
    ).sum()
)

print(
    "Grand total mismatches:",
    (
        (invoice_order_check["grand_total_invoice"]
         - invoice_order_check["grand_total_sales_order"]).abs() > 1
    ).sum()
)


print(
    invoices.groupby("payment_status")["grand_total"]
    .agg(["count", "sum", "mean"])
    .round(2)
)


print("\n\n")

print("*********payment*******")

payments=pd.read_csv("C:\\Users\\JunaidAzizi\\Desktop\\practice\\projects\\CadetX_Warehouse_Analytics\\Data\\payments.csv")

info("payments",payments)

payments["payment_date"]=pd.to_datetime(payments["payment_date"],errors="coerce")

print("unique payment id are : ",payments["payment_id"].nunique())

print("total records are : ",len(payments))

print("duplicate payment id are : ",payments["payment_id"].duplicated().sum())

print("invalid payments dates : ",payments["payment_date"].isna().sum())
print("invalid invoice id are : ",(~payments["invoice_id"].isin(invoices["invoice_id"])).sum())

print("payment method value count \n",payments["payment_method"].value_counts())



duplicate_payment_counts = payments["payment_id"].value_counts()

print(
    "Payment IDs appearing more than once:",
    (duplicate_payment_counts > 1).sum()
)

print(
    "Maximum occurrences of one payment ID:",
    duplicate_payment_counts.max()
)

print(
    "Payment IDs appearing more than twice:",
    (duplicate_payment_counts > 2).sum()
)



duplicate_payments = payments[
    payments["payment_id"].duplicated(keep=False)
].sort_values("payment_id")

print("Rows with repeated payment IDs:", len(duplicate_payments))

print(duplicate_payments.head(20).to_string(index=False))




print(
    "Zero payment amounts:",
    (payments["payment_amount"] == 0).sum()
)

print(
    "Negative payment amounts:",
    (payments["payment_amount"] < 0).sum()
)

print("Payment amount summary:")
print(payments["payment_amount"].describe())




payments_by_invoice = (
    payments.groupby("invoice_id", as_index=False)
    ["payment_amount"]
    .sum()
    .rename(columns={"payment_amount": "total_paid"})
)

invoice_payment_check = invoices.merge(
    payments_by_invoice,
    on="invoice_id",
    how="left"
)

invoice_payment_check["total_paid"] = (
    invoice_payment_check["total_paid"].fillna(0)
)

print(
    "Invoices with payments exceeding grand total:",
    (
        invoice_payment_check["total_paid"]
        > invoice_payment_check["grand_total"] + 1
    ).sum()
)






overpaid_invoices = invoice_payment_check[
    invoice_payment_check["total_paid"]
    > invoice_payment_check["grand_total"] + 1
].copy()

overpaid_invoices["excess_paid"] = (
    overpaid_invoices["total_paid"]
    - overpaid_invoices["grand_total"]
)

print(
    overpaid_invoices[
        [
            "invoice_id",
            "so_id",
            "grand_total",
            "total_paid",
            "excess_paid",
            "payment_status"
        ]
    ].head(10).to_string(index=False)
)




print(
    "Affected invoices with duplicated invoice IDs:",
    overpaid_invoices["invoice_id"].duplicated(keep=False).sum()
)

print(
    "Distinct affected invoice IDs:",
    overpaid_invoices["invoice_id"].nunique()
)

print(
    "Repeated invoice IDs in the original invoice table:",
    invoices["invoice_id"].duplicated().sum()
)




repeated_invoice_ids = invoices.loc[
    invoices["invoice_id"].duplicated(keep=False),
    "invoice_id"
].unique()

payments_to_repeated_ids = payments[
    payments["invoice_id"].isin(repeated_invoice_ids)
]

print(
    "Payment records linked to repeated invoice IDs:",
    len(payments_to_repeated_ids)
)

print(
    "Distinct repeated invoice IDs with payments:",
    payments_to_repeated_ids["invoice_id"].nunique()
)

print(
    "Total payment amount linked to repeated invoice IDs:",
    round(payments_to_repeated_ids["payment_amount"].sum(), 2)
)



overpaid_repeated_ids = overpaid_invoices[
    overpaid_invoices["invoice_id"].isin(repeated_invoice_ids)
]

overpaid_unique_ids = overpaid_invoices[
    ~overpaid_invoices["invoice_id"].isin(repeated_invoice_ids)
]

print(
    "Overpaid records linked to repeated invoice IDs:",
    len(overpaid_repeated_ids)
)

print(
    "Distinct repeated invoice IDs flagged as overpaid:",
    overpaid_repeated_ids["invoice_id"].nunique()
)

print(
    "Overpaid records linked to non-repeated invoice IDs:",
    len(overpaid_unique_ids)
)



invoice_payment_status_check = invoice_payment_check[
    ["invoice_id", "payment_status", "grand_total", "total_paid"]
]

print(
    invoice_payment_status_check.groupby("payment_status")[
        "total_paid"
    ].agg(["count", "sum", "mean"]).round(2)
)



unpaid_with_payments = invoice_payment_check[
    (invoice_payment_check["payment_status"] == "Unpaid")
    & (invoice_payment_check["total_paid"] > 0)
]

print(
    "Unpaid invoices with recorded payments:",
    len(unpaid_with_payments)
)

print(
    "Distinct invoice IDs in this group:",
    unpaid_with_payments["invoice_id"].nunique()
)

print(
    unpaid_with_payments[
        ["invoice_id", "so_id", "grand_total", "total_paid"]
    ].head(10).to_string(index=False)
)



print(
    "Unpaid invoices with payments that have repeated IDs:",
    unpaid_with_payments["invoice_id"]
    .isin(repeated_invoice_ids)
    .sum()
)

print(
    "Unpaid invoices with payments that have unique IDs:",
    (~unpaid_with_payments["invoice_id"]
      .isin(repeated_invoice_ids))
    .sum()
)




payment_date_check = payments.merge(
    invoices[["invoice_id", "invoice_date"]],
    on="invoice_id",
    how="left"
)

print(
    "Payments dated before invoice date:",
    (
        payment_date_check["payment_date"]
        < payment_date_check["invoice_date"]
    ).sum()
)





payment_date_check["repeated_invoice_id"] = (
    payment_date_check["invoice_id"].isin(repeated_invoice_ids)
)

print(
    "Date comparisons before invoice date, repeated IDs:",
    (
        (payment_date_check["payment_date"]
         < payment_date_check["invoice_date"])
        & payment_date_check["repeated_invoice_id"]
    ).sum()
)

print(
    "Date comparisons before invoice date, unique IDs:",
    (
        (payment_date_check["payment_date"]
         < payment_date_check["invoice_date"])
        & ~payment_date_check["repeated_invoice_id"]
    ).sum()
)
