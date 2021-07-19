use chinook;

CREATE TABLE If Not Exists employees_audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employeeNumber INT NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);

DROP TRIGGER before_employee_update ;

CREATE TRIGGER before_employee_update 
    BEFORE UPDATE ON Employee
    FOR EACH ROW 
 INSERT INTO employees_audit
 SET action = 'update',
     EmployeeNumber = OLD.EmployeeId,
     lastname = OLD.lastname,
     changedat = NOW();
     
SELECT NOW();

SHOW TRIGGERS;

UPDATE Employee 
SET 
    lastName = 'Phan'
WHERE
    employeeId = 1711;
    
SELECT * FROM employees_audit;

SELECT * FROM Employee;