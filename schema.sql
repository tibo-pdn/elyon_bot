CREATE DATABASE IF NOT EXISTS elyon_db;

USE elyon_db;

CREATE TABLE IF NOT EXISTS user (
    uuid VARCHAR(255) NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,

    u_gear INT NOT NULL,
    u_level INT NOT NULL,
    u_skill INT NOT NULL,

    r_red INT NOT NULL,
    r_orange INT NOT NULL,
    r_yellow INT NOT NULL,
    r_blue INT NOT NULL,
    r_green INT NOT NULL,
    r_purple INT NOT NULL
);