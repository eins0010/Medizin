# Medizin
Hello,

Welcome to the World Of Programming.


Medicine management system

The idea behind this is to give a better perspective of medical application.
<br>Link for markdown language documentation:
(https://daringfireball.net/projects/markdown/syntax#overview)

Initial Setup:
<pre>Download MySQL server from following link: </pre>
(https://dev.mysql.com/downloads/mysql/)
<pre>Download MySQL shell from following link:</pre>
(https://dev.mysql.com/downloads/shell/)
<pre>Complete single installation for windows </pre>
(https://dev.mysql.com/downloads/installer/)
- Setup the path for mysql if not already set by executable installer.

### To Start server:
Mac Users: Go to system Preferences -> MySQL -> start server <br>
Windows Users: Please check under right bottom menu

### To login to mysql shell
<pre>mysql -u USERNAME -pPASSWORD -h HOSTNAMEORIP DATABASENAME </pre> 
The options above means:
<pre>
-u: username
-p: password (**no space between -p and the password text**)
-h: host
last one is name of the database that you wanted to connect
</pre>
If user is root with passowrd is 123 trying to connect to database hive on IP 123.0.0.1
<pre>mysql --user root -p123 -h 123.0.0.1 hive</pre>  

### For the First time users
- create database MEDIZIN; 
- use MEDIZIN;
- CREATE TABLE test (name VARCHAR(20), role VARCHAR(20));
- insert into test values ("ravi", "admin");
- create table UserCredentials (userid VARCHAR(20), username VARCHAR(20), e_password VARCHAR(20));
- insert into UserCredentials values ("101", "ravi", "qwert");
- insert into UserCredentials values ("102", "eins", "poiut");

### Tutorials for working with python connectors
https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
