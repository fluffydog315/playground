-- cities =
-- | state      | city          |
-- | ---------- | ------------- |
-- | California | Los Angeles   |
-- | California | San Francisco |
-- | California | San Diego     |
-- | Texas      | Houston       |
-- | Texas      | Austin        |
-- | Texas      | Dallas        |

-- concat cities, mysql=> group_concat
select state, string_agg(city, ', ' order by city) as cities
from cities
group by state
order by state

-- bitwise, leetcode 3204
-- user_permissions =
-- | user_id | permissions |
-- | ------- | ----------- |
-- | 1       | 5           |
-- | 2       | 12          |
-- | 3       | 7           |
-- | 4       | 3           |
select bit_and(permissions) as common_perms
, bit_or(permissions) as any_perms
from user_permissions


-- time diff 
-- diff by secounds
extract(epoch from s2.session_start) => return seconds
--count week
extract(week from p.purchase_date) - extract(week from '2023-11-01'::timestamp) + 1 as week_of_month 
 
--20 days ago
current_date - interval '10 days' 
date_part('year', col)
date_part('month',col)
--one day before 
action_date: datetime
t.action_date::date - e.signup_date::date = 1