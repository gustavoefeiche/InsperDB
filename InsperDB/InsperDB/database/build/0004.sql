USE InsperDB;
DROP TABLE IF EXISTS student_has_organization;

CREATE TABLE student_has_organization (

    ID_student INT NOT NULL,
    ID_organization INT NOT NULL,
    
    
	FOREIGN KEY (ID_student)
		REFERENCES person(ID),
        
	FOREIGN KEY (ID_organization)
		REFERENCES student_organization(ID),
        
	PRIMARY KEY ( ID_student, ID_organization)
);
