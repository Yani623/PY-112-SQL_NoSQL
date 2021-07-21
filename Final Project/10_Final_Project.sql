-- 10. Calculate the Profit and Loss (PnL) for every trade in the customer accounts and corp accounts (2 SQL queries) by security by buy/sell.

select * from cust_transactions
;
select * from security_master; 

-- Determine price on transaction date for each transaction:
Select c.trade_date, c.sec_symbol, s.closing_price, c.transaction_id
From cust_transactions as c
Inner Join security_master as s
On c.sec_symbol = s.sec_symbol
Where (c.trade_date = s.trade_date) and (c.sec_symbol = s.sec_symbol) 
order by c.trade_date ASC;


Select c.sec_symbol, c.acct_num, c.trade_type, c.transaction_id, s.closing_price
From corp_transactions as c
Inner Join security_master as s
On c.sec_symbol = s.sec_symbol
Where (c.trade_type = 'Buy') and (c.trade_date = s.trade_date) and (c.sec_symbol = s.sec_symbol) 
order by c.acct_num;

Select c.acct_num As 'Account Number', c.sec_symbol As 'Security', c.trade_date As 'Trade Date', (select c.trade_type Where c.trade_type = 'Buy')As 'Trade Type', c.transaction_id As 'Transaction ID', s.closing_price As 'Purchase Price'
From corp_transactions as c
Inner Join security_master as s
On c.sec_symbol = s.sec_symbol
Where (c.trade_date = s.trade_date) and (c.sec_symbol = s.sec_symbol) and (c.trade_date between '2016-07-18' and '2018-05-24')
order by c.acct_num;


-- Trying Union:
Select c.acct_num As 'Account Number', c.sec_symbol As 'Security', c.trade_date As 'Trade Date', (select c.trade_type Where c.trade_type = 'Buy')As 'Trade Type', c.transaction_id As 'Transaction ID', s.closing_price As 'Purchase Price',

c.trade_date As 'Trade Date', (select c.trade_type Where c.trade_type = 'Buy')As 'Trade Type', c.transaction_id As 'Transaction ID', s.closing_price As 'Purchase Price';

-- Trying in one row without repeating info
Select c.acct_num As 'Account Number',
c.sec_symbol As 'Security', 
(select c.trade_date where c.trade_type = 'Buy')As 'Purchase Date', 
s.closing_price As 'Purchase Price',
(select s.trade_date where c.trade_type = 'Sell')As 'Sale Date',
c.transaction_id As Purchase_Transaction_ID
From corp_transactions as c
Inner Join security_master as s
On c.sec_symbol = s.sec_symbol
Where (c.sec_symbol = s.sec_symbol) and (c.trade_date between '2016-07-18' and '2018-05-24')
order by c.acct_num; 


