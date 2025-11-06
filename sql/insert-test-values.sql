USE palette;

-- --- USERS ---
INSERT INTO user (username, email)
VALUES
  ('artlover', 'artlover@example.com'),
  ('designer_dan', 'dan@example.com');

-- --- PALETTES ---
INSERT INTO palette (user_id, name, description)
VALUES
  (1, 'Sunset Dreams', 'Warm oranges, pinks, and purples for sunset-inspired art.'),
  (2, 'Ocean Breeze', 'Cool blues and greens inspired by the sea.');

-- --- COLORS ---
INSERT INTO color (hex_value, r, g, b, name, hue, saturation, brightness)
VALUES
  ('#FF6B6B', 255, 107, 107, 'Coral Red', 0, 80, 90),
  ('#FFD93D', 255, 217, 61, 'Sunshine Yellow', 50, 85, 100),
  ('#6BCB77', 107, 203, 119, 'Mint Green', 140, 50, 80),
  ('#4D96FF', 77, 150, 255, 'Ocean Blue', 210, 70, 85),
  ('#6A4C93', 106, 76, 147, 'Royal Purple', 260, 60, 60);

-- --- TAGS ---
INSERT INTO tag (name)
VALUES
  ('warm'),
  ('cool'),
  ('nature'),
  ('retro');

-- --- PALETTE_COLOR (many-to-many) ---
INSERT INTO palette_color (palette_id, color_id, order_index)
VALUES
  (1, 1, 1),  -- Sunset Dreams: Coral Red
  (1, 2, 2),  -- Sunset Dreams: Sunshine Yellow
  (1, 5, 3),  -- Sunset Dreams: Royal Purple
  (2, 3, 1),  -- Ocean Breeze: Mint Green
  (2, 4, 2);  -- Ocean Breeze: Ocean Blue

-- --- PALETTE_TAG (many-to-many) ---
INSERT INTO palette_tag (palette_id, tag_id)
VALUES
  (1, 1),  -- Sunset Dreams is warm
  (2, 2),  -- Ocean Breeze is cool
  (2, 3);  -- Ocean Breeze is nature
