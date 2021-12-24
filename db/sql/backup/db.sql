-- MySQL dump 10.13  Distrib 8.0.27, for Linux (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Community`
--

DROP TABLE IF EXISTS `Community`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Community` (
  `community_id` int DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `Useruser_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Community`
--

LOCK TABLES `Community` WRITE;
/*!40000 ALTER TABLE `Community` DISABLE KEYS */;
INSERT INTO `Community` VALUES (1,'Hollow Knight community','Hollow Knight',1),(2,'Fan HK community','Fan HK',2);
/*!40000 ALTER TABLE `Community` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Company`
--

DROP TABLE IF EXISTS `Company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Company` (
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `rating` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Company`
--

LOCK TABLES `Company` WRITE;
/*!40000 ALTER TABLE `Company` DISABLE KEYS */;
INSERT INTO `Company` VALUES (1,'Empresa_1','I am a company',4),(2,'Empresa_2','I am a company',4),(3,'Empresa_3','I am a company',3);
/*!40000 ALTER TABLE `Company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Game`
--

DROP TABLE IF EXISTS `Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Game` (
  `game_id` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `refounded` bit(1) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `Librarylibrary_id` int DEFAULT NULL,
  `Original_Gameoriginal_game_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Game`
--

LOCK TABLES `Game` WRITE;
/*!40000 ALTER TABLE `Game` DISABLE KEYS */;
INSERT INTO `Game` VALUES (1,40,_binary '\0','2011-11-11',1,1),(2,60,_binary '\0','2011-11-11',1,2),(3,60,_binary '\0','2011-11-11',2,2),(4,20,_binary '\0','2011-11-11',2,3);
/*!40000 ALTER TABLE `Game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Genre`
--

DROP TABLE IF EXISTS `Genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Genre` (
  `genre_id` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Genre`
--

LOCK TABLES `Genre` WRITE;
/*!40000 ALTER TABLE `Genre` DISABLE KEYS */;
INSERT INTO `Genre` VALUES (1,'Action','action '),(2,'Thriller','thriller'),(3,'Terror','terror'),(4,'RPG','rpg'),(5,'Family','family'),(6,'Moba','Moba');
/*!40000 ALTER TABLE `Genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Library`
--

DROP TABLE IF EXISTS `Library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Library` (
  `library_id` int DEFAULT NULL,
  `number_of_games` int DEFAULT NULL,
  `Useruser_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Library`
--

LOCK TABLES `Library` WRITE;
/*!40000 ALTER TABLE `Library` DISABLE KEYS */;
INSERT INTO `Library` VALUES (1,2,1),(2,2,2);
/*!40000 ALTER TABLE `Library` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Original_Game`
--

DROP TABLE IF EXISTS `Original_Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Original_Game` (
  `original_game_id` int DEFAULT NULL,
  `rating` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `Companycompany_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Original_Game`
--

LOCK TABLES `Original_Game` WRITE;
/*!40000 ALTER TABLE `Original_Game` DISABLE KEYS */;
INSERT INTO `Original_Game` VALUES (1,4,40,'Carlos Duty',1),(2,3,60,'Hollow Knight',2),(3,5,20,'Ghost of tsushima',3);
/*!40000 ALTER TABLE `Original_Game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Original_Game_Have_Genre`
--

DROP TABLE IF EXISTS `Original_Game_Have_Genre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Original_Game_Have_Genre` (
  `Original_Gameoriginal_game_id` int DEFAULT NULL,
  `Genregenre_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Original_Game_Have_Genre`
--

LOCK TABLES `Original_Game_Have_Genre` WRITE;
/*!40000 ALTER TABLE `Original_Game_Have_Genre` DISABLE KEYS */;
INSERT INTO `Original_Game_Have_Genre` VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6);
/*!40000 ALTER TABLE `Original_Game_Have_Genre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Review`
--

DROP TABLE IF EXISTS `Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Review` (
  `review_id` int DEFAULT NULL,
  `text` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `dislikes` int DEFAULT NULL,
  `likes` int DEFAULT NULL,
  `Useruser_id` int DEFAULT NULL,
  `Original_Gameoriginal_game_id` int DEFAULT NULL,
  `Companycompany_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Review`
--

LOCK TABLES `Review` WRITE;
/*!40000 ALTER TABLE `Review` DISABLE KEYS */;
INSERT INTO `Review` VALUES (1,'-','2015-11-11',5,10,1,NULL,2),(2,'-','2016-11-11',10,20,1,2,NULL),(3,'-','2017-11-11',60,30,2,1,NULL),(4,'-','2018-11-11',1,40,2,NULL,3);
/*!40000 ALTER TABLE `Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User` (
  `user_id` int DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `carddata` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (1,'luiscaumel@gmail.com','password','0000-0000-0000-0000'),(2,'l.caumel@gmail.com','password','0000-0000-0000-0000');
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Buy_Original_Game`
--

DROP TABLE IF EXISTS `User_Buy_Original_Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Buy_Original_Game` (
  `Useruser_id` int DEFAULT NULL,
  `Original_Gameoriginal_game_id` int DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Buy_Original_Game`
--

LOCK TABLES `User_Buy_Original_Game` WRITE;
/*!40000 ALTER TABLE `User_Buy_Original_Game` DISABLE KEYS */;
INSERT INTO `User_Buy_Original_Game` VALUES (1,1,'2011-11-11'),(1,2,'2011-11-11'),(2,2,'2011-11-11'),(2,3,'2011-11-11');
/*!40000 ALTER TABLE `User_Buy_Original_Game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Follow_User`
--

DROP TABLE IF EXISTS `User_Follow_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Follow_User` (
  `Useruser_id1` int DEFAULT NULL,
  `Useruser_id2` int DEFAULT NULL,
  `follows_since` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Follow_User`
--

LOCK TABLES `User_Follow_User` WRITE;
/*!40000 ALTER TABLE `User_Follow_User` DISABLE KEYS */;
INSERT INTO `User_Follow_User` VALUES (1,2,'2011-11-11'),(2,1,'2011-11-11');
/*!40000 ALTER TABLE `User_Follow_User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Rate_Original_Game`
--

DROP TABLE IF EXISTS `User_Rate_Original_Game`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Rate_Original_Game` (
  `Useruser_id` int DEFAULT NULL,
  `Original_Gameoriginal_game_id` int DEFAULT NULL,
  `rate` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Rate_Original_Game`
--

LOCK TABLES `User_Rate_Original_Game` WRITE;
/*!40000 ALTER TABLE `User_Rate_Original_Game` DISABLE KEYS */;
INSERT INTO `User_Rate_Original_Game` VALUES (1,2,5),(2,2,4),(1,1,4),(2,3,4);
/*!40000 ALTER TABLE `User_Rate_Original_Game` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Rate_Review`
--

DROP TABLE IF EXISTS `User_Rate_Review`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Rate_Review` (
  `Useruser_id` int DEFAULT NULL,
  `Reviewreview_id` int DEFAULT NULL,
  `rate` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Rate_Review`
--

LOCK TABLES `User_Rate_Review` WRITE;
/*!40000 ALTER TABLE `User_Rate_Review` DISABLE KEYS */;
INSERT INTO `User_Rate_Review` VALUES (1,3,5),(1,4,4),(2,1,3),(2,2,4);
/*!40000 ALTER TABLE `User_Rate_Review` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User_Subscribe_Community`
--

DROP TABLE IF EXISTS `User_Subscribe_Community`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `User_Subscribe_Community` (
  `Useruser_id` int DEFAULT NULL,
  `Communitycommunity_id` int DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User_Subscribe_Community`
--

LOCK TABLES `User_Subscribe_Community` WRITE;
/*!40000 ALTER TABLE `User_Subscribe_Community` DISABLE KEYS */;
INSERT INTO `User_Subscribe_Community` VALUES (1,1,'2011-11-11'),(2,2,'2011-11-11');
/*!40000 ALTER TABLE `User_Subscribe_Community` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-12-24 17:33:04
