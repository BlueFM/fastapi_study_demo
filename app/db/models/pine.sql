CREATE TABLE IF NOT EXISTS `pine_family`
(
    `pk_id`      INT UNSIGNED AUTO_INCREMENT COMMENT '主键自增id',
    `name`       varchar(20) NOT NULL COMMENT '名称',
    `sex`        varchar(20) NOT NULL COMMENT '性别',
    `age`        SMALLINT    NOT NULL COMMENT '年龄',
    `profession` varchar(50) NOT NULL COMMENT '职业',
    `hobby`      varchar(100) NOT NULL COMMENT '爱好',
    `motto`      varchar(100) NOT NULL COMMENT '座右铭',
    `add_time`   int(10)     NOT NULL DEFAULT 0 COMMENT '数据修改时间戳',
    `is_delete`  SMALLINT    NOT NULL DEFAULT 0 COMMENT '数据是否删除：（0：否， 1：是）',
    PRIMARY KEY (`pk_id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4 COMMENT ='家庭成员表';
