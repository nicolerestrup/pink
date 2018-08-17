import datetime
def number(the_date):
    #something = number(round(the_date,2))
    format = "%y-%m-%d-%H %M:%S"
    print(the_date.replace(microsecond = 0))




tid = datetime.datetime.now()
number(tid)
