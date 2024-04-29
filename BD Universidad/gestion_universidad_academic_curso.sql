-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: gestion_universidad
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `academic_curso`
--

DROP TABLE IF EXISTS `academic_curso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `academic_curso` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(30) NOT NULL,
  `creditos` smallint unsigned NOT NULL,
  `docente_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `Academic_curso_docente_id_efcab381_fk_Academic_docente_id` (`docente_id`),
  CONSTRAINT `Academic_curso_docente_id_efcab381_fk_Academic_docente_id` FOREIGN KEY (`docente_id`) REFERENCES `academic_docente` (`id`),
  CONSTRAINT `academic_curso_chk_1` CHECK ((`creditos` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `academic_curso`
--

LOCK TABLES `academic_curso` WRITE;
/*!40000 ALTER TABLE `academic_curso` DISABLE KEYS */;
INSERT INTO `academic_curso` VALUES (1,'Matematicas',6,NULL),(3,'Computacion',6,NULL),(4,'Algebra',4,NULL),(5,'Historia WWII',7,NULL),(6,'Musica',10,NULL),(7,'Contabilidad',5,NULL),(8,'Programación',6,NULL),(9,'Arquitectura',7,2);
/*!40000 ALTER TABLE `academic_curso` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-29 11:45:30
