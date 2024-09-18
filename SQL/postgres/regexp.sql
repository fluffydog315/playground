--tweet = "Enjoying a great start to the day. #HappyDay #MorningVibes"
-- Tweets =
-- | user_id | tweet_id | tweet                                                      | tweet_date |
-- | ------- | -------- | ---------------------------------------------------------- | ---------- |
-- | 135     | 13       | Enjoying a great start to the day. #HappyDay #MorningVibes | 2024-02-01 |
-- | 136     | 14       | Another #HappyDay with good vibes! #FeelGood               | 2024-02-03 |


/*
Count the top 3 hashtag in Feb 2024
*/
--method 1
with cte as (select regexp_split_to_table(tweet, '\s') as tag 
from tweets), 
cte2 as (select * from cte where tag like '#%')

select tag as hashtag, count(*) as count 
from cte2 group by tag 
order by count desc, tag desc 
limit 3

--method 2

with cte as (
    select unnest(string_to_array(tweet, ' ')) as tweet
    from tweets
    where date_part('year',tweet_date) = 2024
    and date_part('month',tweet_date) = 2 
    
), cte2 as (select * from cte where tweet like '#%')

select tweet as hashtag, count(*) as count
from cte2 
group by 1 
order by 2 desc, 1 desc 
limit 3

-- regexp: 
--regexp_matches: 'g' for multiple matches 
with cte as (
    SELECT regexp_matches(tweet, '(#[A-Za-z0-9]+)', 'g') as hashtag 
    from tweets )


select hashtag, count(*) as count 
from cte 
group by 1 
order by count desc, 1 desc 
limit 3


--regexp only return first item not items

with cte as (select substring(tweet, '#[\w]+') as tag,  (regexp_match(tweet, '(#([A-Za-z0-9_]+))'))[1] as reg, count(*) as cnt
from tweets 
where date_part( 'year', tweet_date ) = '2024' 
and date_part('month' , tweet_date) = '2'
group by 1,2)


--select * from cte
select tag as hashtag, cnt as hashtag_count 
from cte 
order by 2 desc, 1 desc
limit 3;

