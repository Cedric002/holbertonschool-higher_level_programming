-- Create the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on server.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);