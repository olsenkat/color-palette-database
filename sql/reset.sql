-- db-init.sql

-- Drop in reverse dependency order
DROP TABLE IF EXISTS palette_tag;
DROP TABLE IF EXISTS palette_color;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS color;
DROP TABLE IF EXISTS palette;
DROP TABLE IF EXISTS user;

-- Now recreate tables (your schema goes here)

CREATE TABLE `user`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL UNIQUE,
    `password` VARCHAR(100) NOT NULL UNIQUE,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `palette`(
    `palette_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT UNSIGNED NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    `description` TEXT NOT NULL,
    `date_created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES `user`(`user_id`) ON DELETE CASCADE
);
CREATE TABLE `color`(
    `color_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `hex_value` CHAR(7) NOT NULL,
    `r` TINYINT UNSIGNED NOT NULL,
    `g` TINYINT UNSIGNED NOT NULL,
    `b` TINYINT UNSIGNED NOT NULL,
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
    `color_id` BIGINT UNSIGNED NOT NULL,
    `order_index` SMALLINT NOT NULL,
    PRIMARY KEY (`palette_id`,`color_id`),
    FOREIGN KEY (`palette_id`) REFERENCES `palette`(`palette_id`) ON DELETE CASCADE,
    FOREIGN KEY (`color_id`) REFERENCES `color`(`color_id`) ON DELETE CASCADE
);
CREATE TABLE `palette_tag`(
    `palette_id` BIGINT UNSIGNED NOT NULL,
    `tag_id` BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY (palette_id, tag_id),
    FOREIGN KEY (`palette_id`) REFERENCES `palette`(`palette_id`) ON DELETE CASCADE,
    FOREIGN KEY (`tag_id`) REFERENCES `tag`(`tag_id`) ON DELETE CASCADE
);


CREATE INDEX idx_user_username ON user(username);
CREATE INDEX idx_palette_user_id ON palette(user_id);
CREATE INDEX idx_palette_name ON palette(name);
CREATE INDEX idx_color_hex ON color(hex_value);
CREATE INDEX idx_tag_name ON tag(name);
