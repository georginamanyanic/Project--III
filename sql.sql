CREATE DATABASE IF NOT EXISTS educacion;

USE educacion;

-- Modificar tipo de datos de las tablas : 
ALTER TABLE codigos
	DROP COLUMN `index`,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Codi_Barri INT unsigned,
    MODIFY COLUMN Nom_Districte VARCHAR(30),
    MODIFY COLUMN Nom_Barri VARCHAR(50),
    ADD PRIMARY KEY (Codi_Barri);
    
ALTER TABLE educacion_barrios
	RENAME COLUMN `index` TO id_educacion_barrios,
	MODIFY Any YEAR,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Codi_Barri INT unsigned,
    MODIFY COLUMN Nombre INT,
    ADD PRIMARY KEY (id_educacion_barrios),
	ADD FOREIGN KEY (Codi_Barri) REFERENCES codigos (Codi_Barri);
    
ALTER TABLE educacion_distritos
	RENAME COLUMN `index` TO id_educacion_distritos,
	MODIFY Any YEAR,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Nombre INT,
    ADD PRIMARY KEY (id_educacion_distritos);
    
ALTER TABLE superficie
	RENAME COLUMN `index` TO id_superficie,
	MODIFY COLUMN Any YEAR,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Codi_Barri INT unsigned,
    MODIFY COLUMN `superfície (ha)` FLOAT,
    MODIFY COLUMN superficie_km2 FLOAT,
    ADD PRIMARY KEY (id_superficie),
    ADD FOREIGN KEY (Codi_Barri) REFERENCES codigos_barrios (Codi_Barri);
    
ALTER TABLE renta_barrios
	RENAME COLUMN `index` TO id_renta_barrios,
	MODIFY COLUMN Any YEAR,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Codi_Barri INT UNSIGNED,
    MODIFY COLUMN Import_€_Any FLOAT,
    ADD PRIMARY KEY (id_renta_barrios),
    ADD FOREIGN KEY (Codi_Barri) REFERENCES codigos (Codi_Barri);
    
ALTER TABLE renta_distritos
	RENAME COLUMN `index` TO id_renta_distritos,
	MODIFY COLUMN Any YEAR,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Import__Any FLOAT,
    ADD PRIMARY KEY (id_renta_distritos);
    
ALTER TABLE renta_barcelona
	RENAME COLUMN `index` TO id_renta_barcelona,
	MODIFY COLUMN Any YEAR,
    MODIFY COLUMN Import_€_Any FLOAT,
    ADD PRIMARY KEY (id_renta_barcelona);
    

    
ALTER TABLE equipamientos
	MODIFY COLUMN addresses_neighborhood_id INT unsigned,
    MODIFY COLUMN cantidad_equipamientos INT unsigned,
    ADD FOREIGN KEY (addresses_neighborhood_id) REFERENCES codigos (Codi_Barri);
    

    


