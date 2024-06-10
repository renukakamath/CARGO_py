/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - c_bin
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`c_bin` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `c_bin`;

/*Table structure for table `bookings` */

DROP TABLE IF EXISTS `bookings`;

CREATE TABLE `bookings` (
  `booking_id` int(50) NOT NULL AUTO_INCREMENT,
  `customer_id` int(50) DEFAULT NULL,
  `booking_date` varchar(50) DEFAULT NULL,
  `branch_id` int(50) DEFAULT NULL,
  `weight` varchar(50) DEFAULT NULL,
  `length` varchar(50) DEFAULT NULL,
  `width` varchar(50) NOT NULL,
  `from_location` varchar(50) DEFAULT NULL,
  `to_location` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `booking_status` varchar(50) DEFAULT NULL,
  `boy_id` int(50) DEFAULT NULL,
  `price_id` int(50) DEFAULT NULL,
  PRIMARY KEY (`booking_id`,`width`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `bookings` */

insert  into `bookings`(`booking_id`,`customer_id`,`booking_date`,`branch_id`,`weight`,`length`,`width`,`from_location`,`to_location`,`amount`,`booking_status`,`boy_id`,`price_id`) values (1,1,'2022-03-15 23:32:59',1,'34','safx','35','safx','xzvx','500','delivered',1,1),(2,1,'2022-03-15 23:34:22',1,'325','xcv','235','xcv','fsg','500','delivered',2,1),(3,2,'2022-03-26',1,'44','aaa','44','aaa','bbb','500','delivered',2,1),(4,2,'2022-03-26',1,'aaak','aaak','33','aaak','hhbb','500','confirm',0,1);

/*Table structure for table `branches` */

DROP TABLE IF EXISTS `branches`;

CREATE TABLE `branches` (
  `branch_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `branch_name` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`branch_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `branches` */

insert  into `branches`(`branch_id`,`login_id`,`branch_name`,`latitude`,`longitude`,`phone`,`email`) values (1,2,'puthuvyypu','9.986348845905287','76.27498626708984','9123456788','j@gmail.com'),(2,6,'branch','9.973930550350582','76.28939623915603','9087654321','bra@gmail');

/*Table structure for table `cargo_status` */

DROP TABLE IF EXISTS `cargo_status`;

CREATE TABLE `cargo_status` (
  `status_id` int(50) NOT NULL AUTO_INCREMENT,
  `booking_id` int(50) DEFAULT NULL,
  `place_name` varchar(50) DEFAULT NULL,
  `status_date_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`status_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `cargo_status` */

insert  into `cargo_status`(`status_id`,`booking_id`,`place_name`,`status_date_time`) values (1,1,'d','2022-03-15 23:39:41');

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `customer_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `customers` */

insert  into `customers`(`customer_id`,`login_id`,`first_name`,`last_name`,`phone`,`email`,`latitude`,`longitude`) values (1,5,'jifi','jifi','9123456789','j@gmail.com','9.987616235934032','76.29618544451905'),(2,9,'Tiss','Thomas','8907654321','aa@gmail.com','9.976298333333334','76.28771166666667');

/*Table structure for table `deliveryboys` */

DROP TABLE IF EXISTS `deliveryboys`;

CREATE TABLE `deliveryboys` (
  `boy_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `branch_id` int(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `latitude` varchar(100) DEFAULT NULL,
  `longitude` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`boy_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `deliveryboys` */

insert  into `deliveryboys`(`boy_id`,`login_id`,`first_name`,`last_name`,`branch_id`,`phone`,`email`,`latitude`,`longitude`) values (1,4,'dboy','dboy',1,'9123456789','j@gmail.com',NULL,NULL),(2,8,'AAA','BBB',1,'9087654321','aa@gmail.com','9.4529212','76.4304578');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(50) NOT NULL AUTO_INCREMENT,
  `customer_id` int(50) DEFAULT NULL,
  `branch_id` int(50) DEFAULT NULL,
  `feedback_description` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `feedback_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`customer_id`,`branch_id`,`feedback_description`,`reply`,`feedback_date`) values (1,2,2,'gggg','okk','2022-03-25'),(2,2,2,'hhhh','okkk','2022-03-25');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values (1,'admin','admin','admin'),(2,'puthuvyypu','puthuvyypu','branch'),(3,'arunarun','arunarun','staff'),(4,'dboydboy','dboydboy','dboy'),(5,'cus','cus','user'),(6,'branch','branch123','branch'),(7,'anna@123','anna@1234','staff'),(8,'dboy@1234','dboy@1234','dboy'),(9,'tiss','tiss','user');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(50) NOT NULL AUTO_INCREMENT,
  `booking_id` int(50) DEFAULT NULL,
  `amount_paid` varchar(50) DEFAULT NULL,
  `payment_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

insert  into `payment`(`payment_id`,`booking_id`,`amount_paid`,`payment_date`) values (1,1,'500','2022-03-15 23:36:54'),(2,3,'500','2022-03-27');

/*Table structure for table `prices` */

DROP TABLE IF EXISTS `prices`;

CREATE TABLE `prices` (
  `price_id` int(50) NOT NULL AUTO_INCREMENT,
  `maximum_weight` varchar(50) DEFAULT NULL,
  `maximum_height` varchar(50) DEFAULT NULL,
  `maximum_width` varchar(50) DEFAULT NULL,
  `maximum_distance` varchar(50) DEFAULT NULL,
  `minimum_price` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`price_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `prices` */

insert  into `prices`(`price_id`,`maximum_weight`,`maximum_height`,`maximum_width`,`maximum_distance`,`minimum_price`) values (1,'44','44','44','44','500');

/*Table structure for table `review_rating` */

DROP TABLE IF EXISTS `review_rating`;

CREATE TABLE `review_rating` (
  `review_id` int(50) NOT NULL AUTO_INCREMENT,
  `customer_id` int(50) DEFAULT NULL,
  `branch_id` int(11) DEFAULT NULL,
  `review_comment` varchar(50) DEFAULT NULL,
  `rating_point` varchar(50) DEFAULT NULL,
  `review_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`review_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `review_rating` */

insert  into `review_rating`(`review_id`,`customer_id`,`branch_id`,`review_comment`,`rating_point`,`review_date`) values (1,2,2,'ggg','4.0','2022-03-25'),(2,2,1,'ggg','4.5','2022-03-25');

/*Table structure for table `staffs` */

DROP TABLE IF EXISTS `staffs`;

CREATE TABLE `staffs` (
  `staff_id` int(50) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `branch` int(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staffs` */

insert  into `staffs`(`staff_id`,`login_id`,`first_name`,`last_name`,`branch`,`phone`,`email`) values (1,3,'arun','ps',1,'9123456789','s@gamil.com'),(2,7,'don','don',1,'9087654321','ann@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
