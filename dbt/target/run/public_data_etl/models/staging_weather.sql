
  create view "weather_values"."weather"."staging_weather__dbt_tmp"
    
    
  as (
    --staging_weather.sql
select
    city,
    temp as temperature,
    humidity,
    weather,
    timestamp::timestamp as recorded_at
from "weather_values"."public"."weather"
  );