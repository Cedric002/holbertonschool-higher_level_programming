-- creates the MySQL server user user_0d_1 with all privileges for user_0d_1
-- and password should be set to user_0d_1_pwd
CREATE USER 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;