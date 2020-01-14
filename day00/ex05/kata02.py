import datetime


t = (3, 30, 2019, 9, 25)
x = datetime.datetime(t[2], t[3], t[4])

print(x.strftime("%x"), " {:0>2d}".format(t[0]), ":", "{:0>2d}".format(t[1]), sep="")
