CREATE TABLE IF NOT EXISTS students(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	age INTEGER,
	city TEXT
);

INSERT INTO students
(name, age, city)
VALUES
('Ali', 20, 'Tashkent'),
('Vali', 22, 'Samarkand'),
('Hasan', 21, 'Bukhara');


CREATE TABLE IF NOT EXISTS courses(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT,
	student_id INTEGER,
	price INTEGER
);

INSERT INTO courses
(title, student_id, price)
VALUES
('Python', 1, 100),
('SQL', 2, 80),
('Django', 1, 120);

CREATE TABLE IF NOT EXISTS customers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	phone INTEGER,
	city TEXT
);

INSERT INTO customers
(name, phone, city)
VALUES
('Aziz', 99890123, 'Tashkent'),
('Lola', 99890777, 'Namangan'),
('Sardor', 99890999, 'Fargana');


CREATE TABLE IF NOT EXISTS orders(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product TEXT,
	customer_id INTEGER,
	amount INTEGER
);

INSERT INTO orders
(product, customer_id, amount)
VALUES
('Laptop', 1, 1200),
('Phone', 2, 500),
('Tablet', 1, 700);


CREATE TABLE IF NOT EXISTS teachers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT,
	subject TEXT,
	experience INTEGER
);

INSERT INTO teachers
(name, subject, experience)
VALUES
('Kamol', 'Math', 5),
('Dilnoza', 'English', 3),
('Bekzod', 'Physics', 7);

