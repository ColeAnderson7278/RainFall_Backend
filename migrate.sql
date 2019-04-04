CREATE TABLE IF NOT EXISTS scores (
    id SERIAL NOT NULL PRIMARY KEY,
    name TEXT NOT NULL,
    number INTEGER NOT NULL
);

-- DO $$
-- BEGIN
-- IF NOT EXISTS (SELECT * FROM scores) THEN
--     INSERT INTO scores (name, number) VALUES
--     ('Henry', 42000);
-- END IF;
-- END$$;


