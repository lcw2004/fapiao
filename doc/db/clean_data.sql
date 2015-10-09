DELETE FROM tbl_invoice_detail;
DELETE FROM tbl_invoice;
DELETE FROM tbl_custom;



SELECT sum(not_tax_price), sum(tax_price), sum(contain_tax_price) FROM tbl_invoice_detail WHERE invoice_id = 1;

SELECT not_tax_price, tax_price, contain_tax_price FROM tbl_invoice_detail WHERE invoice_id = 1;

UPDATE tbl_invoice set total_not_tax, total_tax, total_num
	SELECT sum(not_tax_price), sum(tax_price), sum(contain_tax_price) FROM tbl_invoice_detail WHERE  tbl_invoice_detail.invoice_Id = tbl_invoice.id
WHERE tbl_invoice.id = 1

UPDATE tbl_invoice set
  total_not_tax = (SELECT sum(not_tax_price) FROM tbl_invoice_detail where tbl_invoice_detail.invoice_Id = tbl_invoice.id),
  total_tax = (SELECT sum(tax_price) FROM tbl_invoice_detail where tbl_invoice_detail.invoice_Id = tbl_invoice.id),
  total_num = (SELECT sum(contain_tax_price) FROM tbl_invoice_detail where tbl_invoice_detail.invoice_Id = tbl_invoice.id)
where tbl_invoice.id = 1;
