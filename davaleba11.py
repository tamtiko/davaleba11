CREATE TABLE MyTable (
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Column1 VARCHAR(50),
    Column2 VARCHAR(50),
    Column3 VARCHAR(50)
);

CREATE INDEX MyIndex ON MyTable (Column1);

SELECT * FROM MyTable WHERE Column1 = 'value';

EXPLAIN SELECT * FROM MyTable WHERE Column1 = 'value';
