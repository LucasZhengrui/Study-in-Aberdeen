SELECT emp_id, emp_name, emp_age, dept_id
INTO Employee_info
FROM Employee;

SELECT dept_id, dept_name, dept_info
INTO Department
FROM Employee;

ALTER TABLE Employee_info
ADD PRIMARY KEY (emp_id);

ALTER TABLE Department
ADD PRIMARY KEY (dept_id);

SELECT E.emp_id, E.emp_name, d.dept_name, d.dept_info
FROM Employee_info E, Department d
WHERE E.dept_id = d.dept_id;
