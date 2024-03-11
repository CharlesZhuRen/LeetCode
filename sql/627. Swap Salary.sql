UPDATE salary
SET sex = IF(sex="m", "f", "m")
;

-- if sex=m, then set sex=f
-- else(i.e. sex=f) set sex=m
