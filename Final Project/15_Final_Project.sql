SELECT * FROM sql_final_project.cust_transactions;

Select acct_num, transaction_id,
(select trade_date where trade_type = 'Buy') As 'Purchase Date',
(select trade_date where trade_type = 'Sell') As 'Sale Date',
('Sale Date' - 'Purchase Date') As 'Total Days Held'
From cust_transactions
Group by transaction_id, acct_num;


Select a.acct_num,
a.transaction_id,
a.sec_symbol,
a.trade_date As Purchase_Date,
b.trade_date As Sale_Date,
datediff(b.trade_date, a.trade_date) As Total_Days_Held
From cust_transactions a
Left Join cust_transactions b
On a.sec_symbol = b.sec_symbol and a.transaction_id = b.transaction_id and b.trade_type = 'Sell'
Where a.trade_type = 'Buy'
Limit 10;


From cust_transactions
Group by transaction_id, acct_num;