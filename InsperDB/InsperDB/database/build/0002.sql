USE InsperDB;
CREATE TABLE Person (
  ID INT NOT NULL AUTO_INCREMENT, 
  Person_email VARCHAR(100) NOT NULL,
  Person_password VARCHAR(100) NOT NULL,
  Valid VARCHAR(100) NOT NULL,
  PRIMARY KEY (ID)
);

