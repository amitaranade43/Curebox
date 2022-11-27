
---------- Populate Doctor entries start -------------------
delete from doctor 
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('2',1,20,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('3',1,40,FALSE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('4',2,60,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('5',2,40,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('6',3,50,FALSE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('7',4,70,TRUE);

---------- Populate Doctor entries end -------------------

---------- Populate Doctor entries start -------------------
delete from doctor 
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('2',1,20,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('3',1,40,FALSE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('4',2,60,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('5',2,40,TRUE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('6',3,50,FALSE);
insert into doctor(id,hospital_id,fees,provide_covid_care) values ('7',4,70,TRUE);

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

insert into doctor_disease(doctor_id,disease_id) values(2,1);
insert into doctor_disease(doctor_id,disease_id) values(2,2);
insert into doctor_disease(doctor_id,disease_id) values(2,3);
insert into doctor_disease(doctor_id,disease_id) values(2,4);
insert into doctor_disease(doctor_id,disease_id) values(2,5);
insert into doctor_disease(doctor_id,disease_id) values(2,6);


insert into doctor_disease(doctor_id,disease_id) values(3,1);
insert into doctor_disease(doctor_id,disease_id) values(3,3);
insert into doctor_disease(doctor_id,disease_id) values(3,5);

insert into doctor_disease(doctor_id,disease_id) values(4,2);
insert into doctor_disease(doctor_id,disease_id) values(4,4);
insert into doctor_disease(doctor_id,disease_id) values(4,6);


insert into doctor_disease(doctor_id,disease_id) values(5,1);
insert into doctor_disease(doctor_id,disease_id) values(5,2);
insert into doctor_disease(doctor_id,disease_id) values(5,3);
insert into doctor_disease(doctor_id,disease_id) values(5,4);


insert into doctor_disease(doctor_id,disease_id) values(6,5);
insert into doctor_disease(doctor_id,disease_id) values(6,6);

insert into doctor_disease(doctor_id,disease_id) values(7,1);
insert into doctor_disease(doctor_id,disease_id) values(7,2);
insert into doctor_disease(doctor_id,disease_id) values(7,3);
insert into doctor_disease(doctor_id,disease_id) values(7,4);


select * from doctor

select * from disease 



---------- Populate Doctor disease entries end -------------------


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
and doc.hospital_id = h.id and h.location = 'Bloomington'