import csv
reader = csv.reader(open("ceeb.csv", "r"))
numeric = '0123456789'
for row in reader:
    ceeb, name = row[:2]
    ceeb = ceeb.lstrip('0')
    if College.objects.filter(ceeb=ceeb).count() == 0:
        if ceeb[0] not in numeric:
            state = ceeb[:2]
            city = 'INTL'
        else:
            state, city = row[2:4]

        College.objects.create(ceeb=ceeb, name=("{} - {}, {}".format(name, city, state)).title())
