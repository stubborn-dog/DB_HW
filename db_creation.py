import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('summary_bot.db')
cursor = conn.cursor()

# Create the `group` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `group` (
    `group_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `group_name` TEXT NOT NULL
);
''')

# Create the `Group_Member` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `Group_Member` (
    `client_id` INTEGER NOT NULL,
    `group_id` INTEGER NOT NULL,
    `is_admin` BOOLEAN NOT NULL,
    PRIMARY KEY(`client_id`, `group_id`),
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`),
    FOREIGN KEY(`group_id`) REFERENCES `group`(`group_id`)
);
''')

# Create the `client` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `client` (
    `client_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `telegram_tag` TEXT NOT NULL
);
''')

# Create the `client_prompts` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `client_prompts` (
    `prompt_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `client_id` INTEGER NOT NULL,
    FOREIGN KEY(`client_id`) REFERENCES `client`(`client_id`)
);
''')

# Create the `prompt` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `prompt` (
    `prompt_id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `content` TEXT NOT NULL
);
''')

# Create the `prompt_stats` table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `prompt_stats` (
    `prompt_id` INTEGER NOT NULL,
    `prompt_frequency` REAL NOT NULL,
    PRIMARY KEY(`prompt_id`),
    FOREIGN KEY(`prompt_id`) REFERENCES `prompt`(`prompt_id`)
);
''')

# Commit and close the connection
conn.commit()
conn.close()
