Select c.customer_id,c.customer_name from customers c where 
c.customer_id in 
(Select customer_id from orders where product_name = 'A')
and 
c.customer_id in 
(Select customer_id from orders where product_name = 'B')
and 
c.customer_id not in 
(Select customer_id from orders where product_name = 'C')
order by c.customer_name
