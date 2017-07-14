#!/usr/bin/env python

months = ['January','Febrary','march','april','may','june','july','august','Septemper','October','November','December']

endings = ['st','nd','rd']+ 17*['th'] \
    +['st','nd','rd']+7*['th'] \
    +['st']

year = raw_input("year:")
month = raw_input("month:")
day = raw_input("day")

month_num = int(month)
day_num = int(day)

month_name = months[month_num -1]
day_name = day+endings[day_num - 1]

print month_name+' '+day_name+' ' +year 


