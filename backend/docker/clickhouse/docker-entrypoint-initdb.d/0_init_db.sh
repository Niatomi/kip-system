#!/bin/bash
set -e
clickhouse client -n <<-EOSQL
CREATE DATABASE kip_system_db ENGINE = Memory COMMENT 'Database for kip';

CREATE TABLE kip_system_db.events
(
    id UUID
) ENGINE = MergeTree()
ORDER BY tuple();
CREATE DATABASE kip_system_db_test ENGINE = Memory COMMENT 'Database for kip';
CREATE TABLE kip_system_db_test.events
(
    id UUID
) ENGINE = MergeTree()
ORDER BY tuple();
EOSQL