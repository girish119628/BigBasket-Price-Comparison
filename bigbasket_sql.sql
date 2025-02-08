-- Analysis of Price, Discount, and Category
use code_it;
CREATE TABLE bigbasket_cln (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Product_Name VARCHAR(255),
    Price FLOAT,
    Discount FLOAT,
    Category VARCHAR(100)
);

-- Average Price by Category 
SELECT Category, round(AVG(Price), 2) AS Average_price
FROM bigbasket_cln
GROUP BY Category
order by Average_price desc;

-- Highest price by Category
SELECT Category, Max(Price) AS Highest_price
FROM bigbasket_cln
GROUP BY Category
order by Highest_price desc;

-- Lowest price by category
select Category, MIN(Price) as Lowest_price
from bigbasket_cln 
group by Category
order by Lowest_price;

-- Average discount by category
SELECT Category, round(AVG(Discount), 2) AS Average_discount
FROM bigbasket_cln
GROUP BY Category
order by Average_discount desc;

-- Highest discount by category
SELECT Category, Max(Discount) AS Highest_discount
FROM bigbasket_cln
GROUP BY Category
order by Highest_discount desc;

select * from bigbasket_cln;

-- Count the products in each category
SELECT Category, count(*) Total_products
from bigbasket_cln
group by Category
order by Total_products desc;

-- Top 10 most expensive Product
SELECT distinct(Product_Name), Price
from bigbasket_cln
order by price desc
limit 10;

-- Top 10 most discounted Product
SELECT distinct(Product_Name), Discount
from bigbasket_cln
order by Discount desc
limit 10;  

-- Top 3 most expensive Product in each Category
SELECT Product_Name, Category, Price
from (select distinct(Product_Name), Category, Price,
RANK() OVER (partition by Category ORDER BY Price desc) as rnk
from bigbasket_cln) ranked
where rnk <= 3;

-- Top 3 most discounted Product in each Category
SELECT Product_Name, Category, Discount
from (select distinct(Product_Name), Category, Discount,
RANK() OVER (partition by Category ORDER BY Price desc) as rnk
from bigbasket_cln) ranked
where rnk <= 3;