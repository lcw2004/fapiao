DROP TABLE tbl_baseinfo;

DROP TABLE tbl_custom;

DROP TABLE tbl_dict;

DROP TABLE tbl_invoice;

DROP TABLE tbl_invoice_detail;

DROP TABLE tbl_product;

CREATE TABLE tbl_baseinfo (
  id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  company_name TEXT,
  people_num   TEXT,
  addr_tell    TEXT,
  bank_no      TEXT
);

CREATE TABLE tbl_custom (
  id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  code            TEXT,
  name            TEXT,
  tax_id          TEXT,
  addr            TEXT,
  bank_account    TEXT,
  business_tax_di TEXT,
  erp_id          TEXT,
  summary_title   TEXT
);

CREATE TABLE tbl_dict (
  id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  label    TEXT,
  value    TEXT,
  type     TEXT,
  describe TEXT,
  status   INTEGER,
  oindex   INTEGER
);

CREATE TABLE tbl_invoice (
  id            INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  invoice_num   TEXT,
  custom_id     TEXT,
  remark        TEXT,
  start_time    TEXT,
  total_not_tax TEXT,
  total_tax     TEXT,
  total_num     TEXT,
  serial_number TEXT,
  drawer        TEXT,
  beneficiary   TEXT,
  reviewer      TEXT,
  status        INTEGER
);

CREATE TABLE tbl_invoice_detail (
  id             INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  pro_code       TEXT,
  pro_name       TEXT,
  pro_type       TEXT,
  pro_unit       TEXT,
  pro_unit_price TEXT,
  pro_num        TEXT,
  tax_price      TEXT,
  tax_rate       TEXT,
  tax            TEXT,
  invoice_Id     INTEGER,
  FOREIGN KEY (invoice_Id)
  REFERENCES tbl_invoice (id)
);

CREATE TABLE tbl_product (
  id               INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name             TEXT,
  code             TEXT,
  type             TEXT,
  unit_price       TEXT,
  tax_price        TEXT,
  tax              TEXT,
  business_tax_num TEXT,
  erp_id           TEXT,
  col1             TEXT,
  col2             TEXT,
  col3             TEXT,
  col4             TEXT
);

