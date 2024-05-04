-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Апр 23 2024 г., 14:13
-- Версия сервера: 8.0.19
-- Версия PHP: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `airport_gaponenko_22`
--
CREATE DATABASE IF NOT EXISTS `airport_gaponenko_22` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `airport_gaponenko_22`;

-- --------------------------------------------------------

--
-- Структура таблицы `pilot`
--

CREATE TABLE `pilot` (
  `id_pil` int NOT NULL,
  `fio` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `samolet`
--

CREATE TABLE `samolet` (
  `id_sam` int NOT NULL,
  `year` date NOT NULL,
  `model` text NOT NULL,
  `capacity` text NOT NULL,
  `ircraft_coode` text NOT NULL,
  `type` text NOT NULL,
  `a_country` text NOT NULL,
  `engine` text NOT NULL,
  `weight` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `samolet`
--

INSERT INTO `samolet` (`id_sam`, `year`, `model`, `capacity`, `ircraft_coode`, `type`, `a_country`, `engine`, `weight`) VALUES
(1, '2010-10-14', 'ЕЕ72210 ', '100', '186GP', 'passenger', 'USA', 'PW4000', 55300);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `pilot`
--
ALTER TABLE `pilot`
  ADD PRIMARY KEY (`id_pil`);

--
-- Индексы таблицы `samolet`
--
ALTER TABLE `samolet`
  ADD PRIMARY KEY (`id_sam`),
  ADD KEY `weight` (`weight`);
--
-- База данных: `airport_kuchiev_23`
--
CREATE DATABASE IF NOT EXISTS `airport_kuchiev_23` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `airport_kuchiev_23`;

-- --------------------------------------------------------

--
-- Структура таблицы `самолет`
--

CREATE TABLE `самолет` (
  `id_sam` int NOT NULL,
  `id_model` text NOT NULL,
  `id_pil` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
--
-- База данных: `airport_stepanchenko_27`
--
CREATE DATABASE IF NOT EXISTS `airport_stepanchenko_27` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `airport_stepanchenko_27`;

-- --------------------------------------------------------

--
-- Структура таблицы `airports`
--

CREATE TABLE `airports` (
  `id_airport` int NOT NULL,
  `id_employers` int NOT NULL,
  `id_race` int NOT NULL,
  `Name` text NOT NULL,
  `Country` text NOT NULL,
  `City` text NOT NULL,
  `Organization` text NOT NULL,
  `Services_organization` text NOT NULL,
  ` Runway strip` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `airplane` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `employers`
--

CREATE TABLE `employers` (
  `id_employers` int NOT NULL,
  `number_employer` int NOT NULL,
  `name` text NOT NULL,
  `age` int NOT NULL,
  `date` date NOT NULL,
  `gender` tinyint(1) NOT NULL,
  `job of title` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `organization` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `employers`
--

INSERT INTO `employers` (`id_employers`, `number_employer`, `name`, `age`, `date`, `gender`, `job of title`, `organization`) VALUES
(2, 10201, 'Gregory', 21, '2003-03-05', 1, 'pilot', 'Azurair');

-- --------------------------------------------------------

--
-- Структура таблицы `passagers`
--

CREATE TABLE `passagers` (
  `id_passagers` int NOT NULL,
  `id_tickets` int NOT NULL,
  `name_passagers` text NOT NULL,
  `date of birth` date NOT NULL,
  `nationality` text NOT NULL,
  `passport` text NOT NULL,
  `number_phone` int NOT NULL,
  `address` text NOT NULL,
  `items` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Дамп данных таблицы `passagers`
--

INSERT INTO `passagers` (`id_passagers`, `id_tickets`, `name_passagers`, `date of birth`, `nationality`, `passport`, `number_phone`, `address`, `items`) VALUES
(3, 5, 'Vladimir', '2000-04-09', 'Russia', '2060 518912', 220115014, 'Rostov-on-Don Voroshilov raion', 'Bag');

-- --------------------------------------------------------

--
-- Структура таблицы `race`
--

CREATE TABLE `race` (
  `id_race` int NOT NULL,
  `id_tickets` int NOT NULL,
  `class/data` text NOT NULL,
  `route` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `race` text NOT NULL,
  `time_begin` int NOT NULL,
  `time_end` int NOT NULL,
  `number_race` int NOT NULL,
  `organization` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `tickets`
--

CREATE TABLE `tickets` (
  `id_tickets` int NOT NULL,
  `id_passagers` int NOT NULL,
  `number_tickets` int NOT NULL,
  `class/data` text NOT NULL,
  `time` time(6) NOT NULL,
  `location` text NOT NULL,
  `race` float NOT NULL,
  `terminal` varchar(12) NOT NULL,
  `name_passager` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `airports`
--
ALTER TABLE `airports`
  ADD PRIMARY KEY (`id_airport`),
  ADD UNIQUE KEY `id_employers` (`id_employers`),
  ADD UNIQUE KEY `id_race` (`id_race`);

--
-- Индексы таблицы `employers`
--
ALTER TABLE `employers`
  ADD PRIMARY KEY (`id_employers`);

--
-- Индексы таблицы `passagers`
--
ALTER TABLE `passagers`
  ADD PRIMARY KEY (`id_passagers`),
  ADD UNIQUE KEY `id_tickets` (`id_tickets`);

--
-- Индексы таблицы `race`
--
ALTER TABLE `race`
  ADD PRIMARY KEY (`id_race`),
  ADD UNIQUE KEY `id_tickets` (`id_tickets`);

--
-- Индексы таблицы `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`id_tickets`),
  ADD UNIQUE KEY `id_passagers` (`id_passagers`);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `airports`
--
ALTER TABLE `airports`
  ADD CONSTRAINT `airports_ibfk_1` FOREIGN KEY (`id_employers`) REFERENCES `employers` (`id_employers`);

--
-- Ограничения внешнего ключа таблицы `race`
--
ALTER TABLE `race`
  ADD CONSTRAINT `race_ibfk_1` FOREIGN KEY (`id_tickets`) REFERENCES `tickets` (`id_tickets`),
  ADD CONSTRAINT `race_ibfk_2` FOREIGN KEY (`id_race`) REFERENCES `airports` (`id_race`);

--
-- Ограничения внешнего ключа таблицы `tickets`
--
ALTER TABLE `tickets`
  ADD CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`id_passagers`) REFERENCES `passagers` (`id_passagers`);
--
-- База данных: `gruber_stepanchenko_27`
--
CREATE DATABASE IF NOT EXISTS `gruber_stepanchenko_27` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `gruber_stepanchenko_27`;

-- --------------------------------------------------------

--
-- Структура таблицы `salespeople`
--

CREATE TABLE `salespeople` (
  `id_salespeople` int NOT NULL,
  `snum` int NOT NULL,
  `sname` text NOT NULL,
  `city` text NOT NULL,
  `comm` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `salespeople`
--
ALTER TABLE `salespeople`
  ADD PRIMARY KEY (`id_salespeople`);
--
-- База данных: `is22kuz`
--
CREATE DATABASE IF NOT EXISTS `is22kuz` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `is22kuz`;

-- --------------------------------------------------------

--
-- Структура таблицы `predmet`
--

CREATE TABLE `predmet` (
  `id_pred` int NOT NULL,
  `nazv` varchar(70) NOT NULL DEFAULT 'базы данных',
  `id_prep` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `predmet`
--

INSERT INTO `predmet` (`id_pred`, `nazv`, `id_prep`) VALUES
(1, 'базы данных', 3),
(2, 'Психохогия общения ', 1),
(3, 'История', 2),
(4, 'Операционные системы', 3);

-- --------------------------------------------------------

--
-- Структура таблицы `prepod`
--

CREATE TABLE `prepod` (
  `id_prep` int NOT NULL,
  `fio` varchar(70) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `prepod`
--

INSERT INTO `prepod` (`id_prep`, `fio`) VALUES
(1, 'Марышева ОВ'),
(2, 'Иваненков ПП'),
(3, 'Кротенко ЕМ');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `predmet`
--
ALTER TABLE `predmet`
  ADD PRIMARY KEY (`id_pred`),
  ADD KEY `id_prep` (`id_prep`);

--
-- Индексы таблицы `prepod`
--
ALTER TABLE `prepod`
  ADD PRIMARY KEY (`id_prep`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `predmet`
--
ALTER TABLE `predmet`
  MODIFY `id_pred` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `prepod`
--
ALTER TABLE `prepod`
  MODIFY `id_prep` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `predmet`
--
ALTER TABLE `predmet`
  ADD CONSTRAINT `predmet_ibfk_1` FOREIGN KEY (`id_prep`) REFERENCES `prepod` (`id_prep`);
--
-- База данных: `is_22`
--
CREATE DATABASE IF NOT EXISTS `is_22` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `is_22`;

-- --------------------------------------------------------

--
-- Структура таблицы `gruppa`
--

CREATE TABLE `gruppa` (
  `id_gr` int NOT NULL,
  `nazv` varchar(20) COLLATE utf8_unicode_ci DEFAULT 'ИС 22'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `gruppa`
--

INSERT INTO `gruppa` (`id_gr`, `nazv`) VALUES
(1, 'ИС 22'),
(2, 'ИС 23'),
(3, 'ИС 21');

-- --------------------------------------------------------

--
-- Структура таблицы `student`
--

CREATE TABLE `student` (
  `id_st` int NOT NULL,
  `fio` varchar(70) COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_gr` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `student`
--

INSERT INTO `student` (`id_st`, `fio`, `id_gr`) VALUES
(1, 'Иванов', 3),
(2, 'Петров', 1),
(3, 'Сидоров', 2);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `gruppa`
--
ALTER TABLE `gruppa`
  ADD PRIMARY KEY (`id_gr`);

--
-- Индексы таблицы `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id_st`),
  ADD KEY `id_gr` (`id_gr`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `gruppa`
--
ALTER TABLE `gruppa`
  MODIFY `id_gr` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `student`
--
ALTER TABLE `student`
  MODIFY `id_st` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`id_gr`) REFERENCES `gruppa` (`id_gr`);
--
-- База данных: `kuznetsova1`
--
CREATE DATABASE IF NOT EXISTS `kuznetsova1` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `kuznetsova1`;

-- --------------------------------------------------------

--
-- Структура таблицы `customers`
--

CREATE TABLE `customers` (
  `cnum` int NOT NULL,
  `snum` int DEFAULT NULL,
  `cname` varchar(80) COLLATE utf8_unicode_ci NOT NULL,
  `pol` varchar(5) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city` varchar(50) COLLATE utf8_unicode_ci NOT NULL DEFAULT (_cp866'San Jose'),
  `rating` int NOT NULL
) ;

--
-- Дамп данных таблицы `customers`
--

INSERT INTO `customers` (`cnum`, `snum`, `cname`, `pol`, `city`, `rating`) VALUES
(2001, 1001, 'Hoffman', 'м', 'Paris', 100),
(2002, 1003, 'Giovanni', 'м', 'Rome', 200),
(2003, 1002, 'Liu', 'м', 'San Jose', 200),
(2004, 1002, 'Grass', 'м', 'Berlin', 300),
(2006, 1001, 'Clemens', 'м', 'Paris', 100),
(2007, 1004, 'Pereira', 'ж', 'Rome', 100),
(2008, 1007, 'Cisneros', 'м', 'San Jose', 300);

-- --------------------------------------------------------

--
-- Структура таблицы `orders`
--

CREATE TABLE `orders` (
  `onum` int NOT NULL,
  `amt` float(7,2) NOT NULL,
  `dostavka` int DEFAULT NULL,
  `oplata` varchar(40) COLLATE utf8_unicode_ci DEFAULT NULL,
  `odate` date NOT NULL,
  `cnum` int DEFAULT NULL,
  `snum` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `orders`
--

INSERT INTO `orders` (`onum`, `amt`, `dostavka`, `oplata`, `odate`, `cnum`, `snum`) VALUES
(3001, 18.69, 2000, 'нал', '2021-03-10', 2008, 1007),
(3002, 1900.10, 345, 'нал', '2021-03-10', 2007, 1004),
(3003, 767.19, 232, 'безнал', '2021-03-10', 2001, 1001),
(3005, 5160.45, 877, 'безнал', '2021-03-10', 2003, 1002),
(3006, 1098.16, 565, 'нал', '2021-03-10', 2008, 1007),
(3007, 75.75, 567, 'нал', '2021-04-10', 2004, 1002),
(3008, 4723.00, 567, 'нал', '2021-05-10', 2006, 1001),
(3009, 1713.23, 768, 'нал', '2021-04-10', 2002, 1003),
(3010, 1309.95, 70, 'нал', '2021-06-10', 2004, 1002);

-- --------------------------------------------------------

--
-- Структура таблицы `salespeople1`
--

CREATE TABLE `salespeople1` (
  `snum` int NOT NULL,
  `sname1` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `naprav` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `city1` varchar(80) COLLATE utf8_unicode_ci DEFAULT NULL,
  `comm` float(4,2) DEFAULT NULL
) ;

--
-- Дамп данных таблицы `salespeople1`
--

INSERT INTO `salespeople1` (`snum`, `sname1`, `naprav`, `city1`, `comm`) VALUES
(1001, 'Peel', 'молочка', 'London', 0.12),
(1002, 'Serres', 'алкоголь', 'San Jose', 0.16),
(1003, 'Axelrod', 'табак', 'New York', 0.10),
(1004, 'Motika', 'колбасы', 'London', 0.11),
(1007, 'Rifkin', 'мясо', 'Barselona', 0.16);

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `customers`
--
ALTER TABLE `customers`
  ADD PRIMARY KEY (`cnum`),
  ADD KEY `snum` (`snum`);

--
-- Индексы таблицы `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`onum`),
  ADD KEY `cnum` (`cnum`),
  ADD KEY `snum` (`snum`);

--
-- Индексы таблицы `salespeople1`
--
ALTER TABLE `salespeople1`
  ADD PRIMARY KEY (`snum`),
  ADD UNIQUE KEY `snum` (`snum`);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `customers`
--
ALTER TABLE `customers`
  ADD CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`snum`) REFERENCES `salespeople1` (`snum`);

--
-- Ограничения внешнего ключа таблицы `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`cnum`) REFERENCES `customers` (`cnum`),
  ADD CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`snum`) REFERENCES `salespeople1` (`snum`);
--
-- База данных: `kypin`
--
CREATE DATABASE IF NOT EXISTS `kypin` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `kypin`;

-- --------------------------------------------------------

--
-- Структура таблицы `enterprise`
--

CREATE TABLE `enterprise` (
  `ent_id` int NOT NULL,
  `ent_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ent_v` varchar(3) COLLATE utf8_unicode_ci NOT NULL,
  `data_reg` date NOT NULL,
  `rab_c` int NOT NULL,
  `vid_p` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `enterprise`
--

INSERT INTO `enterprise` (`ent_id`, `ent_name`, `ent_v`, `data_reg`, `rab_c`, `vid_p`) VALUES
(1, 'ОЧУМЕЛЫЕ РУЧКИ', 'ООО', '2002-06-21', 36, 'Картофель'),
(2, 'БЫСТРОВ', 'ИП', '2022-07-16', 2, 'Картофель'),
(3, 'ПОПОВЯНСКОЕ ГРАФСТВО', 'ЗАО', '2023-08-04', 1, 'Просо'),
(4, 'ГАЧИ', 'ООО', '2005-12-28', 15, 'РиС'),
(5, 'ЧИЛИКИН', 'ИП', '2024-09-15', 10, 'Чеснок');

-- --------------------------------------------------------

--
-- Структура таблицы `product`
--

CREATE TABLE `product` (
  `product_id` int NOT NULL,
  `product_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `ed_iz` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Дамп данных таблицы `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `ed_iz`, `price`) VALUES
(1, 'Картофель', 'КГ', '68.00'),
(2, 'Рис', 'КГ', '113.00'),
(3, 'Просо', 'КГ', '32.00'),
(4, 'Чеснок', 'КГ', '42.00'),
(5, 'Капуста', 'КГ', '29.00'),
(6, 'Лён', 'КГ', '217.00'),
(7, 'Ячмень', 'КГ', '71.00');

-- --------------------------------------------------------

--
-- Структура таблицы `supply`
--

CREATE TABLE `supply` (
  `supply_id` int NOT NULL,
  `date_s` date NOT NULL,
  `sprice_supply` decimal(10,2) NOT NULL,
  `ent_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `enterprise`
--
ALTER TABLE `enterprise`
  ADD PRIMARY KEY (`ent_id`);

--
-- Индексы таблицы `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`product_id`);

--
-- Индексы таблицы `supply`
--
ALTER TABLE `supply`
  ADD PRIMARY KEY (`supply_id`),
  ADD KEY `ent_id` (`ent_id`),
  ADD KEY `product_id` (`product_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `enterprise`
--
ALTER TABLE `enterprise`
  MODIFY `ent_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `product`
--
ALTER TABLE `product`
  MODIFY `product_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT для таблицы `supply`
--
ALTER TABLE `supply`
  MODIFY `supply_id` int NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `supply`
--
ALTER TABLE `supply`
  ADD CONSTRAINT `supply_ibfk_1` FOREIGN KEY (`ent_id`) REFERENCES `enterprise` (`ent_id`),
  ADD CONSTRAINT `supply_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
