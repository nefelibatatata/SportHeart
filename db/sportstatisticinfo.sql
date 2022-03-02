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

 Date: 02/03/2022 10:16:06
*/
continuing_time, steps, calory, distance,standard_time, standard_time
"727","0","0","0","0"
SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for sportstatisticinfo
-- ----------------------------
DROP TABLE IF EXISTS `sportstatisticinfo`;
CREATE TABLE `sportstatisticinfo`  (
  `student_id` varchar(18) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL comment '学籍号',
  `device_id` varchar(18) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL comment '设备标识',
  `sport_date` date NOT NULL DEFAULT '0000-00-00' comment '运动日期',
  `start_time` time NOT NULL DEFAULT '00:00:00' comment '开始时间',
  `sport_type` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL comment '运动模式',
  `continuing_time` int(11) NOT NULL comment '持续时间',
  `steps` int(11) NOT NULL comment '步数',
  `calory` double NOT NULL comment '卡路里',
  `distance` double NOT NULL comment '距离',
  `standard_time` int(11) NOT NULL comment '达标时长',
  `max_heart_rate` double NOT NULL comment '最大心率',
  `average_heart_rate` double NOT NULL comment '平均心率',
  `max_steps` double NOT NULL comment '最大步长',
  `average_steps` double NOT NULL comment '平均步长',
  `rate` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL comment '速度信息',
  PRIMARY KEY (`student_id`, `device_id`, `sport_date`, `start_time`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;
