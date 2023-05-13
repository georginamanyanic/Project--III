CREATE DATABASE IF NOT EXISTS educacion;
DROP DATABASE educacion;
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

    
ALTER TABLE superficie
	RENAME COLUMN `index` TO id_superficie,
	MODIFY COLUMN Any YEAR,
	MODIFY COLUMN Codi_Districte INT,
    MODIFY COLUMN Codi_Barri INT unsigned,
    MODIFY COLUMN `superfície (ha)` FLOAT,
    MODIFY COLUMN superficie_km2 FLOAT,
    ADD PRIMARY KEY (id_superficie),
    ADD FOREIGN KEY (Codi_Barri) REFERENCES codigos(Codi_Barri);
    
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
    
-- Crear una tabla de codigos por distrito
CREATE TABLE codigos_distritos AS 
	SELECT DISTINCT(Codi_Districte), Nom_Districte FROM codigos;
ALTER TABLE codigos_distritos
ADD PRIMARY KEY (Codi_Districte);
    
-- Hipótesis 1: 
	-- 	Query 1: Nivel de estudios total de BCN
    SELECT Any, Nivell_academic, SUM(Nombre) AS num_personas FROM educacion_barrios
		WHERE Any <= 2019
		GROUP BY Any, Nivell_academic;
        
	-- Query 2: Nivel de estudios total de BCN para calcular la tasa de crecimiento
    SELECT Any, Nivell_academic, SUM(Nombre) AS num_personas FROM educacion_barrios
        WHERE Any = 2009 or Any = 2019
        GROUP BY Any, Nivell_academic;
        
	-- Query 3: Nivel de estudios por distrito
    SELECT Any, Nivell_academic, Codi_Districte, Nom_Districte, SUM(Nombre) AS num_personas 
		FROM educacion_barrios
		WHERE ANY <= 2019
		GROUP BY Any, Nivell_academic, Codi_Districte, Nom_Districte;
        
	-- Query 4: Nivel de esetudios por barrios y sexos
    SELECT Any, Codi_Districte, Nom_Districte, Codi_Barri, Nom_Barri, Nivell_academic, Sexe,
		SUM(Nombre) as num_personas FROM {table_name}
		WHERE Any <= 2019
		GROUP BY Any, Codi_Districte, Nom_Districte, Codi_Barri, Nom_Barri, Nivell_academic, Sexe; 
        
-- Hipótesis 2: 
	-- Query1: 
    SELECT * FROM renta_distritos;
    SELECT * FROM renta_barrios; 
    
        




    

    
    

    


