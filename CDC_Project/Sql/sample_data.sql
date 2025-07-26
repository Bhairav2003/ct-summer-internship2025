CREATE DATABASE Retail_DB;
use Retail_DB;

-- 1. Customer Table
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    name NVARCHAR(100),
    address NVARCHAR(255),
    email NVARCHAR(100),
    phone NVARCHAR(15),
    last_modified DATETIME DEFAULT GETDATE()
);

-- 2. Product Table
CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name NVARCHAR(100),
    description NVARCHAR(255),
    price DECIMAL(10, 2),
    category NVARCHAR(50),
    last_modified DATETIME DEFAULT GETDATE()
);

-- 3. Order Table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    order_date DATETIME,
    total_amount DECIMAL(10, 2),
    last_modified DATETIME DEFAULT GETDATE()
);

-- 4. Inventory Table
CREATE TABLE Inventory (
    inventory_id INT PRIMARY KEY,
    product_id INT,
    quantity INT,
    location NVARCHAR(100),
    last_modified DATETIME DEFAULT GETDATE()
);




