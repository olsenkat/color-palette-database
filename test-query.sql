-- Show all palettes
SELECT * FROM palette;

-- Show palettes with their user
SELECT p.name AS palette_name, u.username
FROM palette p
JOIN user u ON p.user_id = u.user_id;

-- Show colors in a specific palette
SELECT p.name AS palette, c.name AS color_name, c.hex_value
FROM palette_color pc
JOIN palette p ON pc.palette_id = p.palette_id
JOIN color c ON pc.color_id = c.color_id
ORDER BY p.name, pc.order_index;

-- Show tags for each palette
SELECT p.name AS palette, t.name AS tag
FROM palette_tag pt
JOIN palette p ON pt.palette_id = p.palette_id
JOIN tag t ON pt.tag_id = t.tag_id;
