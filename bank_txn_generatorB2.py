import csv
import random
import datetime
from datetime import datetime
from datetime import timedelta
from random import randint
import sys

if (len(sys.argv) < 2): print 'invalid num of arguments: arg1: output file'
# args are 0: numLines, 1: output file

channel_type_arr = [
    1001,
    1002,
    2001,
    2002,
    2003,
    2004,
    3001,
    3002,
    3003,
    3004,
    3005,
    3006
]

transaction_location_arr = [
    'North Carolina',
    'Texas',
    'North Dakota',
    'Iowa',
    'Ohio',
    'Connecticut',
    'New York',
    'California',
    'Colorado',
    'Florida',
    'Tennessee',
    'Minnesota',
    'South Carolina',
    'Indiana',
    'Utah',
    'Maryland',
    'Michigan',
    'Illinois',
    'Missouri',
    'Kansas',
    'Mississippi',
    'Louisiana',
    'Georgia',
    'District of Columbia',
    'West Virginia',
    'Idaho',
    'New Jersey',
    'Hawaii',
    'New Mexico',
    'Alabama',
    'Oklahoma',
    'Pennsylvania',
    'Arkansas',
    'Maine',
    'Massachusetts',
    'Oregon',
    'Washington',
    'Nevada',
    'Virginia',
    'Arizona',
    'Kentucky',
    'New Hampshire',
    'Delaware',
    'Wisconsin',
    'Montana',
    'Wyoming',
    'Nebraska',
    'South Dakota',
    'Alaska',
    'Rhode Island',
]

num_users = 199 #99
users_start = 20000001 #starting user id
transaction_id_start = 50000000 #starting transaction number
transaction_floor = -500 #minimum account balance
transaction_ceiling = 100000 #maximum account balance
transaction_min = 10 #min amount per transaction
transaction_max = 10000 #max amount per transaction
transaction_per_account = 20 #10000

# yyyy/mm/dd
start_date= datetime(2016,12,21) #lower limit for random datetime
end_date= datetime(2016,12,31) #upper limit for random datetime

def random_date(start, end):
    return start + timedelta(seconds=randint(0, int((end - start).total_seconds())))

def flip(str):
    if str == "CR": return "DB"
    return "CR"

g=open(sys.argv[1],"w")
w=csv.writer(g, lineterminator='\n')
w.writerow(('Account_Number','Transaction_Time','Credit_Debit_Indicator','Account_Balance','Channel_Type',
            'Transaction_Amount','Previous Balance','Transaction_Currency','Transaction_Location','Transaction_ID'))

user_acc_balance = [0] * num_users

for i in xrange(num_users):

    user_acc_balance[i] = 0

    list_of_dates = []

    for k in xrange(transaction_per_account):
        list_of_dates.append(random_date(start_date, end_date))

    list_of_dates.sort()

    for j in xrange(transaction_per_account):

        skip = False

        account_number = users_start + i

        transaction_time = list_of_dates[j]

        credit_debit_indicator = random.choice(["CR", "DB"])
        
        channel_type = random.choice(channel_type_arr)

        transaction_amount = randint(transaction_min, transaction_max)

        previous_balance = user_acc_balance[i]
        
       
        if (credit_debit_indicator == "DB"):
            if ((user_acc_balance[i] + transaction_amount) < transaction_ceiling):
                user_acc_balance[i] += transaction_amount
            else:
                credit_debit_indicator = flip(credit_debit_indicator)
                user_acc_balance[i] -= transaction_amount
                skip = True
        if (credit_debit_indicator == "CR" and not skip):
            if ((user_acc_balance[i] - transaction_amount) > transaction_floor):
                user_acc_balance[i] -= transaction_amount
            else:
                credit_debit_indicator = flip(credit_debit_indicator)
                user_acc_balance[i] += transaction_amount

        account_balance = user_acc_balance[i]

        transaction_currency = "USD"

        transaction_location = random.choice(transaction_location_arr)

        transaction_id = transaction_id_start + i*transaction_per_account + j

        w.writerow((
            account_number,
            transaction_time,
            credit_debit_indicator,
            account_balance,
            channel_type,
            transaction_amount,
            previous_balance,
            transaction_currency,
            transaction_location,
            transaction_id
        ))

