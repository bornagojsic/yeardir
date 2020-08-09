import datetime
import os
from time import sleep

n = 30
y_m_dir = ["", ""]


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total:
        print()


def create_dir(var, i):
    if i in [0, 1]:
        y_m_dir[i] = os.getcwd()
    dir_name = str(var)
    os.mkdir(dir_name)
    os.chdir(dir_name)


def make(dates):
    syear = int(dates[0])
    eyear = int(dates[1])

    try:
        _ = datetime.date(syear, 1, 1)
    except:
        print("Enter a valid starting year!")
        syear = custom_input(1, 'year')

    try:
        _ = datetime.date(eyear, 1, 1)
    except:
        print("Enter a valid ending year!")
        syear = custom_input(0, 'year')

    print("Starting to create folders...")

    years = eyear - syear

    for year in range(syear, eyear + 1):
        if years:
            printProgressBar(year - syear, years, prefix = "Progress:", suffix = "Complete", length = 50)
            sleep(.01)
        else:
            printProgressBar(1, 1, prefix = "Progress:", suffix = "Complete", length = 50)
        create_dir(year, 0)
        for month in range(1, 13):
                create_dir(month, 1)
                delta = ( datetime.date(year, month + 1, 1) if month != 12 else datetime.date(year + 1, month, 1) ) - datetime.date(year, month, 1)
                for date in [(datetime.date(year, month, 1) + datetime.timedelta(days=i)).strftime('%d') for i in range(delta.days)]:
                    os.mkdir(str(date))
                    if date == '31' and month == 12:
                        break
                os.chdir(y_m_dir[1])
        os.chdir(y_m_dir[0])

    print("Folders are created!")


def main():
    make([input(f"Enter the {'start' if i else 'end'}ing year: ") for i in (1,0)])
    

if __name__ == '__main__':
    main()
    input("Press Enter to exit!")