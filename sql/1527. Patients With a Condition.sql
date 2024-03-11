SELECT
    *
FROM
    Patients
WHERE
    conditions LIKE "DIAB1%"
    OR conditions LIKE "% DIAB1%"
;

-- for the reason that conditions are seperated by space
-- we only need to judge if the first condition starts with "DIAB1" i.e.conditions like "DIAB1%"
-- or if one of the conditions (except the first condition) starts with "DIAB1" i.e. condition like "% DIAB1%"