# Query and Subquery
select *  from employee_id where id_number in 
(select id_number from employee_info where state="GA");
# Inner Join
select fname, lname from employee_id a inner join employee_info b on a.id_number=b.id_number;
# Left Join
select a.id_number, a.fname, a.lname, b.next_kin from employee_id a left join employee_info b on a.id_number = b.id_number;
# Right Join
select a.id_number, a.fname, a.lname, b.next_kin from employee_id a right join employee_info b on a.id_number = b.id_number;
# Self Join
select a.id_number, a.fname, a.lname, b.mname, b.prefix from employee_id a inner join employee_id b on a.lname = b.lname;
# Full Join equivalent (as MySQL does not support Full Join)
select * from employee_id
left join employee_info on employee_id.id_number = employee_info.id_number
union
select * from employee_id
right join employee_info on employee_id.id_number = employee_info.id_number;
