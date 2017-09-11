DROP USER IF EXISTS InsperDBUser@localhost;
flush privileges;
CREATE USER 'InsperDBUser'@'localhost' IDENTIFIED BY 'InsperDatabase404!';
GRANT ALL PRIVILEGES ON insperdb . * TO 'InsperDBUser'@'localhost';
REVOKE DROP ON insperdb.* FROM 'InsperDBUser'@'localhost';
flush privileges;