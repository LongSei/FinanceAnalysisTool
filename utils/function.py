from datetime import date, timedelta
import datetime

def forDate(beginTime, endTime, timeFormat='%Y-%m-%d'):
    def daterange(beginTime, endTime):
        for n in range(int((endTime - beginTime).days)):
            yield beginTime + timedelta(n)

    def str2date(date_string, timeFormat): 
        date = datetime.datetime.strptime(date_string, timeFormat)
        return date

    beginTime = str2date(beginTime, timeFormat)
    endTime = str2date(endTime, timeFormat)

    result = []
    for single_date in daterange(beginTime, endTime):
        result.append(single_date.strftime(timeFormat))
    return result

def reMaskValue(values: list) -> list: 
    sorted(values)
    newValues = {}
    cnt = 0
    for i in range(0, len(values)): 
        if values[i] in newValues.keys(): 
            values[i] = newValues[values[i]]
        else: 
            newValues[values[i]] = cnt
            cnt += 1
            values[i] = newValues[values[i]]
    return {'newList': values, 'amountMask': cnt}
