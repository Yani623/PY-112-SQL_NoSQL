-- 14. The SEC wants you to send them a report of all trades done by the following customer accounts:
-- CU-94677950
-- CU-26735586
-- CU-04842147
-- CU-52277499
-- For the calendar year 2016 and 2017
-- The report should be written to disk and contain:
-- acct_num, last name, first name, security, trade date, lot size, current price on that day
-- The report should be in date order by security symbol
-- File name 'Suspicious_activity_YYYYMMDD.csv'

Select * from cust_accounts;
Select * from cust_transactions;
select * from security_master;


Select ca.acct_num, ca.last_name, ca.first_name, ct.sec_symbol, ct.trade_date, ct.trade_type, ct.trade_lot, ct.transaction_id, sm.closing_price
from cust_accounts ca
Inner Join cust_transactions ct
on ca.acct_num = ct.acct_num
Inner Join security_master sm
on ct.trade_date = sm.trade_date and ct.sec_symbol = sm.sec_symbol
Where (ca.acct_num = 'CU-94677950' or ca.acct_num = 'CU-26735586' or ca.acct_num = 'CU-04842147' or ca.acct_num = 'CU-52277499') 
and (ct.trade_date between '2016-01-01' and '2017-12-31')
order by ct.sec_symbol and ct.trade_date;

-- Creating CSV With Query:
Select ca.acct_num, ca.last_name, ca.first_name, ct.sec_symbol, ct.trade_date, ct.trade_type, ct.trade_lot, ct.transaction_id, sm.closing_price
from cust_accounts ca
Inner Join cust_transactions ct
on ca.acct_num = ct.acct_num
Inner Join security_master sm
on ct.trade_date = sm.trade_date and ct.sec_symbol = sm.sec_symbol
Where (ca.acct_num = 'CU-94677950' or ca.acct_num = 'CU-26735586' or ca.acct_num = 'CU-04842147' or ca.acct_num = 'CU-52277499') 
and (ct.trade_date between '2016-01-01' and '2017-12-31')
order by ct.sec_symbol and ct.trade_date
Into Outfile '/Users/yani/Desktop/PY-112-MySQL/Final Project/Suspicious_activity_20210720.csv'
Fields Enclosed By ';'
Escaped By '"'
Lines Terminated By '\r\n';

show variables like '--secure-file-priv';