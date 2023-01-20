#!/usr/local/bin/tclsh8.6
#EDITABLE OPTIONS##################################################
set library tdbc::odbc ;# SQL Server Library
set version 1.1.1 ;# SQL Server Library Version
set total_querysets 1 ;# Number of query sets before logging off
set RAISEERROR "false" ;# Exit script on SQL Server query error (true or false)
set VERBOSE "false" ;# Show query text and output
set maxdop 2 ;# Maximum Degree of Parallelism
set scale_factor 1000 ;#Scale factor of the tpc-h schema
set authentication "sql";# Authentication Mode (WINDOWS or SQL)
set server {<ip_address>};# HANA
set port "<port>";# Microsoft SQL Server Port
set odbc_driver {HDBODBC};# ODBC Driver
set uid "<user>";#User ID for SQL Server Authentication
set pwd "<password>";#Password for SQL Server Authentication
set tcp "true";#Specify TCP Protocol
set azure "false";#Azure Type Connection
set database "<dbname>";# Database containing the TPC Schema
set refresh_on "false" ;#First User does refresh function
set update_sets 1 ;#Number of sets of refresh function to complete
set trickle_refresh 1000 ;#time delay (ms) to trickle refresh function
set REFRESH_VERBOSE "false" ;#report refresh function activity
set cachetext "select /* Cache 1Gb */";#tag for cache size

#EDITABLE OPTIONS##################################################
#LOAD LIBRARIES AND MODULES
if [catch {package require $library $version} message] { error "Failed to load $library - $message" }
if [catch {::tcl::tm::path add modules} ] { error "Failed to find modules directory" }
if [catch {package require tpchcommon} ] { error "Failed to load tpch common functions" } else { namespace import tpchcommon::* }

proc connect_string { server port odbc_driver authentication uid pwd tcp azure db } {
if { $tcp eq "true" } { set server $server:$port }
if {[ string toupper $authentication ] eq "WINDOWS" } {
set connection "DRIVER=$odbc_driver;SERVER=$server;TRUSTED_CONNECTION=YES"
} else {
if {[ string toupper $authentication ] eq "SQL" } {
set connection "DRIVER=$odbc_driver;SERVERNODE=$server;UID=$uid;PWD=$pwd"
        } else {
puts stderr "Error: neither WINDOWS or SQL Authentication has been specified"
set connection "DRIVER=$odbc_driver;SERVER=$server"
        }
}
if { $azure eq "true" } { append connection ";" "DATABASE=$db" }
return $connection
}

