CREATE TABLE `user`(
    `user_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(50) NOT NULL,
    `email` VARCHAR(100) NOT NULL,
    `created_at` TIMESTAMP NOT NULL
);
CREATE TABLE `palettes`(
    `palette_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_id` BIGINT NOT NULL,
    `name` VARCHAR(50) NOT NULL,
    `description` TEXT NOT NULL,
    `date_created` TIMESTAMP NOT NULL,
    `updated_at` TIMESTAMP NULL
);
CREATE TABLE `colors`(
    `color_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `hex_value` CHAR(7) NOT NULL,
    `rgb_value` VARCHAR(11) NULL,
    `name` VARCHAR(50) NULL,
    `hue` BIGINT NULL,
    `saturation` BIGINT NULL,
    `brightness` BIGINT NULL
);
CREATE TABLE `tags`(
    `tag_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);
CREATE TABLE `palette_colors`(
    `pallete_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `color_id` BIGINT NOT NULL,
    `order_index` BIGINT NOT NULL,
    PRIMARY KEY(`color_id`)
);
CREATE TABLE `palette_tags`(
    `palette_id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
    `tag_id` BIGINT NOT NULL,
    PRIMARY KEY(`tag_id`)
);
ALTER TABLE
    `palettes` ADD CONSTRAINT `palettes_user_id_foreign` FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`);
ALTER TABLE
    `palettes` ADD CONSTRAINT `palettes_palette_id_foreign` FOREIGN KEY(`palette_id`) REFERENCES `palette_colors`(`pallete_id`);
ALTER TABLE
    `tags` ADD CONSTRAINT `tags_tag_id_foreign` FOREIGN KEY(`tag_id`) REFERENCES `palette_tags`(`tag_id`);
ALTER TABLE
    `palette_colors` ADD CONSTRAINT `palette_colors_pallete_id_foreign` FOREIGN KEY(`pallete_id`) REFERENCES `palette_tags`(`palette_id`);
ALTER TABLE
    `palette_colors` ADD CONSTRAINT `palette_colors_color_id_foreign` FOREIGN KEY(`color_id`) REFERENCES `colors`(`color_id`);
