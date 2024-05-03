-- May 3, 2024
-- Status: Complete
-- Notes: 

SELECT Product.product_name, Sales.year, Sales.price
FROM Sales
JOIN Product ON Sales.product_id = Product.product_id
  

-- SELECT Product.product_name, Sales.year, Sales.price
-- FROM Sales
-- LEFT JOIN Product ON Sales.product_id = Product.product_id

