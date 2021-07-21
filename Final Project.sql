SELECT * FROM corp_accounts;
select * from corp_transactions;

-- 11. Write a query to report by account number the total number of buys, sells, and shares traded per security (For both customer and corporate accounts - 2 SQL queries)

-- # of Buys for each security
select acct_num, sec_symbol, count(trade_type) As '# of Buys'
from corp_transactions
where trade_type = 'BUY'
group by sec_symbol, acct_num
order by acct_num;


-- # of Sells for each security
select acct_num, sec_symbol, count(trade_type) As '# of Sells', sum(trade_lot) As 'Shares Traded'
from corp_transactions
where trade_type = 'SELL'
group by sec_symbol, acct_num;

-- Shares Traded
select sec_symbol, count(trade_lot) As 'Shares Traded'
from corp_transactions
group by sec_symbol;


select * from corp_transactions;
select acct_num, sec_symbol, count(trade_type) As '# of Buys', '# of Sells', 'Shares Traded'
	from 
		(select acct_num, sec_symbol, count(trade_type) As '# of Sells', sum(trade_lot) As 'Shares Traded'
		from corp_transactions
		where trade_type = 'SELL')as x
Where trade_type = 'Buy'
Group By sec_symbol, acct_num
order by acct_num;
