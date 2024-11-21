import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('summary_bot.db')
cursor = conn.cursor()

# Insert data into the "group" table
cursor.execute('''
INSERT INTO "group" ("group_name")
VALUES 
    ("Slay girls"),
    ("Lovers of Pain and Labs"),
    ("Faculty of philology"),
    ("Intro to translation");
''')

# Insert data into the "client" table
cursor.execute('''
INSERT INTO "client" ("name", "telegram_tag")
VALUES 
    ("Polina", "@pastuska"),
    ("Yliana", "@anna_kartina"),
    ("Kris", "@inlove_with_cl"),
    ("Anastasiia", "@the_life_wasn't_a_mistake"),
    ("Volodymyr", "@true_linguist"),
    ("Svitlana", "@best_translater_and_teacher"),
    ("Yura", "@the_best_sheikh_of_first_group");
''')

# Insert data into the "Group_Member" table
cursor.execute('''
INSERT INTO "Group_Member" ("client_id", "group_id", "is_admin")
VALUES 
    (7, 2, 1),
    (7, 3, 0),
    (7, 4, 0),
    (6, 4, 1),
    (5, 3, 0),
    (5, 4, 0),
    (4, 3, 0),
    (4, 4, 0),
    (3, 1, 0),
    (3, 2, 0),
    (3, 3, 0),
    (3, 4, 0),  
    (2, 1, 0),
    (2, 2, 0),
    (2, 4, 0),  
    (1, 1, 1),
    (1, 2, 0),
    (1, 3, 0),  
    (1, 4, 0);
''')

# Insert data into the "prompt" table
cursor.execute('''
INSERT INTO "prompt" ("content")
VALUES 
    ("What are the main news?"),
    ("Were there any info about h/w?"),
    ("What did happen? Why are people angry?");
''')

# Insert data into the "prompt_stats" table
cursor.execute('''
INSERT INTO "prompt_stats" ("prompt_id", "prompt_frequency")
VALUES 
    (1, 0.4),
    (2, 0.4),
    (3, 0.2);
''')

# Commit the transaction and close the cursor
conn.commit()
cursor.close()

print("Data inserted successfully!")
