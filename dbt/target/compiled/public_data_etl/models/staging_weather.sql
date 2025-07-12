--staging_weather.sql
select
    city,
    temp as temperature,
    humidity,
    weather,
    timestamp::timestamp as recorded_at
from "weather_values"."public"."weather"