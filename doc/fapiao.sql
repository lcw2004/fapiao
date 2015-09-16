drop table tbl_baseinfo;

drop table tbl_custom;

drop table tbl_dict;

drop table tbl_invoice;

drop table tbl_invoice_detail;

drop table tbl_product;

create table tbl_baseinfo (
ID                   INTEGER,
company_name         TEXT,
people_num           TEXT,
addr_tell            TEXT,
bank_no              TEXT
);

create table tbl_custom (
ID                   INTEGER,
code                 TEXT,
name                 TEXT,
tax_id               TEXT,
addr                 TEXT,
bank_account         TEXT,
business_tax_di      TEXT,
erp_id               TEXT,
summary_title        TEXT
);

create table tbl_dict (
ID                   INTEGER                        not null,
label                TEXT,
value                TEXT,
type                 TEXT,
describe             TEXT,
status               INTEGER,
oindex               INTEGER,
primary key (ID)
);

create table tbl_invoice (
id                   INTEGER                        not null,
invoice_num          TEXT,
custom_id            TEXT,
remark               TEXT,
start_time           TEXT,
total_not_tax        TEXT,
total_tax            TEXT,
total_num            TEXT,
serial_number        TEXT,
drawer               TEXT,
beneficiary          TEXT,
reviewer             TEXT,
status               INTEGER,
primary key (id)
);

create table tbl_invoice_detail (
ID                   INTEGER                        not null,
pro_code             TEXT,
pro_name             TEXT,
pro_type             TEXT,
pro_unit             TEXT,
pro_unit_price       TEXT,
pro_num              TEXT,
tax_price            TEXT,
tax_rate             TEXT,
tax                  TEXT,
invoice_Id           INTEGER,
primary key (ID),
foreign key (invoice_Id)
      references tbl_invoice (id)
);

create table tbl_product (
ID                   INTEGER                        not null,
name                 TEXT,
code                 TEXT,
type                 TEXT,
unit_price           TEXT,
tax_price            TEXT,
tax                  TEXT,
business_tax_num     TEXT,
erp_id               TEXT,
col1                 TEXT,
col2                 TEXT,
col3                 TEXT,
col4                 TEXT,
primary key (ID)
);

