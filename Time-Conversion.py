from datetime import datetime

def timeConversion(s):
  return datetime.strftime(datetime.strptime(s, '%I:%M:%S%p'), '%H:%M:%S')
