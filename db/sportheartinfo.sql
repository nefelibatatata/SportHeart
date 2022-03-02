/*
 Navicat Premium Data Transfer

 Source Server         : JU
 Source Server Type    : MySQL
 Source Server Version : 50556
 Source Host           : 47.97.185.12:3306
 Source Schema         : fmp

 Target Server Type    : MySQL
 Target Server Version : 50556
 File Encoding         : 65001

 Date: 02/03/2022 10:15:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sportheartinfo
-- ----------------------------
DROP TABLE IF EXISTS `sportheartinfo`;
CREATE TABLE `sportheartinfo`  (
  `student_id` varchar(18) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL comment '学籍号',
  `device_id` varchar(18) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL comment '设备标识',
  `sport_date` date NOT NULL DEFAULT '0000-00-00' comment '运动日期',
  `start_time` time NOT NULL DEFAULT '00:00:00' comment '开始时间',
  `sport_type` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL comment '运动模式',
  `location` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL comment '位置',
  `heart_rate` longtext CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL comment '心率',
  PRIMARY KEY (`student_id`, `device_id`, `sport_date`, `start_time`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
