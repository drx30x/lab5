CREATE SCHEMA service_it;
CREATE TABLE service_it.users (id SERIAL NOT NULL, full_name VARCHAR NOT NULL, login VARCHAR NOT NULL UNIQUE, password VARCHAR NOT NULL);
INSERT INTO service_it.users (full_name, login, password) VALUES
('Ivan Ivanov','Ivanov01', '123456'),
('Иванов Владимир', 'ASWQ111', 'cherry'),
('Николаев Арнольд', 'arnold656', 'qwerty123'),
('Юриев Петр', 'petya000', 'qwerty'),
('Золотов Сергей', 'sergeizolotov', 'password123'),
('Троицкий Кирилл', 'audirw', 'banana'),
('Лиханов Олег', 'oleglihanov', 'zxcvbnm'),
('Гордеев Юрий', 'usbtypec', 'qwerty111'),
('Перов Леонид', 'absurdism', 'password5'),
('Иванов Петр', 'ivanov111', 'qwerty12345');