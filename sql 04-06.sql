/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.5.20-log : Database - leukemia
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`leukemia` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `leukemia`;

/*Table structure for table `clinic` */

DROP TABLE IF EXISTS `clinic`;

CREATE TABLE `clinic` (
  `login_id` int(20) DEFAULT NULL,
  `clinic_name` varchar(100) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pincode` int(20) DEFAULT NULL,
  `license` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `clinic` */

insert  into `clinic`(`login_id`,`clinic_name`,`phone`,`email`,`place`,`post`,`pincode`,`license`) values (2,'Sreechand Speciality',8590017050,'info@sreechandhospital.com','Kannur','Kannur',670001,'22-CT-11-0000');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `clinic_id` int(11) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `image` */

DROP TABLE IF EXISTS `image`;

CREATE TABLE `image` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `clinic_id` int(11) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `image` */

insert  into `image`(`image_id`,`clinic_id`,`photo`,`date`,`result`) values (1,2,'/static/pic/220708-161847.jpg','2022-07-08','Diseased'),(2,2,'/static/pic/220708-162721.jpg','2022-07-08','Non Diseased'),(3,2,'/static/pic/220708-163056.jpg','2022-07-08','Diseased'),(4,2,'/static/pic/220708-163113.jpg','2022-07-08','Diseased'),(5,2,'/static/pic/220708-163138.jpg','2022-07-08','Diseased'),(6,2,'/static/pic/220708-163149.jpg','2022-07-08','Diseased'),(7,2,'/static/pic/220708-163203.jpg','2022-07-08','Diseased'),(8,2,'/static/pic/220708-163217.jpg','2022-07-08','Diseased'),(9,2,'/static/pic/220708-163231.jpg','2022-07-08','Diseased'),(10,2,'/static/pic/220708-163249.jpg','2022-07-08','Diseased'),(11,2,'/static/pic/220708-163355.jpg','2022-07-08','Invalid Input'),(12,2,'/static/pic/220708-163409.jpg','2022-07-08','Invalid Input'),(13,2,'/static/pic/220708-163445.jpg','2022-07-08','Diseased'),(14,2,'/static/pic/220708-164305.jpg','2022-07-08','Invalid Input');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'info@sreechandhospital.com','sree@123','clinic');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
