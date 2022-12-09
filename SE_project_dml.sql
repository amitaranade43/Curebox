---------- Populate Role entries start -------------------

insert into role(id,rolename) values(1,'Patient');
insert into role(id,rolename) values(2,'Doctor');
insert into role(id,rolename) values(3,'Insurance Provider');


---------- Populate Role entries end -------------------


---------- Populate User entries start -----------------

delete from public.user;

insert into public.user(id,password,first_name,last_name,email,role_id)
values(1,'qwerty','Patient1','Pat1','patient1@gmail.com',1);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(2,'qwerty','Patient2','Pat2','patient2@gmail.com',1);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(3,'qwerty','Patient3','Pat3','patient3@gmail.com',1);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(4,'qwerty','Patient4','Pat4','patient4@gmail.com',1);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(5,'qwerty','Patient5','Pat5','patient5@gmail.com',1);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(6,'qwerty','Patient6','Pat6','patient6@gmail.com',1);

insert into public.user(id,password,first_name,last_name,email,role_id)
values(7,'qwerty','Doctor1','Doc1','doctor1@gmail.com',2);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(8,'qwerty','Doctor2','Doc2','doctor2@gmail.com',2);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(9,'qwerty','Doctor3','Doc3','doctor3@gmail.com',2);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(10,'qwerty','Doctor4','Doc4','doctor4@gmail.com',2);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(11,'qwerty','Doctor5','Doc5','doctor5@gmail.com',2);
insert into public.user(id,password,first_name,last_name,email,role_id)
values(12,'qwerty','Doctor6','Doc6','doctor6@gmail.com',2);

------------ Populate User entrie end ---------------------



---------- Populate Doctor entries start -------------------
delete from doctor 
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('7',1,20,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('8',1,40,FALSE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('9',2,60,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('10',2,40,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('11',3,50,FALSE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('12',4,70,TRUE);

---------- Populate Doctor entries end -------------------

---------- Populate Hospital entries start -------------------

delete from hospital
insert into hospital(id,name,location,no_of_covid_beds) 
values(1,'IU Health Bloomington Hospital','Bloomington',10)
insert into hospital(id,name,location,no_of_covid_beds) 
values(2,'Harrison County Hospital','Corydon',15)
insert into hospital(id,name,location,no_of_covid_beds) 
values(3,'Johnson Memorial Health','Franklin',10)
insert into hospital(id,name,location,no_of_covid_beds) 
values(4,'Monroe Hospital','Bloomington',10)


---------- Populate Hospital entries end -------------------


---------- Populate Doctor disease entries start -------------------

delete from doctor_disease;

insert into doctor_disease(doctor_id,disease_id) values(7,1);
insert into doctor_disease(doctor_id,disease_id) values(7,2);
insert into doctor_disease(doctor_id,disease_id) values(7,3);
insert into doctor_disease(doctor_id,disease_id) values(7,4);
insert into doctor_disease(doctor_id,disease_id) values(7,5);
insert into doctor_disease(doctor_id,disease_id) values(7,6);


insert into doctor_disease(doctor_id,disease_id) values(8,1);
insert into doctor_disease(doctor_id,disease_id) values(8,3);
insert into doctor_disease(doctor_id,disease_id) values(8,5);

insert into doctor_disease(doctor_id,disease_id) values(9,2);
insert into doctor_disease(doctor_id,disease_id) values(9,4);
insert into doctor_disease(doctor_id,disease_id) values(9,6);


insert into doctor_disease(doctor_id,disease_id) values(10,1);
insert into doctor_disease(doctor_id,disease_id) values(10,2);
insert into doctor_disease(doctor_id,disease_id) values(10,3);
insert into doctor_disease(doctor_id,disease_id) values(10,4);


insert into doctor_disease(doctor_id,disease_id) values(11,5);
insert into doctor_disease(doctor_id,disease_id) values(11,6);

insert into doctor_disease(doctor_id,disease_id) values(12,1);
insert into doctor_disease(doctor_id,disease_id) values(12,2);
insert into doctor_disease(doctor_id,disease_id) values(12,3);
insert into doctor_disease(doctor_id,disease_id) values(12,4);


---------- Populate Doctor disease entries end -------------------


---------- Disease entries start -----------------------

delete from disease;
insert into disease(id,name) values(1,'Allergies');
insert into disease(id,name) values(2,'Colds and Flu');
insert into disease(id,name) values(3,'Conjunctivitis');
insert into disease(id,name) values(4,'Diarrhea');
insert into disease(id,name) values(5,'Headaches');
insert into disease(id,name) values(6,'Stomach Aches');
								   


---------- Disease entires end -------------------------



---------- Misc queries for testing ----------------

select * from curebox_user 

select * from user 

select * from doctor_specialization

select * from booking


select * from hospital
select * from doctor

select distinct h.location 
from hospital h join doctor d on h.id = d.hospital_id
order by 1

select distinct doc.fees , u.name 
from doctor_disease dd natural join doctor doc natural join curebox_user u , hospital h where  UPPER(u.name) like UPPER('doctor1')
and dd.disease_id = (select disease_id from disease d where d.name = 'Colds and Flu')
and doc.provide_covid_care = true
and doc.hospital_id = h.id and h.location = 'Bloomington'

select * from doctor_disease dd
where dd.disease_id = (select d.id from disease d where d.name = 'Colds and Flu') ;

select distinct doc.fees , u.name 
from doctor_disease dd natural join doctor doc natural join curebox_user u , hospital h where 
1 = 1 and
dd.doctor_id = doc.id and dd.disease_id = (select d.id from disease d where d.name = 'Colds and Flu') ;


select * from doctor 

select distinct doc.fees , u.name
from doctor_disease dd natural join doctor doc natural join curebox_user u , hospital h 
where 1 = 1 and dd.doctor_id = doc.id 
and dd.disease_id = (select disease_id from disease d where d.name = 'Colds and Flu')
and doc.hospital_id = h.id and h.location = 'Bloomington'*/