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

insert  into `clinic`(`login_id`,`clinic_name`,`phone`,`email`,`place`,`post`,`pincode`,`license`) values (2,'aaa',1234567890,'a@gmail.com','kottayam','chala',987654,'123234455'),(3,'Sreechand speciality',8590297841,'sreechand@gmail.com','kannur','chova',670596,'8765'),(4,'',0,'','','',0,''),(5,'Cooperative Hospital',9446890056,'cooperative@gmail.co','Thalassery','Thalassery',670589,'87659'),(6,'Cooperative Hospital',9446890056,'cooperative@gmail.com','Thaliparamba','Thaliparamba',670543,'7654');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `clinic_id` int(11) DEFAULT NULL,
  `feedback` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`clinic_id`,`feedback`,`date`) values (1,2,'The pharmacy staff c','2022-03-23');

/*Table structure for table `image` */

DROP TABLE IF EXISTS `image`;

CREATE TABLE `image` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `clinic_id` int(11) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `result` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`image_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `image` */

insert  into `image`(`image_id`,`clinic_id`,`photo`,`date`,`result`) values (1,2,'/static/pic/220323-1','2022-03-23',NULL),(2,2,'/static/pic/220510-1','2022-05-10',NULL),(3,2,'/static/pic/220510-1','2022-05-10',NULL),(4,2,'/static/pic/220510-1','2022-05-10',NULL),(5,2,'/static/pic/220510-1','2022-05-10',NULL),(6,2,'/static/pic/220510-1','2022-05-10',NULL),(7,2,'/static/pic/220510-171231jpg','2022-05-10','Diseased'),(8,2,'/static/pic/220510-171607jpg','2022-05-10','Diseased'),(9,2,'/static/pic/220510-171719jpg','2022-05-10','Diseased');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'sreechand@gmail.com','sree123','clinic'),(3,'koyli@gmail.com','koyli41','clinic'),(4,'','','clinic'),(5,'cooperative@gmail.co','coop1234','clinic'),(6,'cooperative@gmail.co','co3456','clinic');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
