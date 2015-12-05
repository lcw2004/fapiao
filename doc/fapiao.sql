drop table tbl_baseinfo;

drop table tbl_custom;

drop table tbl_dict;

drop table tbl_invoice;

drop table tbl_invoice_detail;

drop table tbl_product;

drop table tbl_user;

create table tbl_baseinfo (
id                   INTEGER                        not null,
company_name         TEXT,
people_num           TEXT,
addr_tell            TEXT,
bank_no              TEXT,
primary key (id)
);

create table tbl_custom (
id                   INTEGER                        not null,
code                 TEXT,
name                 TEXT,
tax_id               TEXT,
addr                 TEXT,
bank_account         TEXT,
business_tax_id      TEXT,
erp_id               TEXT,
summary_title        TEXT,
remark               TEXT,
status               INTEGER,
primary key (id)
);

create table tbl_dict (
id                   INTEGER                        not null,
label                TEXT,
value                TEXT,
type                 TEXT,
describe             TEXT,
status               INTEGER,
oindex               INTEGER,
primary key (id)
);

create table tbl_invoice (
id                   INTEGER                        not null,
custom_id            INTEGER,
invoice_num          TEXT,
remark               TEXT,
start_time           TEXT,
total_not_tax        INTEGER,
total_tax            INTEGER,
total_num            INTEGER,
serial_number        TEXT,
drawer               TEXT,
beneficiary          TEXT,
reviewer             TEXT,
status               INTEGER,
primary key (id),
foreign key (custom_id)
      references tbl_custom (id)
);

create table tbl_product (
id                   INTEGER                        not null,
name                 TEXT,
code                 TEXT,
type                 TEXT,
unit                 TEXT,
unit_price           TEXT,
tax_price            TEXT,
tax                  TEXT,
business_tax_num     TEXT,
erp_id               TEXT,
col1                 TEXT,
col2                 TEXT,
col3                 TEXT,
col4                 TEXT,
p_id                 INTEGER,
status               INTEGER,
primary key (id)
);

create table tbl_invoice_detail (
id                   INTEGER                        not null,
pro_num              INTEGER,
not_tax_price        INTEGER,
tax_price            INTEGER,
contain_tax_price    INTEGER,
invoice_Id           INTEGER,
product_id           INTEGER,
primary key (id),
foreign key (invoice_Id)
      references tbl_invoice (id),
foreign key (product_id)
      references tbl_product (id)
);

create table tbl_user (
id                   INTEGER,
name                 TEXT,
login_name           TEXT,
password             TEXT,
status               INTEGER,
is_admin             INTEGER
);

