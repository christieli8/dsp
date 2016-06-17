# Hint:  use Google to find python function

from datetime import datetime

def get_days(d_start, d_stop, fmt):
  start = datetime.strptime(d_start, fmt)
  stop = datetime.strptime(d_stop, fmt)
  return (stop-start).days

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

days_1 = get_days(date_start, date_stop, "%m-%d-%Y")
print 'days: ', days_1


####b)  
date_start = '12312013'  
date_stop = '05282015'  

days_2 = get_days(date_start, date_stop, "%m%d%Y")
print 'days: ', days_2

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

print 'days: ', days_3