proc standsql { odbc sql RAISEERROR } {
if {[ catch {set rows [$odbc allrows $sql ]} message]} {
if { $RAISEERROR } {
error "Query Error :$message"
        } else {
puts "$message"
        }
} else {
return $rows
        }
}
#########################
#TPCH REFRESH PROCEDURE
proc mk_order_ref { odbc upd_num scale_factor trickle_refresh REFRESH_VERBOSE } {
#2.27.2 Refresh Function Definition
#LOOP (SF * 1500) TIMES
#INSERT a new row into the ORDERS table
#LOOP RANDOM(1, 7) TIMES
#INSERT a new row into the LINEITEM table
#END LOOP
#END LOOP
set refresh 100
set delta 1
set L_PKEY_MAX   [ expr {200000 * $scale_factor} ]
set O_CKEY_MAX [ expr {150000 * $scale_factor} ]
set O_ODATE_MAX [ expr {(92001 + 2557 - (121 + 30) - 1)} ]
set sfrows [ expr {$scale_factor * 1500} ]
set startindex [ expr {(($upd_num * $sfrows) - $sfrows) + 1 } ]
set endindex [ expr {$upd_num * $sfrows} ]
for { set i $startindex } { $i <= $endindex } { incr i } {
after $trickle_refresh
if { $upd_num == 0 } {
set okey [ mk_sparse $i $upd_num ]
} else {
set okey [ mk_sparse $i [ expr {1 + $upd_num / (10000 / $refresh)} ] ]
}
set custkey [ RandomNumber 1 $O_CKEY_MAX ]
while { $custkey % 3 == 0 } {
set custkey [ expr {$custkey + $delta} ]
if { $custkey < $O_CKEY_MAX } { set min $custkey } else { set min $O_CKEY_MAX }
set custkey $min
set delta [ expr {$delta * -1} ]
}
if { ![ array exists ascdate ] } {
for { set d 1 } { $d <= 2557 } {incr d} {
set ascdate($d) [ mk_time $d ]
        }
}
set tmp_date [ RandomNumber 92002 $O_ODATE_MAX ]
set date $ascdate([ expr {$tmp_date - 92001} ])
set opriority [ pick_str_2 [ get_dists o_oprio ] o_oprio ]
set clk_num [ RandomNumber 1 [ expr {$scale_factor * 1000} ] ]
set clerk [ concat Clerk#[format %1.9d $clk_num]]
set comment [ TEXT_2 49 ]
set spriority 0
set totalprice 0
set orderstatus "O"
set ocnt 0
set lcnt [ RandomNumber 1 7 ]
if { $ocnt > 0} { set orderstatus "P" }
if { $ocnt == $lcnt } { set orderstatus "F" }
if { $REFRESH_VERBOSE } {
puts "Refresh Insert Orderkey $okey..."
        }
$odbc evaldirect "INSERT INTO orders (o_orderdate, o_orderkey, o_custkey, o_orderpriority, o_shippriority, o_clerk, o_orderstatus, o_totalprice, o_comment) VALUES ('$date', '$okey', '$custkey', '$opriority', '$spriority', '$clerk', '$orderstatus', '$totalprice', '$comment')"
#Lineitem Loop
for { set l 0 } { $l < $lcnt } {incr l} {
set lokey $okey
set llcnt [ expr {$l + 1} ]
set lquantity [ RandomNumber 1 50 ]
set ldiscount [format %1.2f [ expr [ RandomNumber 0 10 ] / 100.00 ]]
set ltax [format %1.2f [ expr [ RandomNumber 0 8 ] / 100.00 ]]
set linstruct [ pick_str_2 [ get_dists instruct ] instruct ]
set lsmode [ pick_str_2 [ get_dists smode ] smode ]
set lcomment [ TEXT_2 27 ]
set lpartkey [ RandomNumber 1 $L_PKEY_MAX ]
set rprice [ rpb_routine $lpartkey ]
set supp_num [ RandomNumber 0 3 ]
set lsuppkey [ PART_SUPP_BRIDGE $lpartkey $supp_num $scale_factor ]
set leprice [format %4.2f [ expr {$rprice * $lquantity} ]]
set totalprice [format %4.2f [ expr {$totalprice + [ expr {(($leprice * (100 - $ldiscount)) / 100) * (100 + $ltax) / 100} ]}]]
set s_date [ RandomNumber 1 121 ]
set s_date [ expr {$s_date + $tmp_date} ]
set c_date [ RandomNumber 30 90 ]
set c_date [ expr {$c_date + $tmp_date} ]
set r_date [ RandomNumber 1 30 ]
set r_date [ expr {$r_date + $s_date} ]
set lsdate $ascdate([ expr {$s_date - 92001} ])
set lcdate $ascdate([ expr {$c_date - 92001} ])
set lrdate $ascdate([ expr {$r_date - 92001} ])
if { [ julian $r_date ] <= 95168 } {
set lrflag [ pick_str_2 [ get_dists rflag ] rflag ]
} else { set lrflag "N" }
if { [ julian $s_date ] <= 95168 } {
incr ocnt
set lstatus "F"
} else { set lstatus "O" }
odbc evaldirect "INSERT INTO lineitem (l_shipdate, l_orderkey, l_discount, l_extendedprice, l_suppkey, l_quantity, l_returnflag, l_partkey, l_linestatus, l_tax, l_commitdate, l_receiptdate, l_shipmode, l_linenumber, l_shipinstruct, l_comment) VALUES ('$lsdate','$lokey', '$ldiscount', '$leprice', '$lsuppkey', '$lquantity', '$lrflag', '$lpartkey', '$lstatus', '$ltax', '$lcdate', '$lrdate', '$lsmode', '$llcnt', '$linstruct', '$lcomment')"
  }
if { ![ expr {$i % 1000} ] } {
   }
}
}

proc del_order_ref { odbc upd_num scale_factor trickle_refresh REFRESH_VERBOSE } {
#2.28.2 Refresh Function Definition
#LOOP (SF * 1500) TIMES
#DELETE FROM ORDERS WHERE O_ORDERKEY = [value]
#DELETE FROM LINEITEM WHERE L_ORDERKEY = [value]
#END LOOP
set refresh 100
set sfrows [ expr {$scale_factor * 1500} ]
set startindex [ expr {(($upd_num * $sfrows) - $sfrows) + 1 } ]
set endindex [ expr {$upd_num * $sfrows} ]
for { set i $startindex } { $i <= $endindex } { incr i } {
after $trickle_refresh
if { $upd_num == 0 } {
set okey [ mk_sparse $i $upd_num ]
} else {
set okey [ mk_sparse $i [ expr {$upd_num / (10000 / $refresh)} ] ]
}
$odbc evaldirect "DELETE FROM lineitem WHERE l_orderkey = $okey"
$odbc evaldirect "DELETE FROM orders WHERE o_orderkey = $okey"
if { $REFRESH_VERBOSE } {
puts "Refresh Delete Orderkey $okey..."
        }
if { ![ expr {$i % 1000} ] } {
   }
 }
}

proc do_refresh { server port scale_factor odbc_driver authentication uid pwd tcp azure database update_sets trickle_refresh REFRESH_VERBOSE RF_SET } {
set connection [ connect_string $server $port $odbc_driver $authentication $uid $pwd $tcp $azure $database ]
if [catch {tdbc::odbc::connection create odbc $connection} message ] {
error "Connection to $connection could not be established : $message"
 } else {
if {!$azure} {odbc evaldirect "use $database"}
odbc evaldirect "set implicit_transactions OFF"
}
set upd_num 1
for { set set_counter 1 } {$set_counter <= $update_sets } {incr set_counter} {
if {  [ tsv::get application abort ]  } { break }
if { $RF_SET eq "RF1" || $RF_SET eq "BOTH" } {
puts "New Sales refresh"
set r0 [clock clicks -millisec]
mk_order_ref odbc $upd_num $scale_factor $trickle_refresh $REFRESH_VERBOSE
set r1 [clock clicks -millisec]
set rvalnew [expr {double($r1-$r0)/1000}]
puts "New Sales refresh complete in $rvalnew seconds"
        }
if { $RF_SET eq "RF2" || $RF_SET eq "BOTH" } {
puts "Old Sales refresh"
set r3 [clock clicks -millisec]
del_order_ref odbc $upd_num $scale_factor $trickle_refresh $REFRESH_VERBOSE
set r4 [clock clicks -millisec]
set rvalold [expr {double($r4-$r3)/1000}]
puts "Old Sales refresh complete in $rvalold seconds"
        }
if { $RF_SET eq "BOTH" } {
set rvaltot [expr {double($r4-$r0)/1000}]
puts "Completed update set(s) $set_counter in $rvaltot seconds"
        }
incr upd_num
        }
puts "Completed $update_sets update set(s)"
odbc close
}
#########################
#TPCH QUERY GENERATION
proc set_query { maxdop myposition } {
global sql
set sql(1) [string cat cachetext "l_returnflag, l_linestatus, sum(cast(l_quantity as bigint)) as sum_qty, sum(l_extendedprice) as sum_base_price, sum(l_extendedprice * (1 - l_discount)) as sum_disc_price, sum(l_extendedprice * (1 - l_discount) * (1 + l_tax)) as sum_charge, avg(cast(l_quantity as bigint)) as avg_qty, avg(l_extendedprice) as avg_price, avg(l_discount) as avg_disc, count(*) as count_order from  tpch.lineitem where l_shipdate <= add_days (to_date('1998-12-01', 'YYYY-MM-DD'),-109) group by l_returnflag, l_linestatus order by l_returnflag, l_linestatus "]
set sql(2) "select /*TPCH Q02*/ top 100 s_acctbal, s_name, n_name, p_partkey, p_mfgr, s_address, s_phone, s_comment from tpch.part, tpch.supplier, tpch.partsupp, tpch.nation, tpch.region where p_partkey = ps_partkey and s_suppkey = ps_suppkey and p_size = :1 and p_type like '%:2' and s_nationkey = n_nationkey and n_regionkey = r_regionkey and r_name = ':3' and ps_supplycost = ( select min(ps_supplycost) from tpch.partsupp, tpch.supplier, tpch.nation, tpch.region where p_partkey = ps_partkey and s_suppkey = ps_suppkey and s_nationkey = n_nationkey and n_regionkey = r_regionkey and r_name = ':3') order by s_acctbal desc, n_name, s_name, p_partkey "
set sql(3) "select /*TPCH Q03*/ top 10 l_orderkey, sum(l_extendedprice * (1 - l_discount)) as revenue, o_orderdate, o_shippriority from tpch.customer, tpch.orders,  tpch.lineitem where c_mktsegment = ':1' and c_custkey = o_custkey and l_orderkey = o_orderkey and o_orderdate < ':2' and l_shipdate > ':2' group by l_orderkey, o_orderdate, o_shippriority order by revenue desc, o_orderdate "
set sql(4) "select /*TPCH Q04*/ o_orderpriority, count(*) as order_count from tpch.orders where o_orderdate >= ':1' and o_orderdate < add_months(to_date(':1','YYYY-MM-DD'),3) and exists ( select * from  tpch.lineitem where l_orderkey = o_orderkey and l_commitdate < l_receiptdate) group by o_orderpriority order by o_orderpriority "
set sql(5) "select /*TPCH Q05*/ n_name, sum(l_extendedprice * (1 - l_discount)) as revenue from tpch.customer, tpch.orders, tpch.lineitem, tpch.supplier, tpch.nation, tpch.region where c_custkey = o_custkey and l_orderkey = o_orderkey and l_suppkey = s_suppkey and c_nationkey = s_nationkey and s_nationkey = n_nationkey and n_regionkey = r_regionkey and r_name = ':1' and o_orderdate >= ':2' and o_orderdate < add_years(to_date(':2','YYYY-MM-DD'),1) group by n_name order by revenue desc "
set sql(6) "select /*TPCH Q06*/ sum(l_extendedprice * l_discount) as revenue from  tpch.lineitem where l_shipdate >= ':1' and l_shipdate < add_years(to_date(':1','YYYY-DD-MM'),1) and l_discount between :2 - 0.01 and :2 + 0.01 and l_quantity < :3 "
set sql(7) "select /*TPCH Q07*/ supp_nation, cust_nation, l_year, sum(volume) as revenue from ( select n1.n_name as supp_nation, n2.n_name as cust_nation, year(l_shipdate) as l_year, l_extendedprice * (1 - l_discount) as volume from tpch.supplier,tpch.lineitem,tpch.orders,tpch.customer,tpch.nation n1, tpch.nation n2 where s_suppkey = l_suppkey and o_orderkey = l_orderkey and c_custkey = o_custkey and s_nationkey = n1.n_nationkey and c_nationkey = n2.n_nationkey and ( (n1.n_name = ':1' and n2.n_name = ':2') or (n1.n_name = ':2' and n2.n_name = ':1')) and l_shipdate between '1995-01-01' and '1996-12-31') shipping group by supp_nation, cust_nation, l_year order by supp_nation, cust_nation, l_year "
set sql(8) "select /*TPCH Q08*/ o_year, sum(case when nation = ':1' then volume else 0 end) / sum(volume) as mkt_share from (select year(o_orderdate) as o_year, l_extendedprice * (1 - l_discount) as volume, n2.n_name as nation from tpch.part, tpch.supplier,tpch.lineitem,tpch.orders, tpch.customer, tpch.nation n1, tpch.nation n2, tpch.region where p_partkey = l_partkey and s_suppkey = l_suppkey and l_orderkey = o_orderkey and o_custkey = c_custkey and c_nationkey = n1.n_nationkey and n1.n_regionkey = r_regionkey and r_name = ':2' and s_nationkey = n2.n_nationkey and o_orderdate between '1995-01-01' and '1996-12-31' and p_type = ':3') all_nations group by o_year order by o_year "
set sql(9) "select /*TPCH Q09*/ nation, o_year, sum(amount) as sum_profit from ( select n_name as nation, year(o_orderdate) as o_year, l_extendedprice * (1 - l_discount) - ps_supplycost * l_quantity as amount from tpch.part, tpch.supplier, tpch.lineitem, tpch.partsupp, tpch.orders, tpch.nation where s_suppkey = l_suppkey and ps_suppkey = l_suppkey and ps_partkey = l_partkey and p_partkey = l_partkey and o_orderkey = l_orderkey and s_nationkey = n_nationkey and p_name like '%:1%') profit group by nation, o_year order by nation, o_year desc "
set sql(10) "select /*TPCH Q10*/ top 20 c_custkey, c_name, sum(l_extendedprice * (1 - l_discount)) as revenue, c_acctbal, n_name, c_address, c_phone, c_comment from tpch.customer, tpch.orders, tpch.lineitem, tpch.nation where c_custkey = o_custkey and l_orderkey = o_orderkey and o_orderdate >= ':1' and o_orderdate < add_months(to_date(':1', 'YYYY-MM-DD'),3) and l_returnflag = 'R' and c_nationkey = n_nationkey group by c_custkey, c_name, c_acctbal, c_phone, n_name, c_address, c_comment order by revenue desc "
set sql(11) "select /*TPCH Q11*/ ps_partkey, sum(ps_supplycost * ps_availqty) as value from tpch.partsupp, tpch.supplier, tpch.nation where ps_suppkey = s_suppkey and s_nationkey = n_nationkey and n_name = ':1' group by ps_partkey having sum(ps_supplycost * ps_availqty) > ( select sum(ps_supplycost * ps_availqty) * :2 from tpch.partsupp, tpch.supplier, tpch.nation where ps_suppkey = s_suppkey and s_nationkey = n_nationkey and n_name = ':1') order by value desc "
set sql(12) "select /*TPCH Q12*/ l_shipmode, sum(case when o_orderpriority = '1-URGENT' or o_orderpriority = '2-HIGH' then 1 else 0 end) as high_line_count, sum(case when o_orderpriority <> '1-URGENT' and o_orderpriority <> '2-HIGH' then 1 else 0 end) as low_line_count from tpch.orders,  tpch.lineitem where o_orderkey = l_orderkey and l_shipmode in (':1', ':2') and l_commitdate < l_receiptdate and l_shipdate < l_commitdate and l_receiptdate >= ':3' and l_receiptdate < add_months(to_date(':3','YYYY-MM-DD'),1) group by l_shipmode order by l_shipmode "
set sql(13) "select /*TPCH Q13*/ c_count, count(*) as custdist from ( select c_custkey, count(o_orderkey) as c_count from tpch.customer left outer join tpch.orders on c_custkey = o_custkey and o_comment not like '%:1%:2%' group by c_custkey) c_orders group by c_count order by custdist desc, c_count desc "
set sql(14) "select /*TPCH Q14*/ 100.00 * sum(case when p_type like 'PROMO%' then l_extendedprice * (1 - l_discount) else 0 end) / sum(l_extendedprice * (1 - l_discount)) as promo_revenue from tpch.lineitem, tpch.part where l_partkey = p_partkey and l_shipdate >= ':1' and l_shipdate < add_months(to_date(':1','YYYY-MM-DD'),1) "
set sql(15) "with revenue0 as (select l_suppkey as supplier_no, sum(l_extendedprice * (1 - l_discount)) as total_revenue from  tpch.lineitem where l_shipdate >= '1996-01-01' and l_shipdate < add_months(to_date('1996-01-01','YYYY-MM-DD'),3) group by l_suppkey ) select /*TPCH Q15*/ s_suppkey, s_name, s_address, s_phone, revenue0.total_revenue from tpch.supplier inner join revenue0 on s_suppkey = revenue0.supplier_no order by s_suppkey "
set sql(16) "select /*TPCH Q16*/ p_brand, p_type, p_size, count(distinct ps_suppkey) as supplier_cnt from tpch.partsupp, tpch.part where p_partkey = ps_partkey and p_brand <> ':1' and p_type not like ':2%' and p_size in (:3, :4, :5, :6, :7, :8, :9, :10) and ps_suppkey not in ( select s_suppkey from tpch.supplier where s_comment like '%Customer%Complaints%') group by p_brand, p_type, p_size order by supplier_cnt desc, p_brand, p_type, p_size "
set sql(17) "select /*TPCH Q17*/ sum(l_extendedprice) / 7.0 as avg_yearly from tpch.lineitem, tpch.part where p_partkey = l_partkey and p_brand = ':1' and p_container = ':2' and l_quantity < ( select 0.2 * avg(l_quantity) from  tpch.lineitem where l_partkey = p_partkey) "
set sql(18) "select /*TPCH Q18*/ top 100 c_name, c_custkey, o_orderkey, o_orderdate, o_totalprice, sum(l_quantity) from tpch.customer, tpch.orders,tpch.lineitem where o_orderkey in ( select l_orderkey from  tpch.lineitem group by l_orderkey having sum(l_quantity) > :1) and c_custkey = o_custkey and o_orderkey = l_orderkey group by c_name, c_custkey, o_orderkey, o_orderdate, o_totalprice order by o_totalprice desc, o_orderdate "
set sql(19) "select /*TPCH Q19*/ sum(l_extendedprice* (1 - l_discount)) as revenue from tpch.lineitem, tpch.part where ( p_partkey = l_partkey and p_brand = ':1' and p_container in ('SM CASE', 'SM BOX', 'SM PACK', 'SM PKG') and l_quantity >= :4 and l_quantity <= :4 + 10 and p_size between 1 and 5 and l_shipmode in ('AIR', 'AIR REG') and l_shipinstruct = 'DELIVER IN PERSON') or ( p_partkey = l_partkey and p_brand = ':2' and p_container in ('MED BAG', 'MED BOX', 'MED PKG', 'MED PACK') and l_quantity >= :5 and l_quantity <= :5 + 10 and p_size between 1 and 10 and l_shipmode in ('AIR', 'AIR REG') and l_shipinstruct = 'DELIVER IN PERSON') or ( p_partkey = l_partkey and p_brand = ':3' and p_container in ('LG CASE', 'LG BOX', 'LG PACK', 'LG PKG') and l_quantity >= :6 and l_quantity <= :6 + 10 and p_size between 1 and 15 and l_shipmode in ('AIR', 'AIR REG') and l_shipinstruct = 'DELIVER IN PERSON') "
set sql(20) "select /*TPCH Q20*/ s_name, s_address from tpch.supplier, tpch.nation where s_suppkey in ( select ps_suppkey from tpch.partsupp where ps_partkey in ( select p_partkey from tpch.part where p_name like ':1%') and ps_availqty > ( select 0.5 * sum(l_quantity) from  tpch.lineitem where l_partkey = ps_partkey and l_suppkey = ps_suppkey and l_shipdate >= ':2' and l_shipdate < add_years(to_date(':2','YYYY-MM-DD'),1))) and s_nationkey = n_nationkey and n_name = ':3' order by s_name "
set sql(21) "select /*TPCH Q21*/ top 100 s_name, count(*) as numwait from tpch.supplier,tpch.lineitem l1, tpch.orders,tpch.nation where s_suppkey = l1.l_suppkey and o_orderkey = l1.l_orderkey and o_orderstatus = 'F' and l1.l_receiptdate > l1.l_commitdate and exists ( select * from  tpch.lineitem l2 where l2.l_orderkey = l1.l_orderkey and l2.l_suppkey <> l1.l_suppkey) and not exists ( select * from  tpch.lineitem l3 where l3.l_orderkey = l1.l_orderkey and l3.l_suppkey <> l1.l_suppkey and l3.l_receiptdate > l3.l_commitdate) and s_nationkey = n_nationkey and n_name = ':1' group by s_name order by numwait desc, s_name "
set sql(22) "select /*TPCH Q22*/ cntrycode, count(*) as numcust, sum(c_acctbal) as totacctbal from ( select substring(c_phone, 1, 2) as cntrycode, c_acctbal from tpch.customer where substring(c_phone, 1, 2) in (':1', ':2', ':3', ':4', ':5', ':6', ':7') and c_acctbal > ( select avg(c_acctbal) from tpch.customer where c_acctbal > 0.00 and substring(c_phone, 1, 2) in (':1', ':2', ':3', ':4', ':5', ':6', ':7')) and not exists ( select * from tpch.orders where o_custkey = c_custkey)) custsale group by cntrycode order by cntrycode "
}


proc get_query { query_no maxdop myposition } {
global sql
if { ![ array exists sql ] } { set_query $maxdop $myposition }
return $sql($query_no)
}

proc sub_query { query_no scale_factor maxdop myposition } {
set P_SIZE_MIN 1
set P_SIZE_MAX 50
set MAX_PARAM 10
set q2sub [get_query $query_no $maxdop $myposition ]
switch $query_no {
1 {
regsub -all {:1} $q2sub [RandomNumber 60 120] q2sub
  }
2 {
regsub -all {:1} $q2sub [RandomNumber $P_SIZE_MIN $P_SIZE_MAX] q2sub
set qc [ lindex [ split [ pick_str_2 [ get_dists p_types ] p_types ] ] 2 ]
regsub -all {:2} $q2sub $qc q2sub
set qc [ pick_str_2 [ get_dists regions ] regions ]
regsub -all {:3} $q2sub $qc q2sub
  }
3 {
set qc [ pick_str_2 [ get_dists msegmnt ] msegmnt ]
regsub -all {:1} $q2sub $qc q2sub
set tmp_date [RandomNumber 1 31]
if { [ string length $tmp_date ] eq 1 } {set tmp_date [ concat 0$tmp_date ]  }
regsub -all {:2} $q2sub [concat 1995-03-$tmp_date] q2sub
  }
4 {
set tmp_date [RandomNumber 1 58]
set yr [ expr 93 + $tmp_date/12 ]
set mon [ expr $tmp_date % 12 + 1 ]
if { [ string length $mon ] eq 1 } {set mon [ concat 0$mon ] }
set tmp_date [ concat 19$yr-$mon-01 ]
regsub -all {:1} $q2sub $tmp_date q2sub
  }
5 {
set qc [ pick_str_2 [ get_dists regions ] regions ]
regsub -all {:1} $q2sub $qc q2sub
set tmp_date [RandomNumber 93 97]
regsub -all {:2} $q2sub [concat 19$tmp_date-01-01] q2sub
  }
6 {
set tmp_date [RandomNumber 93 97]
regsub -all {:1} $q2sub [concat 19$tmp_date-01-01] q2sub
regsub -all {:2} $q2sub [concat 0.0[RandomNumber 2 9]] q2sub
regsub -all {:3} $q2sub [RandomNumber 24 25] q2sub
  }
7 {
set qc [ pick_str_2 [ get_dists nations2 ] nations2 ]
regsub -all {:1} $q2sub $qc q2sub
set qc2 $qc
while { $qc2 eq $qc } { set qc2 [ pick_str_2 [ get_dists nations2 ] nations2 ] }
regsub -all {:2} $q2sub $qc2 q2sub
  }
8 {
set nationlist [ get_dists nations2 ]
set regionlist [ get_dists regions ]
set qc [ pick_str_2 $nationlist nations2 ]
regsub -all {:1} $q2sub $qc q2sub
set nind [ lsearch -glob $nationlist [concat \*$qc\*] ]
switch $nind {
0 - 4 - 5 - 14 - 15 - 16 { set qc "AFRICA" }
1 - 2 - 3 - 17 - 24 { set qc "AMERICA" }
8 - 9 - 12 - 18 - 21 { set qc "ASIA" }
6 - 7 - 19 - 22 - 23 { set qc "EUROPE"}
10 - 11 - 13 - 20 { set qc "MIDDLE EAST"}
}
regsub -all {:2} $q2sub $qc q2sub
set qc [ pick_str_2 [ get_dists p_types ] p_types ]
regsub -all {:3} $q2sub $qc q2sub
  }
9 {
set qc [ pick_str_2 [ get_dists colors ] colors ]
regsub -all {:1} $q2sub $qc q2sub
  }
10 {
set tmp_date [RandomNumber 1 24]
set yr [ expr 93 + $tmp_date/12 ]
set mon [ expr $tmp_date % 12 + 1 ]
if { [ string length $mon ] eq 1 } {set mon [ concat 0$mon ] }
set tmp_date [ concat 19$yr-$mon-01 ]
regsub -all {:1} $q2sub $tmp_date q2sub
   }
11 {
set qc [ pick_str_2 [ get_dists nations2 ] nations2 ]
regsub -all {:1} $q2sub $qc q2sub
set q11_fract [ format %11.10f [ expr 0.0001 / $scale_factor ] ]
regsub -all {:2} $q2sub $q11_fract q2sub
}
12 {
set qc [ pick_str_2 [ get_dists smode ] smode ]
regsub -all {:1} $q2sub $qc q2sub
set qc2 $qc
while { $qc2 eq $qc } { set qc2 [ pick_str_2 [ get_dists smode ] smode ] }
regsub -all {:2} $q2sub $qc2 q2sub
set tmp_date [RandomNumber 93 97]
regsub -all {:3} $q2sub [concat 19$tmp_date-01-01] q2sub
}
13 {
set qc [ pick_str_2 [ get_dists Q13a ] Q13a ]
regsub -all {:1} $q2sub $qc q2sub
set qc [ pick_str_2 [ get_dists Q13b ] Q13b ]
regsub -all {:2} $q2sub $qc q2sub
}
14 {
set tmp_date [RandomNumber 1 60]
set yr [ expr 93 + $tmp_date/12 ]
set mon [ expr $tmp_date % 12 + 1 ]
if { [ string length $mon ] eq 1 } {set mon [ concat 0$mon ] }
set tmp_date [ concat 19$yr-$mon-01 ]
regsub -all {:1} $q2sub $tmp_date q2sub
}
15 {
set tmp_date [RandomNumber 1 58]
set yr [ expr 93 + $tmp_date/12 ]
set mon [ expr $tmp_date % 12 + 1 ]
if { [ string length $mon ] eq 1 } {set mon [ concat 0$mon ] }
set tmp_date [ concat 19$yr-$mon-01 ]
regsub -all {:1} $q2sub $tmp_date q2sub
}
16 {
set tmp1 [RandomNumber 1 5]
set tmp2 [RandomNumber 1 5]
regsub {:1} $q2sub [ concat Brand\#$tmp1$tmp2 ] q2sub
set p_type [ split [ pick_str_2 [ get_dists p_types ] p_types ] ]
set qc [ concat [ lindex $p_type 0 ] [ lindex $p_type 1 ] ]
regsub -all {:2} $q2sub $qc q2sub
set permute [list]
for {set i 3} {$i <= $MAX_PARAM} {incr i} {
set tmp3 [RandomNumber 1 50]
while { [ lsearch $permute $tmp3 ] != -1  } {
set tmp3 [RandomNumber 1 50]
}
lappend permute $tmp3
set qc $tmp3
regsub -all ":$i" $q2sub $qc q2sub
        }
   }
17 {
set tmp1 [RandomNumber 1 5]
set tmp2 [RandomNumber 1 5]
regsub {:1} $q2sub [ concat Brand\#$tmp1$tmp2 ] q2sub
set qc [ pick_str_2 [ get_dists p_cntr ] p_cntr ]
regsub -all {:2} $q2sub $qc q2sub
 }
18 {
regsub -all {:1} $q2sub [RandomNumber 312 315] q2sub
}
19 {
set tmp1 [RandomNumber 1 5]
set tmp2 [RandomNumber 1 5]
regsub {:1} $q2sub [ concat Brand\#$tmp1$tmp2 ] q2sub
set tmp1 [RandomNumber 1 5]
set tmp2 [RandomNumber 1 5]
regsub {:2} $q2sub [ concat Brand\#$tmp1$tmp2 ] q2sub
set tmp1 [RandomNumber 1 5]
set tmp2 [RandomNumber 1 5]
regsub {:3} $q2sub [ concat Brand\#$tmp1$tmp2 ] q2sub
regsub -all {:4} $q2sub [RandomNumber 1 10] q2sub
regsub -all {:5} $q2sub [RandomNumber 10 20] q2sub
regsub -all {:6} $q2sub [RandomNumber 20 30] q2sub
}
20 {
set qc [ pick_str_2 [ get_dists colors ] colors ]
regsub -all {:1} $q2sub $qc q2sub
set tmp_date [RandomNumber 93 97]
regsub -all {:2} $q2sub [concat 19$tmp_date-01-01] q2sub
set qc [ pick_str_2 [ get_dists nations2 ] nations2 ]
regsub -all {:3} $q2sub $qc q2sub
        }
21 {
set qc [ pick_str_2 [ get_dists nations2 ] nations2 ]
regsub -all {:1} $q2sub $qc q2sub
}
22 {
set permute [list]
for {set i 0} {$i <= 7} {incr i} {
set tmp3 [RandomNumber 10 34]
while { [ lsearch $permute $tmp3 ] != -1  } {
set tmp3 [RandomNumber 10 34]
}
lappend permute $tmp3
set qc $tmp3
regsub -all ":$i" $q2sub $qc q2sub
        }
    }
}
return $q2sub
}
#########################
#TPCH QUERY SETS PROCEDURE
proc do_tpch { server port scale_factor odbc_driver authentication uid pwd tcp azure db RAISEERROR VERBOSE maxdop total_querysets myposition } {
set connection [ connect_string $server $port $odbc_driver $authentication $uid $pwd $tcp $azure $db ]
if [catch {tdbc::odbc::connection create odbc $connection} message ] {
error "Connection to $connection could not be established : $message"
 } else {
#if {!$azure} {odbc evaldirect "use $db"}
#odbc evaldirect "set implicit_transactions OFF"
#}
for {set it 0} {$it < $total_querysets} {incr it} {
if {  [ tsv::get application abort ]  } { break }
unset -nocomplain qlist
set start [ clock seconds ]
for { set q 1 } { $q <= 22 } { incr q } {
set dssquery($q)  [sub_query $q $scale_factor $maxdop $myposition ]
if {$q != 15} {
        ;
} else {
set query15list [split $dssquery($q) "\;"]
            set q15length [llength $query15list]
            set q15c 0
            while {$q15c <= [expr $q15length - 1]} {
            set dssquery($q,$q15c) [lindex $query15list $q15c]
            incr q15c
                }
        }
}
set o_s_list [ ordered_set $myposition ]
for { set q 1 } { $q <= 22 } { incr q } {
if {  [ tsv::get application abort ]  } { break }
set qos [ lindex $o_s_list [ expr $q - 1 ] ]
puts "Executing Query $qos ($q of 22)"
if {$VERBOSE} { puts $dssquery($qos) }
if {$qos != 15} {
set t0 [clock clicks -millisec]
set oput [ standsql odbc $dssquery($qos) $RAISEERROR ]
set t1 [clock clicks -millisec]
set value [expr {double($t1-$t0)/1000}]
if {$VERBOSE} { printlist $oput }
if { [ llength $oput ] > 0 } { lappend qlist $value }
puts "query $qos completed in $value seconds"
              } else {
            set q15c 0
            while {$q15c <= [expr $q15length - 1] } {
        if { $q15c != 1 } {
if {[ catch {set sql_output [odbc evaldirect $dssquery($qos,$q15c)]} message]} {
if { $RAISEERROR } {
error "Query Error :$message"
        } else {
puts "$message"
                }
          }
        } else {
set t0 [clock clicks -millisec]
set oput [ standsql odbc $dssquery($qos,$q15c) $RAISEERROR ]
set t1 [clock clicks -millisec]
set value [expr {double($t1-$t0)/1000}]
if {$VERBOSE} { printlist $oput }
if { [ llength $oput ] > 0 } { lappend qlist $value }
puts "query $qos completed in $value seconds"
                }
            incr q15c
                }
        }
  }
set end [ clock seconds ]
set wall [ expr $end - $start ]
set qsets [ expr $it + 1 ]
puts "Completed $qsets query set(s) in $wall seconds"
puts "Geometric mean of query times returning rows ([llength $qlist]) is [ format \"%.5f\" [ gmean $qlist ]]"
        }
odbc close
 }
#########################
#RUN TPC-H
set rema [ lassign [ findvuhposition ] myposition totalvirtualusers ]
set power_test "false"
if { $totalvirtualusers eq 1 } {
#Power Test
set power_test "true"
set myposition 0
        }
if { $refresh_on } {
if { $power_test } {
set trickle_refresh 0
set update_sets 1
set REFRESH_VERBOSE "false"
do_refresh $server $port $scale_factor $odbc_driver $authentication $uid $pwd $tcp $azure $database $update_sets $trickle_refresh $REFRESH_VERBOSE RF1
do_tpch $server $port $scale_factor $odbc_driver $authentication $uid $pwd $tcp $azure $database $RAISEERROR $VERBOSE $maxdop $total_querysets 0
do_refresh $server $port $scale_factor $odbc_driver $authentication $uid $pwd $tcp $azure $database $update_sets $trickle_refresh $REFRESH_VERBOSE RF2
        } else {
switch $myposition {
1 {
do_refresh $server $port $scale_factor $odbc_driver $authentication $uid $pwd $tcp $azure $database $update_sets $trickle_refresh $REFRESH_VERBOSE BOTH
        }
default {
do_tpch $server $port $scale_factor $odbc_driver $authentication $uid $pwd $tcp $azure $database $RAISEERROR $VERBOSE $maxdop $total_querysets [ expr $myposition - 1 ]
        }
    }
 }
} else {
do_tpch $server $port $scale_factor $odbc_driver $authentication $uid $pwd $tcp $azure $database $RAISEERROR $VERBOSE $maxdop $total_querysets $myposition
                }









