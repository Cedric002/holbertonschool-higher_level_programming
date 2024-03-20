-- creates the MySQL server user user_0d_1 with all privileges for user_0d_1
-- and password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS @user@'localhost' IDENTIFIED BY @password;
GRANT ALL PRIVILEGES ON *.* TO @user@'localhost';
FLUSH PRIVILEGES;