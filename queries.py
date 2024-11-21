import sqlite3

conn = sqlite3.connect('summary_bot.db')
cursor = conn.cursor()

rows = cursor.fetchall()
for row in rows:
    print(row)

print('-'*20)


cursor.execute('''
SELECT c.name
FROM "Group_Member" gm
JOIN "client" c ON gm.client_id = c.client_id
WHERE gm.is_admin = 1
''')


# Fetch and print all results
rows = cursor.fetchall()
print('Admins of groups:')
for row in rows:
    print(row[0])

print('-'*20)


cursor.execute('''
SELECT g.group_name, COUNT(gm.client_id) AS member_count
FROM "Group_Member" gm
JOIN "group" g ON gm.group_id = g.group_id
GROUP BY g.group_id
ORDER BY member_count DESC
LIMIT 1
''')

row = cursor.fetchone()
if row:
    print(f"The group with the largest number of members is: {row[0]} with {row[1]} members.")
else:
    print("No groups found.")

# Close the connection
cursor.close()
conn.close()
