SELECT
    user_id,
    CONCAT(Upper(left(name, 1)), Lower(substring(name, 2))) AS name
FROM
    users
ORDER BY
    user_id
;

-- concat 2 parts of the raw name
-- part 1: the first letter in upper case
-- part 2: the rest letters in lower case