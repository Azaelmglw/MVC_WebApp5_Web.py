dropdb App5_DB;
createdb App5_DB;
psql App5_DB;

CREATE TABLE clients(
c_id                serial      NOT NULL    PRIMARY KEY,
c_name              varchar(25) NOT NULL,
c_gender            char(1)     NOT NULL    DEFAULT 'M',
c_phone_number      char(10)    NOT NULL,
c_occupation        varchar(25) NOT NULL
);

CREATE TABLE products(
    p_id            serial          NOT NULL    PRIMARY KEY,
    p_name          varchar(25)     NOT NULL,
    p_description   text            NOT NULL,
    p_brand         varchar(15)     NOT NULL,
    p_origin        varchar(25)     NOT NULL
);


INSERT INTO products(p_name, p_description, p_brand, p_origin)
VALUES
('Time Machine',        'Extremely useful tool whenever you need to undo a regrettable moment in your life',              'TrustWorthy',  'China'),
('Teleporter',          'Want to always be on time, with this you will need better excuses when getting late at work',    'CheapStuff',   'Germany'),
('Presidential Jet',    'Luxurius airplane made for the one and only reason to cause envy between your coworkers',        'DownWeGo',     'Malaysia');


CREATE ROLE "Boris" WITH LOGIN PASSWORD 'pos';
GRANT ALL PRIVILEGES ON clients, products TO Boris;
GRANT ALL PRIVILEGES ON SEQUENCE clients_c_id_seq, products_p_id_seq TO "Boris";