-- CREATE DATABASE tyotunnit;
SELECT NOW()

-- CREATE TABLE tyo_taulu (
--     id              SERIAL PRIMARY KEY,
--     nimi            varchar(255) NOT NULL,
--     alku            TIMESTAMP NOT NULL,
--     loppu           TIMESTAMP NOT NULL,
--     projekti_nimi   varchar(255) NOT NULL,
--     selite          varchar NOT NULL
-- );

INSERT INTO tyo_taulu
    (nimi,alku,loppu,projekti_nimi,selite) 
    VALUES ("matti","2022-03-08 13:07:43.14758+02","2022-03-09 13:07:43.14758+02","blabla","blablabla");
    
select *, to_char(createddate, 'yyyymmdd hh:mi:ss tt') as created_date
from "Group"