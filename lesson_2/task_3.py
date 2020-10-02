# I understand we didn't learn functions yet but my eyes bleed when I see code dubbing...
def check_raw_data(raw_month_arg):
    if raw_month_arg.isdigit():
        month_mun_loc = int(raw_month_arg)
        if month_mun_loc > 12 or month_mun_loc < 0:
            month_mun_loc = 0
    else:
        month_mun_loc = None
    return month_mun_loc


# Get Season by month (List & Dict 2-in-1)
months_corr = [["январь", "january"],
               ["февраль", "february"],
               ["март", "march"],
               ["апрель", "april"],
               ["май", "may"],
               ["июнь", "june"],
               ["июль", "july"],
               ["август", "august"],
               ["сентябрь", "september"],
               ["октябрь", "october"],
               ["ноябрь", "november"],
               ["декабрь", "december"]]
season_corr = {12: 'winter', 1: 'winter', 2: 'winter',
               3: 'spring', 4: 'spring', 5: 'spring',
               6: 'summer', 7: 'summer', 8: 'summer',
               9: 'fall', 10: 'fall', 11: 'fall'}
month_mun = 0
while month_mun == 0:
    raw_month = input("Enter month (or *** for exit):")
    if raw_month == '***':
        break
    month_mun = check_raw_data(raw_month)
    if month_mun == 0:
        print("Enter correct month number (1 to 12)!")
    elif month_mun is None:
        raw_month = raw_month.lower().strip()
        for can_num in range(len(months_corr)):
            candidate = months_corr[can_num]
            if raw_month in candidate:
                month_mun = can_num + 1
                break
        # Do some education
        if month_mun is None:
            print("You've been mistaken in month's name or you use new language. Choose one of 2 options:")
            new_month = input("Enter 1-12 for new month name remember or something else to reenter correct month:")
            month_mun = check_raw_data(new_month)
            if month_mun is None:
                month_mun = 0
            else:
                months_corr[month_mun - 1].append(raw_month.lower().strip())
    if month_mun != 0:
        print(f"For month {raw_month} season is {season_corr[month_mun]}.")
    month_mun = 0
