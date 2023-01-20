
CREATE SCHEMA "TPCH";
--
--drop table customer;
CREATE TABLE "TPCH"."CUSTOMER"(
	C_CUSTKEY bigint NOT NULL,
	C_NAME varchar(25) NOT NULL,
	C_ADDRESS varchar(40) NOT NULL,
	C_NATIONKEY int NOT NULL,
	C_PHONE char(15) NOT NULL,
	C_ACCTBAL decimal(12, 2) NOT NULL,
	C_MKTSEGMENT char(10) NOT NULL,
	C_COMMENT varchar(118) NOT NULL
); 

--drop table lineitem;
CREATE TABLE "TPCH"."LINEITEM"(
	L_ORDERKEY bigint NOT NULL,
	L_PARTKEY bigint NOT NULL,
	L_SUPPKEY int NOT NULL,
	L_LINENUMBER int NOT NULL,
	L_QUANTITY decimal(12, 2) NOT NULL,
	L_EXTENDEDPRICE decimal(12, 2) NOT NULL,
	L_DISCOUNT decimal(12, 2) NOT NULL,
	L_TAX decimal(12, 2) NOT NULL,
	L_RETURNFLAG char(1) NOT NULL,
	L_LINESTATUS char(1) NOT NULL,
	L_SHIPDATE date NOT NULL,
	L_COMMITDATE date NOT NULL,
	L_RECEIPTDATE date NOT NULL,
	L_SHIPINSTRUCT char(25) NOT NULL,
	L_SHIPMODE char(10) NOT NULL,
	L_COMMENT varchar(44) NOT NULL
)
partition by hash(L_ORDERKEY) partitions 8
;

--drop table nation;
CREATE TABLE "TPCH"."NATION"(
	N_NATIONKEY int NOT NULL,
	N_NAME char(25) NOT NULL,
	N_REGIONKEY int NOT NULL,
	N_COMMENT varchar(152) NOT NULL
);

--drop table ORDERS;
CREATE TABLE "TPCH"."ORDERS"(
	O_ORDERKEY bigint NOT NULL,
	O_CUSTKEY bigint NOT NULL,
	O_ORDERSTATUS char(1) NOT NULL,
	O_TOTALPRICE decimal(12, 2) NOT NULL,
	O_ORDERDATE date NOT NULL,
	O_ORDERPRIORITY char(15) NOT NULL,
	O_CLERK char(15) NOT NULL,
	O_SHIPPRIORITY int NOT NULL,
	O_COMMENT varchar(79) NOT NULL
);

--drop table part;
CREATE TABLE "TPCH"."PART"(
	P_PARTKEY bigint NOT NULL,
	P_NAME varchar(55) NOT NULL,
	P_MFGR char(25) NOT NULL,
	P_BRAND char(10) NOT NULL,
	P_TYPE varchar(25) NOT NULL,
	P_SIZE int NOT NULL,
	P_CONTAINER char(10) NOT NULL,
	P_RETAILPRICE decimal(12, 2) NOT NULL,
	P_COMMENT varchar(23) NOT NULL
);

--drop table partsupp;
CREATE TABLE "TPCH"."PARTSUPP"(
	PS_PARTKEY bigint NOT NULL,
	PS_SUPPKEY int NOT NULL,
	PS_AVAILQTY int NOT NULL,
	PS_SUPPLYCOST decimal(12, 2) NOT NULL,
	PS_COMMENT varchar(199) NOT NULL
);


--drop table region;
CREATE TABLE "TPCH"."REGION"(
	R_REGIONKEY int NOT NULL,
	R_NAME char(25) NOT NULL,
	R_COMMENT varchar(152) NOT NULL
);

--drop table "TPCH"."SUPPLIER";
CREATE TABLE "TPCH"."SUPPLIER"(
	S_SUPPKEY int NOT NULL,
	S_NAME char(25) NOT NULL,
	S_ADDRESS varchar(40) ,
	S_NATIONKEY int NOT NULL,
	S_PHONE char(15) NOT NULL,
	S_ACCTBAL decimal(12, 2) NOT NULL,
	S_COMMENT varchar(102) NOT NULL
);


select count(*) from "TPCH"."SUPPLIER";
select count(*) from "TPCH"."SUPPLIER_DRAM";
select count(*)  from "TPCH"."CUSTOMER";
select count(*)  from "TPCH"."PARTSUPP";
select count(*)  from "TPCH"."REGION";
select count(*)  from "TPCH"."PART";
select count(*)  from "TPCH"."ORDERS";
select count(*)  from "TPCH"."NATION";
select count(*)  from "TPCH"."LINEITEM";

ALTER TABLE "TPCH"."SUPPLIER_DRAM" PERSISTENT MEMORY OFF IMMEDIATE CASCADE;



