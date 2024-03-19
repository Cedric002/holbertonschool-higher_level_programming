-- creates the MySQL server user user_0d_1 with all privileges for user_0d_1
-- and password should be set to user_0d_1_pwd
SELECT EXISTS (SELECT DISTINCT user FROM mysql.user WHERE user = 'user_0d_1') as is_user;

IF NOT EXISTS (SELECT DISTINCT user FROM mysql.user WHERE user = 'user_0d_1') THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
END IF;

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;