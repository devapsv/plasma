import ibm_db

connection=ibm_db.connect("DATABASE=bludb;HOSTNAME=6667d8e9-9d4d-4ccb-ba32-21da3bb5aafc.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30376;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=bjq36094;PWD=UHlt6tExajsxU4x0",'','')





sql=""" CREATE TABLE DONAR (
    id varchar(255),
    name varchar(255),
    phone varchar(255) ,
    email varchar(255) ,
    password varchar(255),
    age varchar(255),
    blood_group varchar(255),
    weight varchar(255),
    parasitic varchar(255),
    hiv varchar(255),
    blood_disease varchar(255),
    drugs varchar(255),
    vaccine varchar(255),
    overall_health varchar(255),
    donated_plasma varchar(255),
    date varchar(255)
    
    
    
    
     )  """
ibm_db.exec_immediate(connection,sql)





print("All inserted")