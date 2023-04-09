Writer User
---
mysql> CREATE USER 'my_app'@'%' IDENTIFIED WITH mysql_native_password BY 'my_app_pass';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES on *.* TO 'my_app'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)


Reader User
---
mysql> CREATE USER 'my_app_reader'@'%' IDENTIFIED WITH mysql_native_password BY 'my_app_reader_pass';
Query OK, 0 rows affected (0.01 sec)
mysql> GRANT SELECT on *.* TO 'my_app_reader'@'%' WITH GRANT OPTION;
Query OK, 0 rows affected (0.01 sec)

