CREATE TABLE `students`  ( `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT , `name` VARCHAR(30) Not NULL , `dob` TIME , `age` TINYINT );


INSERT INTO `students` ( `name` , `dob` , `age`   ) VALUES
 ("mary",'1999-8-20','23'),
("chan",'1999-9-20','22');


update `students` set `name`="chan" where `id` = 2;