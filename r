CREATE DATABASE PythonAutomation;
CREATE DATABASE APIDevelop;
use APIDevelop;
CREATE TABLE CustomerInfo

(CourseName varchar(50),

PurchasedDate date,

Amount int(50),

Location varchar(50));



INSERT INTO CustomerInfo values("selenium",CURRENT_DATE(),120,'Africa');

INSERT INTO CustomerInfo values("Protractor",CURRENT_DATE(),45,'Africa');

INSERT INTO CustomerInfo values("Appium",CURRENT_DATE(),99,'Asia');

INSERT INTO CustomerInfo values("WebServices",CURRENT_DATE(),21,'Asia');

INSERT INTO CustomerInfo values("Jmeter",CURRENT_DATE(),76,'Asia');

CREATE TABLE Books

(BookName varchar(50),

isbn varchar(50),

aisle varchar(50),

author varchar(50));

INSERT INTO Books values("Devops","bnid34","75","Rahul Shetty2");
INSERT INTO Books values("Selenium","kosncs34fr","23","Rahul Shetty");
INSERT INTO Books values("Jmeter","rtbrss24t","234","Rahul Shetty3");
select * from Books;
select * from CustomerInfo;
SET SQL_SAFE_UPDATES = 0;
update customerInfo set Location = 'US' where CourseName = 'Jmeter';
delete from customerInfo where courseName = 'WebServices';




CREATE TABLE Storage3(book_name varchar(50),id varchar(50),

isbn varchar(50),

aisle int,

author varchar(50),PRIMARY KEY (id));
	INSERT INTO Storage3(book_name,id,isbn,aisle,author) values("Appium","fdsefr343","fdsefr3","43","Rahul Shetty");
	INSERT INTO Storage3 values("selenium","qwer12","qwer","12","Rahul Shetty");
select * from Storage3;
