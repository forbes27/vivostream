CREATE TABLE departments (
    	id int NOT NULL,
	name varchar(200) NOT NULL UNIQUE,
	PRIMARY KEY (id)
);
CREATE TABLE roles (
	id  int NOT NULL,
	name varchar NOT NULL UNIQUE,
	description varchar(200) NOT NULL,
	PRIMARY KEY(id)
   );
CREATE TABLE employees (
	id int NOT NULL,
	email varchar NOT NULL,
	username varchar(60) NOT NULL,
	first_name varchar(60) NOT NULL,
	last_name varchar(60) NOT NULL,
	password_hash varchar(128),
	tier varchar(25),
   	department_id int,
	role_id int,
	is_admin boolean,
	FOREIGN KEY (department_id) references departments(id),
	FOREIGN KEY (role_id) references roles(id),
	PRIMARY KEY(id)
);
CREATE UNIQUE INDEX ix_employees_email
ON employees(email);
CREATE INDEX ix_employees_first_name
ON employees(first_name);
CREATE INDEX ix_employees_last_name
ON employees(last_name);
CREATE INDEX ix_employees_username
ON employees(username);

