CREATE TABLE table_m3 (
    id SERIAL PRIMARY KEY,
    "Country" VARCHAR(255),           
    "City" VARCHAR(255),          
    "AQI Value" INT,                  
    "AQI Category" VARCHAR(100),  
    "CO AQI Value" INT,          
    "CO AQI Category" VARCHAR(100),   
    "Ozone AQI Value" INT,            
    "Ozone AQI Category" VARCHAR(100),
    "NO2 AQI Value" INT,              
    "NO2 AQI Category" VARCHAR(100),  
    "PM25 AQI Value" INT,             
    "PM25 AQI Category" VARCHAR(100), 
    "lat" DECIMAL(9,4),              
    "lng" DECIMAL(9,4)  
);


COPY p2m3_dhani_data_raw
FROM '/Users/achmaddhani/projects/milestone/p2-ftds009-hck-m3-achmaddhani/P2M3_Dhani_data_raw.csv'
DELIMITER ','
CSV HEADER;