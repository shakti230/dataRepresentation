show databases;
create database datarep;
use datarep;
create table training ( id int NOT NULL auto_increment, 
name varchar(80), course varchar(80), PRIMARY KEY(id) );
insert into training (name) value ("Sarah"); 
insert into training (name) value (’Sarah’); 
Delete from training where id = 1;
select * from training;
update training set firstname="Tom" where id = 1;
create table course ( id int NOT NULL auto_increment, 
course varchar(80),  description varchar(80), PRIMARY KEY(id) );
select * from course;
insert into course (course, description) values ("DSE Training","Online DSE training"); 
insert into course (course, description) values ("Manual Handling","Training on manual handling",); 
