-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql12.freesqldatabase.com
-- Generation Time: Sep 04, 2024 at 06:01 PM
-- Server version: 5.5.62-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql12727620`
--

-- --------------------------------------------------------

--
-- Table structure for table `files`
--

CREATE TABLE `files` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `file_name` varchar(255) DEFAULT NULL,
  `ipfs_link` varchar(255) DEFAULT NULL,
  `encryption_key` blob
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `files`
--

INSERT INTO `files` (`id`, `user_id`, `file_name`, `ipfs_link`, `encryption_key`) VALUES
(5, 1, 'j0vt6ueb78docx.docx', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmVH2WBrdVPqQ9GzrEyZSixJj8Uy6ppEu4y5UCeek2ypJe\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(12, 3, 'Dp.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmVLvDyrA1sVbBocKPbtcKJyUvCGUMeBhY43bwp5dbW1vj\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(13, 3, 'Finalyear_16_Bitlocks-1.pdf', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmdTXU9QrKB1PwKzGSjaKzQu2L66CsTtcoyHSf7ALHLJwa\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(14, 5, 'newplot.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmYVp56ZramgnMjP4eT6RUNH8MgTznV6sM7gHBaznHeywF\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(15, 5, 'newplot.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmYVp56ZramgnMjP4eT6RUNH8MgTznV6sM7gHBaznHeywF\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(16, 5, 'newplot.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmYVp56ZramgnMjP4eT6RUNH8MgTznV6sM7gHBaznHeywF\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(60, 1, 'example3. (3).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmT3V3VaNEwBbrGKJtgwWCAEFKqtU62P4iX5SZ3XwegKzR\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(62, 1, 'example3. (1).png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/Qmb6BWvVXMM3dyaNWAqQi184ZRayTuT4UHjEFg3PdHe1C8\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(63, 1, 'example3. (1).png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/Qmb6BWvVXMM3dyaNWAqQi184ZRayTuT4UHjEFg3PdHe1C8\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(64, 1, 'example3. (4).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmT3V3VaNEwBbrGKJtgwWCAEFKqtU62P4iX5SZ3XwegKzR\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(65, 1, 'example3. (4).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmT3V3VaNEwBbrGKJtgwWCAEFKqtU62P4iX5SZ3XwegKzR\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(66, 1, 'example3. (8).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmT3V3VaNEwBbrGKJtgwWCAEFKqtU62P4iX5SZ3XwegKzR\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(67, 1, 'example3. (8).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmT3V3VaNEwBbrGKJtgwWCAEFKqtU62P4iX5SZ3XwegKzR\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(68, 1, 'example3. (8).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmT3V3VaNEwBbrGKJtgwWCAEFKqtU62P4iX5SZ3XwegKzR\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(69, 1, 'output000.txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(70, 1, 'output000.txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(71, 1, 'example3. (9).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(72, 1, 'example3. (9).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(73, 1, 'example3. (10).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(74, 1, 'example3. (10).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(75, 1, 'example3. (10).txt', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmSbi9989A7xWw1UCi8sxvJAu7vYy33m2SBffV9qDgRzE4\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(76, 1, 'images.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmUY5WtUQrQuPTjsNkHwNtQL6S1cy9ftnmG2EtRsbwCKEX\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(77, 1, 'images.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmUY5WtUQrQuPTjsNkHwNtQL6S1cy9ftnmG2EtRsbwCKEX\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56),
(78, 1, 'images.png', '{\"ipfs_storage\":{\"ipfs_url\":\"https://gateway.pinata.cloud/ipfs/QmUY5WtUQrQuPTjsNkHwNtQL6S1cy9ftnmG2EtRsbwCKEX\"}}', 0xbf1bb34f8f42886504eafbcd7b2ea9dc3cefebb90810d318920fb680e1203c56);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'test', 'test'),
(2, 'hello', 'hello'),
(3, 'piyush ', 'piyush'),
(4, 'phinehas.mane22@vit.edu', '7350348346'),
(5, 'vaishnavi', 'vaishnavi'),
(6, 'shreyash4004', 'Shreyash123'),
(7, 'Yogesh', '123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `files`
--
ALTER TABLE `files`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `files`
--
ALTER TABLE `files`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `files`
--
ALTER TABLE `files`
  ADD CONSTRAINT `files_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
