CREATE DATABASE IF NOT EXISTS kip_system_db_test ENGINE = MergeTree COMMENT 'Database for prod';
CREATE TABLE IF NOT EXISTS kip_system_db_test.events (id UUID) ENGINE = MergeTree() ORDER BY tuple();