CREATE TABLE IF NOT EXISTS `cat`(
    `pk_id` INT UNSIGNED AUTO_INCREMENT COMMENT '主键自增id',
    `name` varchar(20) NOT NULL COMMENT '猫名' default 'niko',
    `breed` varchar(20) NOT NULL COMMENT '品种'   default 'unknown',
    `skin_color` varchar(20) NOT NULL COMMENT '皮肤颜色 ' default 'unknown',
    `owner` varchar(20) NOT NULL COMMENT '主人' default 'unknown',
    `age` SMALLINT NOT NULL COMMENT '年龄',
    `add_time` int(10) NOT NULL DEFAULT 0 COMMENT '数据修改时间戳',
    `is_delete` SMALLINT NOT NULL DEFAULT 0 COMMENT '数据是否删除：（0：否， 1：是）',
   PRIMARY KEY ( `pk_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='niko表';