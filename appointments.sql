-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema appointments
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema appointments
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `appointments` DEFAULT CHARACTER SET utf8 ;
USE `appointments` ;

-- -----------------------------------------------------
-- Table `appointments`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointments`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(100) NULL,
  `password` VARCHAR(250) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `appointments`.`appointments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointments`.`appointments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `grupo` VARCHAR(250) NULL,
  `task` VARCHAR(250) NULL,
  `date` DATE NULL,
  `status` VARCHAR(250) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_appointments_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_appointments_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `appointments`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `appointments`.`statistics`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appointments`.`statistics` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `height` REAL NULL,
  `weight` REAL NULL,
  `month` DATE NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_statistics_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_statistics_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `appointments`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
