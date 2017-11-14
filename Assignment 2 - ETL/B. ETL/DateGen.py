from datetime import date
from dateutil.relativedelta import relativedelta

def gendates(days_back, days_total):
    startDt = date.today() + relativedelta(days=+(-1 * days_back))
    for dateOff in range(days_total):
        dimDate = startDt + relativedelta(days=+dateOff)
        print ('k' + str(dateOff), dimDate, dimDate.year, str (dimDate.year) + 'm' + str(dimDate.month))

