CREATE TABLE IF NOT EXISTS user (
   username VARCHAR(255) PRIMARY KEY,
   password VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS account (
   username VARCHAR(255) PRIMARY KEY,
   amount DECIMAL(19,4),
);

CREATE TABLE IF NOT EXISTS plan (
   username VARCHAR(255),
   plan_name VARCHAR(255),
   percent DECIMAL(4,2)
   PRIMARY KEY (username, plan_name)
);

