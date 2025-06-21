--staging_weather.sql
select
    city,
    temp as temperature,
    humidity,
    weather,
    timestap::timestap as recorded_at
from {{ source('weather_source', 'weather') }}