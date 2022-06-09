SELECT
    firstname, lastname, city, state
FROM
    person AS p LEFT JOIN address AS a ON p.personid = a.personid
;

-- use LEFT JOIN so that if the address of a person id is not present in the address table, null will be reported