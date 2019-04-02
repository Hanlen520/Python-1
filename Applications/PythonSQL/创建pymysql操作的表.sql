-- ****************MySql*****************
-- -*- coding: utf-8 -*-
-- --------------------------------------
-- ProjectName: MySpace
-- Author: crisimple
-- CreateTime: 2019/3/1 21:56
-- FileName: 创建pymysql操作的表.sql
-- Description:
-- Question:
-- ---------------------------------------

USE STUDY_DATABASE;
CREATE TABLE pymysql_data(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  name VARCHAR(20) NOT NULL ,
  age INT NOT NULL ,
  detail TEXT NULL
);

USE STUDY_DATABASE;
CREATE TABLE pymysql_singleData(
     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
     name VARCHAR(20) NOT NULL
);


SELECT * FROM STUDY_DATABASE.pymysql_data;
SELECT * FROM STUDY_DATABASE.pymysql_singleData;