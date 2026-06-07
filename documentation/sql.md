
# SQL

**Structured Query Language** (**SQL**) is a language used to manage data, especially in a relational database management system (RDBMS). It is particularly useful in handling structure data.

### Quick links

- [Cheat Sheet](https://www.geeksforgeeks.org/sql/sql-cheat-sheet/)

## Commands

### Structure of a SQL server 

```
<server>
    <database>
        <tables>
            <columns>
            <records>
        <views>
```

### Databases

```SQL
CREATE DATABASE <database>; -- Create a database
USE <database>; -- Reference tables from a specific database moving forwards
DROP DATABASE <database>; -- Delete a database
```

### Tables

```SQL
CREATE TABLE <table> (
    <column> <data_type> <constrain>
);
```

| Data type | Description |
| - | - |
| `BOOL` | A value of zero is considered as false, nonzero value are considered true. |
| `INT` | A normal-size integer. |
| `FLOAT` | A small floating-point number. |
| `CHAR(size)` | A fixed-length string. *size* specifies the column length in characters from 0 to 255. |
| `VARCHAR(size)` | A variable-length strin. *size* specifies the maximum column length in characters, from 0 to 65535.
| `DATETIME` | A date and time combination formatted as `YYYY-MM-DD hh:mm:ss`. |
| `DATE` | A date formatted as `YYYY-MM-DD`. |
| `TIME` | A time formatted as `hh:mm:ss` |
| `ENUM(val1, ...)` | A string object that can have only one value, chosen from the list of possible values. |
| `SET(val1, ...)` | A string object that can have zero or more values, chosen from the list of possible values. |

| Constrains | Description |
| - | - |
| `PRIMARY KEY` | Each record has a unique identifier. |
| `UNIQUE` | The column must contain unique values for each record. |
| `NOT NULL` | The column must have values and cannot be `NULL` |
| `CHECK (<condition>)` | The value must meet the condition. |

```SQL
ALTER TABLE <table>
    ADD <column> <data_type> -- Add a column
    ALTER COLUMN <column> <data_type> -- Change the data type of a column
    DROP COLUMN <column> -- Delete a column
```

```SQL
DROP TABLE <table>;
```

### Read data

```SQL
SELECT * FROM <table>
WHERE <condition> -- Filter data
LIMIT <limit> -- Set a limit for fetched records
```

### Manipulate data

```SQL
INSERT INTO <table_name> (<column>) 
VALUES 
    (<value>);
```

```SQL
UPDATE <table>
SET <column> = <value>
WHERE <condition>
```

```SQL
DELETE FROM <table>
WHERE <condition>
```

### Filtering data

```SQL
SELECT * FROM <table>
WHERE 1 = 1
    AND <column> = <value> -- Column equals value
    AND <string_column> LIKE '%{substring}%' -- String includes a substring
    AND <column> IN (<value>, <value>) -- Included in set
    AND <column> BETWEEN <min_value> AND <max_value>
    AND <column> IS NULL
```

```SQL
SELECT * FROM <table>
GROUP BY <column>
ORDER BY <column> ASC/DESC;
```

### Joins

```SQL
SELECT * FROM 
<left_table> <join_type> JOIN <right_table>
ON <condition>
```

| Join Type | Description |
| - | - |
| `LEFT/RIGHT JOIN` | Return all rows from the left/right table, even if there is no match with the other table. |
| `INNER JOIN` | Retrieves records from both tables where there is a match. |
| `FULL OUTER JOIN` | This retrieves all records, including unmatched records. |

- `UNION ALL`: Concatenates two tables.

### Functions

| Type | Functions |
| - | - |
| Aggregation | `COUNT` `SUM` `AVG` `MIN` `MAX` |
| Scalar | `UPPER/LOWER` |
| String | `CONCAT` `SUBSTRING` `LEFT/RIGHT` |
| Mathematical | `SQRT` |
| Date and time | `CURRENT_DATE` |

### Views

```SQL
CREATE VIEW <view> AS (
    SELECT * FROM <table>
);
DROP VIEW IF EXISTS <view>;
```

### Common Table Expressions (CTEs)

```SQL
WITH <CTE> AS (
    SELECT * FROM <table>
)
SELECT * FROM <CTE>;
```

### Missing topics

- Transactions: `BEGIN TRANSACTION` `COMMIT` `ROLLBACK`
- Procedures: `CREATE PROCEDURE <procedure>()`
- Triggers: `CREATE TRIGGER <trigger>`
