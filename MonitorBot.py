import shutil
# https://stackabuse.com/how-to-copy-a-file-in-python/
import datetime
import os

#funcions
def logger(logstring):
    if debug:
        print(logstring)

# function to send Emails
def sendEmail(fromEmail, toEmail, thesubject, thebody):
    import smtplib
    from email.mime.text import MIMEText
    msg = MIMEText(thebody)

    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = thesubject

    server = smtplib.SMTP("mail-gw.ent.nwie.net",25)
    server.send_message(msg)
    server.quit()

# global variables

fromEmailAddress = "noreply.ref67bot.monitor@nationwide.com"
toEmailAddress = "cognizant.plpc.rpa@nationwide.com"
reportsEmailAddresses = "gimeia1@nationwide.com"
debug = True
headerfields = list()
dataMap = {}

now = datetime.datetime.now()

#check what day it is today and quit if not weekday Monday = 0 and Sunday = 6
# Do not Run on Weekends
if now.isoweekday() > 5:
    quit()

# print(now.isoweekday())
dateToday = f"{datetime.datetime.now():%d-%m-%Y}".lstrip('0')
hourNow = now.hour
minuteNow = now.minute

logger (dateToday)

# Only Run between 6am and 10pm
if not(hourNow in range(7,22)):
    quit()

# set flag to send processed report on top of each odd hour (7,9,11...)
if hourNow%2 > 0:
    if minuteNow >= 0 and minuteNow < 15:
        sendReport = True

# sendEmail(fromEmailAddress, toEmailAddress, "Testing from Python", "TESTING")

inFolder = "X:\PLBPO\ACUMANUM\MultiReferral\Reports"
#"\\ohlewnas300s\BPORobotics\PLBPO\ACUMANUM\MultiReferral\Reports"
todaysLogFile = inFolder + "\ReportFile_ " + dateToday + ".csv"

logFileCreated = False

if os.path.exists(todaysLogFile):
    logFileCreated = True
    logger('...Non-timestamped log File Created')
elif os.path.exists(inFolder):
    logger('...checking for time-stamped log file')
    for subdir, dirs, files in os.walk(inFolder):
        for file in files:
            if ("ReportFile_" in file) and (dateToday in file):
                #logger (os.path.join(subdir, file))
                todaysLogFile = os.path.join(subdir, file)
                logFileCreated = True

logger (todaysLogFile)
if logFileCreated:
    head, tail = os.path.split(todaysLogFile)
    shutil.copy(todaysLogFile,tail)
    fin = open(tail,'r')
    counter = 0
    for line in fin:
        counter = counter + 1
        logger(line)
        if counter == 1:
            if "," in line:
                delimiter = ","
            else:
                delimiter = ";"
            headerfields = line.split(delimiter)
        else:
            datafields = line.split(delimiter)
            for field in headerfields:
                dataMap[field] = datafields[headerfields.index(field)]


logger(dataMap)

#timediff = datetime.datetime.fromtimestamp(dataMap["TransactionStartTime"]) - datetime.fromtimestamp(dataMap["TransactionEndTime"])

#print(timediff.time())


