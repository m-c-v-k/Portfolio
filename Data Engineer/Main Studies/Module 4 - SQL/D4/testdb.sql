DROP TABLE IF EXISTS address_list;
CREATE TABLE IF NOT EXISTS address_list (
name VARCHAR(50),
phone VARCHAR(50),
email VARCHAR(50)
);
INSERT INTO address_list
VALUES
('Åke Bråk', '071-117 17 19', 'aaake@combort.com', 1),
('George Beast', '0246-123 456', 'thebest789@bullhead.com', 2),
('Sven Dufva', '077-777 77 77', 'sven.dufva@sputnik.fi', 3);
SELECT * FROM address_list;
