
# SQL

## Commands

```sql
CREATE TABLE SpotifyExtendedStreamingHistory (
    ts DATETIME,
    platform NVARCHAR(255),
    ms_played INT,
    conn_country NVARCHAR(2),
    ip_addr NVARCHAR(16),
    master_metadata_track_name NVARCHAR(255),
    master_metadata_album_artist_name NVARCHAR(255),
    master_metadata_album_album_name NVARCHAR(255),
    reason_start NVARCHAR(32),
    reason_end NVARCHAR(32),
    shuffle BIT,
    skipped BIT
);
```

```sql
INSERT INTO SpotifyExtendedStreamingHistory (
    ts,
    ms_played,
    conn_country,
    master_metadata_track_name,
    master_metadata_album_artist_name,
    master_metadata_album_album_name
) VALUES (
    '2019-07-21 18:29:36.000',
     242430,
    'MX',
    'Gethsemane',
    'Sleep Token',
    'Even In Arcadia'
)
```

```sql
UPDATE SpotifyExtendedStreamingHistory
SET conn_country = 'Mexico'
WHERE conn_country = 'MX';
```

```sql
DELETE FROM SpotifyExtendedStreamingHistory
WHERE master_metadata_album_artist_name IS NULL;
```

```sql
ALTER TABLE SpotifyExtendedStreamingHistory
    -- ADD liked BIT
    -- ALTER COLUMN conn_country VARCHAR(255)
    -- DROP COLUMN ip_addr
```

### More commands

- `UNION ALL`: Concatenates two tables.
- `LEFT JOIN`: Return all rows from the left table, even if there is no match with the right table.

