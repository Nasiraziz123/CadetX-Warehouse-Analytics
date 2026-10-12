# Initial Data Dictionary — Week 1

## 1. Purpose

This document describes the initial structure of the datasets used in the Heavy Supplier, Inventory & Warehouse Analytics project. It records table names, their purposes, important fields, and observed relationships.

The dictionary is preliminary because the official field documentation was not available during the initial assessment. Field meanings should be confirmed with the project team where necessary.

## 2. Dataset Overview

| Table | Observed purpose | Important fields |
|---|---|---|
| `branches` | Branch and warehouse information | `branch_id`, `branch_name`, `warehouse_capacity`, `monthly_operational_cost` |
| `customers` | Customer information and purchasing history | `customer_id`, `customer_type`, `branch_id`, `credit_limit`, `current_balance` |
| `products` | Product details, pricing, and stock thresholds | `product_id`, `category`, `unit_cost`, `unit_price`, `reorder_level`, `safety_stock` |
| `suppliers` | Supplier information and performance-related attributes | `supplier_id`, `supplier_type`, `lead_time_days`, `reliability_score` |
| `inventory_master` | Product-level stock information for each branch | `product_id`, `branch_id`, `current_stock`, `max_stock`, `warehouse_bin` |
| `purchase_orders_header` | Purchase order summary information | `po_id`, `supplier_id`, `branch_id`, `order_date`, `po_status`, `grand_total` |
| `purchase_orders_lines` | Individual products and quantities within purchase orders | `po_id`, `line_number`, `product_id`, `quantity`, `unit_cost`, `line_grand_total` |
| `sales_orders_header` | Sales order summary information | `so_id`, `customer_id`, `branch_id`, `order_date`, `order_status`, `grand_total` |
| `sales_orders_lines` | Individual products and quantities within sales orders | `so_id`, `line_number`, `product_id`, `quantity`, `unit_price`, `line_grand_total` |
| `stock_ledger` | Inventory movement history | `movement_id`, `product_id`, `branch_id`, `movement_type`, `quantity`, `running_balance` |
| `invoices` | Invoice amounts, due dates, and payment status | `invoice_id`, `so_id`, `customer_id`, `grand_total`, `payment_status` |
| `payments` | Payment transactions | `payment_id`, `invoice_id`, `payment_date`, `payment_amount`, `payment_method` |

## 3. Key Fields and Relationships

| Field or key | Table | Initial interpretation |
|---|---|---|
| `branch_id` | `branches` | Identifier for a branch |
| `customer_id` | `customers` | Identifier for a customer |
| `product_id` | `products` | Identifier for a product |
| `supplier_id` | `suppliers` | Identifier for a supplier |
| `po_id` | `purchase_orders_header` | Identifier for a purchase order |
| `so_id` | `sales_orders_header` | Identifier for a sales order |
| `movement_id` | `stock_ledger` | Identifier for a stock movement |
| `invoice_id` | `invoices` | Intended invoice identifier; repeated values were observed |
| `payment_id` | `payments` | Intended payment identifier; repeated values were observed |

Initial relationship checks found:

- Customers reference valid branch IDs.
- Inventory records reference valid product and branch IDs.
- Purchase orders reference valid suppliers and branches.
- Purchase order lines reference valid purchase orders and products.
- Sales orders reference valid customers and branches.
- Sales order lines reference valid sales orders and products.
- Stock ledger movements reference valid products and branches; tested purchase order and sales order references were valid.
- Invoices reference valid sales orders, customers, and branches.
- Payments reference invoice IDs present in the invoice table.

These findings describe the checks performed; they do not establish that every relationship has been fully validated against official business rules.

## 4. Important Data Fields

### Inventory and stock

- `opening_stock`: Stock quantity recorded at opening.
- `current_stock`: Current stock quantity recorded in the inventory master.
- `reorder_level`: Recorded stock threshold for reordering.
- `safety_stock`: Recorded buffer-stock threshold.
- `max_stock` / `max_stock_level`: Recorded maximum stock threshold.

**Open question:** All 180 inventory master records had `current_stock` greater than `max_stock`. The meaning, units, and relationship between these fields require confirmation.

### Purchasing and sales

- `quantity`: Quantity recorded on an order line.
- `unit_cost`: Cost per unit on a purchase order line.
- `unit_price`: Price per unit on a sales order line.
- `line_total`: Line amount before GST, based on the tested calculations.
- `gst_rate`: GST percentage recorded for a line.
- `gst_amount`: GST amount recorded for a line.
- `line_grand_total`: Line amount including GST.

### Supplier information

- `lead_time_days`: Recorded supplier lead-time value.
- `reliability_score`: Supplier reliability score; its scale and definition need confirmation.
- `import_duty_rate`: Recorded import-duty rate; its exact unit and calculation rules need confirmation.

### Invoices and payments

- `grand_total`: Recorded total including the GST amount in the tested order and invoice tables.
- `payment_status`: Recorded invoice payment-status category.
- `payment_amount`: Amount recorded for a payment transaction.

Repeated invoice and payment identifiers require investigation before definitive payment reconciliation.

## 5. Data Types and Preparation Notes

The initial profiling identified the following preparation considerations:

- Date fields should be parsed consistently as dates.
- Warehouse capacity values include text units such as `sqft`.
- Product dimensions are stored as text, for example `40x25x25`.
- Postal codes and tax identifiers should be treated carefully because they function as identifiers rather than quantities.
- The meaning and permitted values of categorical fields should be confirmed before standardization.

No transformations should be made solely on the basis of these observations. Decisions should be documented and supported by the data definitions or business requirements.

## 6. Limitations

- Official field documentation was not available during the initial assessment.
- Some field meanings and business rules remain unconfirmed.
- Repeated invoice and payment identifiers may affect joins and financial reconciliation.
- Stock-ledger balance validation depends on the correct transaction sequence and adjustment rules.

## 7. Next Steps

1. Obtain or confirm the official field definitions.
2. Investigate inventory stock values exceeding maximum stock thresholds.
3. Investigate repeated invoice and payment identifiers.
4. Confirm stock-ledger transaction ordering and adjustment rules.
5. Finalize the data dictionary after the definitions and business rules have been verified.