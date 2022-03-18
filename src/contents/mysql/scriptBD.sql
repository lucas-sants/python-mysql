/** DROP DATABASE python_db; **/
/** CREATE SCHEMA python_db; **/

CREATE TABLE python_db.students (
	`id_student` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(20) NOT NULL,
    `cpf` VARCHAR(11) NOT NULL,
    PRIMARY KEY (`id_student`)
);

INSERT INTO python_db.students VALUES (DEFAULT, 'Fulano', '12345678910');

SELECT * FROM python_db.students;