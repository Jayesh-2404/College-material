-- SELECT employee_id, first_name , salary
-- FROM public.employees;

-- 2nd question 
-- SELECT employee_id , first_name 
-- FROM public.employees
-- WHERE manager_id = 100;


-- 3rd question
-- SELECT employee_id , first_name 
-- FROM public.employees
-- WHERE salary>=4800;

-- 4th question
-- SELECT employee_id , first_name
-- FROM public.employees
-- WHERE last_name = 'Austin';

-- 5th question

-- SELECT employee_id , first_name
-- FROM public.employees
-- WHERE department_id = 60 OR department_id = 70 OR department_id = 80;


-- unique manager id 
SELECT DISTINCT manager_id
FROM public.employees;

