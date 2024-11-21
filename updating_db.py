import sqlite3


conn = sqlite3.connect('summary_bot.db')
cursor = conn.cursor()

cursor.execute('''
UPDATE "client"
SET name = "Anastasia"
WHERE name = "Anastasiia";
''')

cursor.execute('''
UPDATE "group"
SET group_name = "Slay Queens"
WHERE group_name = "Slay girls";
''')

cursor.execute('''
UPDATE "prompt_stats"
SET prompt_frequency = 0.6
WHERE prompt_id = 1;
''')

cursor.execute('''
UPDATE "prompt_stats"
SET prompt_frequency = CAST(prompt_frequency AS INTEGER);
''')

cursor.execute('''
UPDATE "Group_Member"
SET "is_admin" = 0
WHERE group_id = 1 AND client_id = 1
''')

cursor.execute('''
UPDATE "Group_Member"
SET "is_admin" = 1
WHERE group_id = 1 AND client_id = 3
''')


conn.commit()
cursor.close()
