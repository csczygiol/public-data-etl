-- fct_avg_temp_by_city.sql
select
    city,
    date_trunc('day', recorded_at) as day,
    avg(temperature) as avg_temperature
from "weather_values"."weather"."staging_weather"
group by city, day