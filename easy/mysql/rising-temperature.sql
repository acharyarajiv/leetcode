# Write your MySQL query statement below
select curr_day.Id 
from Weather curr_day
join Weather prev_day on DATEDIFF(curr_day.RecordDate, prev_day.RecordDate) = 1 
where curr_day.Temperature > prev_day.Temperature