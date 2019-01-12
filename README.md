# Medizin

Medicine management system

Hello, This project concentrates on problems faced by small scale pharmacy. 
The idea behind this is to give a better perspective of medical application.
Objective is to provide a world class software to deliver following usercases: 
- their daily medicine intake, export and stock
- Money transactions
- Notifications about medicines going to expire
- Taking all Actors together to deliver a complete package to user.


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

- Install Gradle
(https://gradle.org/install/) 

### To Start MYSQL server:
Mac Users: Go to system Preferences -> MySQL -> start server <br>
Windows Users: Please check under right bottom menu or anything similar for windows

### To Start this Medizin application
Go to Medizin directory from either terminal or cmd and type the following 
<pre> gradle run </pre> 

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
- https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html

### Tutorial for AES Encryption
- https://www.youtube.com/watch?v=AQDCe585Lnc

### Project structure
<pre>
      ├── README.md -> Holds the top level documentation.
      ├── config.py -> All project level configuration goes here.
      ├── requirements.txt -> All the packages required to run this application smoothly.
      ├── run.py -> To run this application.
      └── Medizin
          ├── serializers -> Holds all the transformers
          ├── clients -> Any external service we are trying to use in this project
          ├── controllers -> All the rest end points are exposed here.
          ├── models -> All Project level data models goes here
          ├── utils -> project level utilities folder
          └── tests -> test the configured routes
</pre>

### DATABASE
This Database folder holds files which have different meaning.

-> Connections: File holding connections to different databases (MSSQL and MYSQL)
-> database_tables: All the table protos for this project. Some insertion data if required.
-> table objects: This is a directory under which Each Database table should be represented as a class entity in this file. 
Along with the attributes this class should contain methods to perform operations specific to that table.

### CONTROLLERS
This folder mainly concentrates on different kind of routes we can provide under a namespace for better good of this application.

### SERIALIZERS
This folder holds all the serializers or transformers for marshalling and unmarshalling. Either it can be getting data from web to 
convert into our proto or converting our system defined proto to API readable format.
The files in this folder follows the following convention: controller_name + model (authenticate_model)

### TESTS
This folder holds the test cases for all the routes in the application, testing it with different kind of inputs.
