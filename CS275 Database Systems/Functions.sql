# Numeric Functions Demonstration
-- ACOS(x): Returns the cosine of X
select acos(0);
-- ATAN(x): Returns the arc tangent of X
select atan(4);
-- EXP(x): Returns the value of e raised to the power of X
select EXP(2);

# Time and Date Functions
-- UTC TIMESTAMP(): Returns the current UTC Time and Date in format "YYYY-MM-DD hh:mm:ss"
select utc_timestamp();
-- MAKEDATE(year, day of year): Create a date from year and day of year
select makedate(2012, 52);
-- QUARTER(date): Returns the quarter of input date
select quarter('2006-8-01');

# String Functions
-- CHAR_LENGTH(string): Returns length of string in characters
select char_length('Supercalifragilisticexpialidocious');
-- REVERSE(string): Reverses string
select reverse('Supercalifragilisticexpialidocious');
-- CONCAT('string', 'string', 'string'): Concatenates strings
select concat('Brady', ' Alexander', ' Esplin');