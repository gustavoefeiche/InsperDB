USE InsperDB;
DROP TABLE IF EXISTS student_organization;
CREATE TABLE student_organization (
  ID INT NOT NULL AUTO_INCREMENT, 
  nome VARCHAR(100) NOT NULL,
  creationDate DATETIME,
  PRIMARY KEY (ID)
);