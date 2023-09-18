CREATE TABLE users (
    user_id INTEGER NOT NULL AUTO_INCREMENT,
    username VARCHAR(20) NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    email VARCHAR(64) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id)
);

CREATE TABLE stray_cat_info (
    cat_id INTEGER NOT NULL AUTO_INCREMENT,
    title VARCHAR(20) NOT NULL,
    description VARCHAR(128) NOT NULL,
    image_url VARCHAR(128) NOT NULL,
    location_lat FLOAT NOT NULL,
    location_lng FLOAT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- 修正此处
    PRIMARY KEY (cat_id)
);

CREATE TABLE comments (
    comment_id INTEGER NOT NULL AUTO_INCREMENT,
    user_id INTEGER NOT NULL,
    cat_id INTEGER NOT NULL,
    content VARCHAR(1024) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,  -- 修正此处
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (cat_id) REFERENCES stray_cat_info(cat_id),
    PRIMARY KEY (comment_id)
);
