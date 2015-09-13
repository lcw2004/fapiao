drop table 发票信息表;

drop table 发票详细信息表;

drop table 商品信息;

drop table 基础信息表;

drop table 客户资料表;

drop table 数据字典表;

create table 发票信息表 (
ID                   CHAR(10)                       not null,
发票号码                 CHAR(10),
客户ID                 CHAR(10),
备注                   CHAR(10),
开票日期                 CHAR(10),
总不含税金额               CHAR(10),
总税额                  CHAR(10),
价税合计                 CHAR(10),
系统流水号                CHAR(10),
开票人                  CHAR(10),
收款人                  CHAR(10),
复核人                  CHAR(10),
发票产生标志               CHAR(10),
primary key (ID)
);

create table 发票详细信息表 (
ID                   CHAR(10)                       not null,
产品代码                 CHAR(10),
产品名称                 CHAR(10),
产品型号                 CHAR(10),
产品单位                 CHAR(10),
产品单价                 CHAR(10),
产品数量                 CHAR(10),
含税单价                 CHAR(10),
税率                   CHAR(10),
税额                   CHAR(10),
发票ID                 CHAR(10),
primary key (ID),
foreign key (发票ID)
      references 发票信息表 (ID)
);

create table 商品信息 (
产品名称                 CHAR(10),
产品代码                 CHAR(10),
产品型号                 CHAR(10),
产品单价                 CHAR(10),
含税单价                 CHAR(10),
税率                   CHAR(10),
企业税号                 CHAR(10),
ERA对照值               CHAR(10),
备用字段1                CHAR(10),
备用字段2                CHAR(10),
备用字段3                CHAR(10),
备用字段4                CHAR(10)
);

create table 基础信息表 (
公司名称                 CHAR(10),
纳税人识别号               CHAR(10),
地址电话                 CHAR(10),
开户行账号                CHAR(10)
);

create table 客户资料表 (
客户代码                 CHAR(10),
客户名称                 CHAR(10),
客户税号                 CHAR(10),
客户地址                 CHAR(10),
开户银行账号               CHAR(10),
企业税号                 CHAR(10),
ERP对照值               CHAR(10),
开票汇总名称               CHAR(10)
);

create table 数据字典表 (
ID                   CHAR(10),
label                CHAR(10),
value                CHAR(10),
type                 CHAR(10),
"desc"               CHAR(10),
status               CHAR(10)
);

