-- 13. MSFT was on the restricted list for the corporate client Ether Trading from 1/1/2017 through 12/31/2017.
-- Please list all trades for this client during this period and classify the restricted trades as 'ILLEGAL'


SELECT * FROM sql_final_project.corp_transactions;

Select ca.acct_name, ct.acct_num, ct.trade_date, ct.sec_symbol, ct.trade_type As 'Illegal Trades'
From corp_transactions ct
Inner Join corp_accounts ca
On ct.acct_num = ca.acct_num
Where ca.acct_name = 'ether trading' and ct.sec_symbol = 'MSFT' and trade_date between '2017-01-01' and '2017-12-31';


Select (count(*) * '10000') As 'Total Fine' 
from corp_transactions ct
Inner Join corp_accounts ca
On ct.acct_num = ca.acct_num
Where ca.acct_name = 'ether trading' and ct.sec_symbol = 'MSFT' and trade_date between '2017-01-01' and '2017-12-31';