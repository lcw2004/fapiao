drop table ��Ʊ��Ϣ��;

drop table ��Ʊ��ϸ��Ϣ��;

drop table ��Ʒ��Ϣ;

drop table ������Ϣ��;

drop table �ͻ����ϱ�;

drop table �����ֵ��;

create table ��Ʊ��Ϣ�� (
ID                   CHAR(10)                       not null,
��Ʊ����                 CHAR(10),
�ͻ�ID                 CHAR(10),
��ע                   CHAR(10),
��Ʊ����                 CHAR(10),
�ܲ���˰���               CHAR(10),
��˰��                  CHAR(10),
��˰�ϼ�                 CHAR(10),
ϵͳ��ˮ��                CHAR(10),
��Ʊ��                  CHAR(10),
�տ���                  CHAR(10),
������                  CHAR(10),
��Ʊ������־               CHAR(10),
primary key (ID)
);

create table ��Ʊ��ϸ��Ϣ�� (
ID                   CHAR(10)                       not null,
��Ʒ����                 CHAR(10),
��Ʒ����                 CHAR(10),
��Ʒ�ͺ�                 CHAR(10),
��Ʒ��λ                 CHAR(10),
��Ʒ����                 CHAR(10),
��Ʒ����                 CHAR(10),
��˰����                 CHAR(10),
˰��                   CHAR(10),
˰��                   CHAR(10),
��ƱID                 CHAR(10),
primary key (ID),
foreign key (��ƱID)
      references ��Ʊ��Ϣ�� (ID)
);

create table ��Ʒ��Ϣ (
��Ʒ����                 CHAR(10),
��Ʒ����                 CHAR(10),
��Ʒ�ͺ�                 CHAR(10),
��Ʒ����                 CHAR(10),
��˰����                 CHAR(10),
˰��                   CHAR(10),
��ҵ˰��                 CHAR(10),
ERA����ֵ               CHAR(10),
�����ֶ�1                CHAR(10),
�����ֶ�2                CHAR(10),
�����ֶ�3                CHAR(10),
�����ֶ�4                CHAR(10)
);

create table ������Ϣ�� (
��˾����                 CHAR(10),
��˰��ʶ���               CHAR(10),
��ַ�绰                 CHAR(10),
�������˺�                CHAR(10)
);

create table �ͻ����ϱ� (
�ͻ�����                 CHAR(10),
�ͻ�����                 CHAR(10),
�ͻ�˰��                 CHAR(10),
�ͻ���ַ                 CHAR(10),
���������˺�               CHAR(10),
��ҵ˰��                 CHAR(10),
ERP����ֵ               CHAR(10),
��Ʊ��������               CHAR(10)
);

create table �����ֵ�� (
ID                   CHAR(10),
label                CHAR(10),
value                CHAR(10),
type                 CHAR(10),
"desc"               CHAR(10),
status               CHAR(10)
);

