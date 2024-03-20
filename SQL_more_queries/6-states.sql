-- Create the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your server.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY(id)
);