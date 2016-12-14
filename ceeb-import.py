import csv
reader = csv.reader(open("ceeb.csv", "r"))
for row in reader:
    ceeb, name, city, state = row
    ceeb = ceeb.lstrip('0')
    if College.objects.filter(ceeb=ceeb).count() == 0:
        College.objects.create(ceeb=ceeb, name=("{} - {}, {}".format(name, city, state)).title())
