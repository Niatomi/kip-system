CREATE DATABASE IF NOT EXISTS kip_system_db ENGINE = MergeTree COMMENT 'Database for prod';
CREATE TABLE IF NOT EXISTS kip_system_db.events (id UUID) ENGINE = MergeTree() ORDER BY tuple();
