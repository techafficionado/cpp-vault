Note: You need to specify the 'where RowYearDayCode between' condition for the paritioning to take into effect in your select

Sample explain on the query:

explain select * from Position1 where RowYearDayCode>2018104 and RowYearDayCode<2018107;
+----+-------------+-----------+-------------------------+------+---------------+------+---------+------+------+----------+-------------+
| id | select_type | table     | partitions              | type | possible_keys | key  | key_len | ref  | rows | filtered | Extra       |
+----+-------------+-----------+-------------------------+------+---------------+------+---------+------+------+----------+-------------+
|  1 | SIMPLE      | Position1 | part2018106,part2018107 | ALL  | NULL          | NULL | NULL    | NULL |    1 |   100.00 | Using where |
+----+-------------+-----------+-------------------------+------+---------------+------+---------+------+------+----------+-------------+
1 row in set, 1 warning (0.00 sec)

Best Practices:
> Do not have more than 50 partitions to avoid slowing down of queries.
> My tests showed that including the partition condition reduced query time by half.
