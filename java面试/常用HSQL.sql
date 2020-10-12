什么是绝对值同比
    本期数据-同期数据/|同期数据|
    例： 2019年1月1日的gmv -2018年1月1日的gmv/|2018年1月1日的gmv|

什么是绝对值环比
    本期数据-上期数据/|上期数据|
    例： 2019年2月2日的gmv -2018年2月1日的gmv/|2018年2月1日的gmv|

数据集准备
建表语句
    create table new_table(
    dt string,
    area string,
    province string,
    saleroom int
    );
数据准备
    insert into new_table values('2017-12-01', 'hd', 'sh','3600000');
    insert into new_table values('2017-12-02', 'hd', 'js','2800000');
    insert into new_table values('2017-12-03', 'hd', 'zj','4500000');
    insert into new_table values('2017-12-04', 'hb', 'bj','3000000');
    insert into new_table values('2017-12-05', 'hb', 'tj','2800000');
    insert into new_table values('2018-12-01', 'hd', 'sh','3000000');
    insert into new_table values('2018-12-02', 'hd', 'js','2000000');
    insert into new_table values('2018-12-03', 'hd', 'zj','2500000');
    insert into new_table values('2018-12-04', 'hb', 'bj','2600000');
    insert into new_table values('2018-12-05', 'hb', 'tj','1500000');
-- 同比计算
with tmp as (
select
dt,
area,
province,
saleroom,
lag(saleroom,1,0) over(partition by concat(month(dt),"-",day(dt)),area,province order by dt asc) pre_sale
from new_table)
select
dt,area,province,saleroom,pre_sale,
if(round((saleroom-pre_sale)/abs(pre_sale)*1.00,2) is null,100,round((saleroom-pre_sale)/abs(pre_sale)*1.00,2)*100)
from tmp;

-- 环比计算
with tmp as (
    select
        dt,
        area,
        province,
        saleroom,
        lag(saleroom,1,0) over(partition by concat(month(dt),"-",day(dt)),area,province order by dt asc) pre_sale
        from new_table)

    select
        dt,area,province,saleroom,pre_sale,
        if(round((saleroom-pre_sale)/abs(pre_sale)*1.00,2) is null,100,round((saleroom-pre_sale)/abs(pre_sale)*1.00,2)*100)
        from tmp ;

-- lateral的用法
lateral view explode(split(...)) new_table as new_column




4、[Hive SQL]统计amt连续3个月，环比增长>50%的user

user_id month amt
1,20170101,100
3,20170101,20
4,20170101,30
1,20170102,200
2,20170102,240
3,20170102,30
4,20170102,2
1,20170101,180
2,20170101,250
3,20170101,30
4,20170101,260
…
…

select user_id
    from(
    select
        user_id,month,mon_amt,pre_mon_amt,
        --当前月的销售额 > 前一个月的销售额并且
        sum(case when ((mon_amt - pre_mon_amt) / pre_mon_amt * 100) > 50
            and datediff(to_date(month,'yyyymm'),to_date(pre2_month,'yyyymm'),'mm') = 2
            then 1 else 0 end)
        over(partition by user_id order by month asc rows between current row and 2 following) as flag
    from (
        select
            user_id,
            substr(month,0,6) as month,
            sum(amt) as mon_amt,
            --计算当前月份的上一个月份的销售总额
            lag(sum(amt),1,0.00001) over(partition by user_id order by substr(month,0,6) asc ) as pre_mon_amt,
            --计算当前月份的前2个月的月份
            substr(lag(substr(month,0,6),2,'199001') over(partition by user_id order by substr(month,0,6) asc),0,6) as pre_2_mon
        from amt
    group by user_id,substr(month,0,6)
    ) t1
  ) t2
  where t2.flag >=3;



-- 按时间段统计
SELECT time, COUNT( * ) AS num
FROM
	(
	SELECT Duration,
		DATE_FORMAT(
			concat( date( TimeStart ), ' ', HOUR ( TimeStart ), ':', floor( MINUTE ( TimeStart ) / 10 ) * 10 ),
			'%Y-%m-%d %H:%i'
		) AS time
	FROM tarck
	WHERE Flag = 0  AND Duration >= 300
	) a
GROUP BY DATE_FORMAT( time, '%Y-%m-%d %H:%i' )
ORDER BY time;

-- 按时间段统计2
from_unixtime(floor(unix_timestamp(errorTime) / 60) * 60, '%Y-%m-%d %H:%i:%s') as date

-- 按时间段统计3
from_unixtime(unix_timestamp(time) - unix_timestamp(time) % time_interval, '%Y-%m-%d %H:%i:%s') as date