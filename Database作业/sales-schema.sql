

use sales;

DROP TABLE IF EXISTS purchase_item;
DROP TABLE IF EXISTS purchase;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS staff;
DROP TABLE IF EXISTS customer;

CREATE TABLE customer(
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(25) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(50),
  phone VARCHAR(15) NOT NULL,
  address VARCHAR(50) NOT NULL
);

CREATE TABLE staff(
  id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(25) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  is_active BOOLEAN,
  phone VARCHAR(15) NOT NULL,
  address VARCHAR(50) NOT NULL
);

CREATE TABLE category(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(25) NOT NULL
);

CREATE TABLE product(
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  price FLOAT NOT NULL,
  category_id INT,
  FOREIGN KEY(category_id) REFERENCES category(id)
);

CREATE TABLE purchase(
  id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT NOT NULL,
  status ENUM('Pending', 'Processing', 'Rejected', 'Completed') DEFAULT 'Pending',
  purchase_date DATE NOT NULL,
  staff_id INT NOT NULL,
  FOREIGN KEY(customer_id) REFERENCES customer(id),
  FOREIGN KEY(staff_id) REFERENCES staff(id)
);

CREATE TABLE purchase_item(
  id INT PRIMARY KEY AUTO_INCREMENT,
  purchase_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price FLOAT NOT NULL,
  discount FLOAT,
  FOREIGN KEY(purchase_id) REFERENCES purchase(id),
  FOREIGN KEY(product_id) REFERENCES product(id)
);
