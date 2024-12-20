CREATE TABLE company_types (
	id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name varchar(3)
);

CREATE TABLE suppliers (
	id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	type_id int NOT NULL REFERENCES company_types(id),
	name varchar(250) NOT NULL,
	inn varchar(12) NOT NULL,
	quality_rating int,
	supply_start_date date
);

CREATE TABLE material_types (
	id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name varchar(20)
);

CREATE TABLE units (
	id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name varchar(20)
);

CREATE TABLE materials (
	id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name varchar(50) NOT NULL,
	type_id int NOT NULL REFERENCES material_types(id),
	image varchar(255),
	price numeric,
	inventory int,
	min_amount int,
	package_amount int,
	unit_id int REFERENCES units(id)
);

CREATE TABLE materials_suppliers (
	material_id bigint NOT NULL REFERENCES materials(id),
	supplier_id bigint NOT NULL REFERENCES suppliers(id),
	UNIQUE (material_id, supplier_id)
);