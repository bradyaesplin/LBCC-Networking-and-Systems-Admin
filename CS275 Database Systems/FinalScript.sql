-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema employeerecords
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema employeerecords
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `employeerecords` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `employeerecords` ;

-- -----------------------------------------------------
-- Table `employeerecords`.`employee_info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employeerecords`.`employee_info` (
  `id_number` INT NOT NULL,
  `street_address` VARCHAR(40) NOT NULL,
  `city` VARCHAR(30) NOT NULL,
  `state` VARCHAR(30) NOT NULL,
  `mail_code` INT NOT NULL,
  `next_kin` VARCHAR(100) NOT NULL,
  `nk_phone` VARCHAR(12) NOT NULL,
  PRIMARY KEY (`id_number`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `employeerecords`.`employee_id`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `employeerecords`.`employee_id` (
  `id_number` INT NOT NULL,
  `lname` VARCHAR(20) NOT NULL,
  `fname` VARCHAR(30) NOT NULL,
  `mname` VARCHAR(30) NOT NULL,
  `prefix` VARCHAR(5) NOT NULL,
  `login_id` INT NOT NULL,
  `employee_info_id_number` INT NOT NULL,
  PRIMARY KEY (`id_number`, `employee_info_id_number`),
  INDEX `fk_employee_id_employee_info_idx` (`employee_info_id_number` ASC) VISIBLE,
  CONSTRAINT `fk_employee_id_employee_info`
    FOREIGN KEY (`employee_info_id_number`)
    REFERENCES `employeerecords`.`employee_info` (`id_number`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
