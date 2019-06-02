import csv

with open('q&a.csv', newline='') as csvfile, open('data.sql', 'w', newline='') as sqlfile:
    rows = csv.reader(csvfile)
    category = ''
    content = ''
    for row in rows:
        if row[1].startswith('100'):
            category = row[1]
        if row[4]:
            content = row[4]
            if category and content:
                sqlfile.write('INSERT INTO `talk`(`category`,`content`) VALUES ( \'' + category + '\', \'' + content + '\');\n')
