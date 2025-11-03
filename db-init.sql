CREATE TABLE `user`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `email` VARCHAR(100) NOT NULL UNIQUE,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE `palette`(
    `palette_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    `description` TEXT NOT NULL,
    `date_created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`)
);
CREATE TABLE `color`(
    `color_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `hex_value` CHAR(7) NOT NULL,
    `r` TINYINT NOT NULL,
    `g` TINYINT NOT NULL,
    `b` TINYINT NOT NULL,
    `name` VARCHAR(50) NULL,
    `hue` SMALLINT NULL,
    `saturation` SMALLINT NULL,
    `brightness` SMALLINT NULL
);
CREATE TABLE `tag`(
    `tag_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL UNIQUE
);
CREATE TABLE `palette_color`(
    `palette_id` BIGINT UNSIGNED NOT NULL,
    `color_id` BIGINT NOT NULL,
    `order_index` SMALLINT NOT NULL,
    PRIMARY KEY (`palette_id`,`color_id`),
    FOREIGN KEY (`palette_id`) REFERENCES `palette`(`palette_id`),
    FOREIGN KEY (`color_id`) REFERENCES `color`(`color_id`)
);
CREATE TABLE `palette_tag`(
    `palette_id` BIGINT UNSIGNED NOT NULL,
    `tag_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (palette_id, tag_id),
    FOREIGN KEY (`palette_id`) REFERENCES `palette`(`palette_id`),
    FOREIGN KEY (`tag_id`) REFERENCES `tag`(`tag_id`)
);
