import sqlite3

# Create (or open) the database
conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

# Remove the old table if it exists
cur.execute('DROP TABLE IF EXISTS Counts')

# Create a new table
cur.execute('''
CREATE TABLE Counts (
    org TEXT,
    count INTEGER
)
''')

# Ask the user for the file name
fname = input('Enter file name: ')

# Use the default file if the user presses Enter
if len(fname) < 1:
    fname = 'mbox.txt'

# Open the file
fh = open(fname)

# Read the file line by line
for line in fh:

    # Skip lines that do not start with "From: "
    if not line.startswith('From: '):
        continue

    # Split the line into words
    pieces = line.split()

    # Get the email address
    email = pieces[1]

    # Extract the organization (domain)
    org = email.split('@')[1]

    # Check if this organization already exists
    cur.execute(
        'SELECT count FROM Counts WHERE org = ?',
        (org,)
    )

    row = cur.fetchone()

    # If organization is not in the table, insert it
    if row is None:
        cur.execute(
            'INSERT INTO Counts (org, count) VALUES (?, 1)',
            (org,)
        )

    # Otherwise, increase its count
    else:
        cur.execute(
            'UPDATE Counts SET count = count + 1 WHERE org = ?',
            (org,)
        )

# Save all changes once (faster than committing inside the loop)
conn.commit()

# SQL query to display the top 10 organizations
sqlstr = '''
SELECT org, count
FROM Counts
ORDER BY count DESC
LIMIT 10
'''

# Print the results
for row in cur.execute(sqlstr):
    print(row[0], row[1])

# Close the cursor and connection
cur.close()
conn.close()