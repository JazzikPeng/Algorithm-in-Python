
/* Write your MySQL query statement below */
SELECT DISTINCT
    l1.Num AS ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num
;

/* Faster solution */
select distinct a.num as ConsecutiveNums
from (select num, (case when @record = num then @count := @count + 1
                          when @record := num then @count := 1
                    end) as count_result
      from Logs, (select @record := null, @count := 0) b
      ) a
where a.count_result >= 3;