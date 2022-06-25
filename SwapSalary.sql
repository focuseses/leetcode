-- swap values in SQL 
UPDATE Salary
SET sex = CASE WHEN gender = 'm' THEN 'f' 
                  WHEN gender = 'f' THEN 'm'
                  ELSE gender END