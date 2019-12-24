from igramscraper.instagram import Instagram
from time import sleep

instagram = Instagram()
sleep(2)

subjects = ['berniesanders', 'realdonaldtrump']

# Get account objects
def get_accounts():
    accounts = []
    for subject in subjects:
        account = instagram.get_account(subject)
        accounts.append(account)
    return accounts

# Get account data
def get_account_data(account):
    account_data_dict = {}
    account_data_dict['account_external_url'] = account.external_url
    account_data_dict['account_id'] = account.identifier
    account_data_dict['account_is_verified'] = account.is_verified
    account_data_dict['account_username'] = account.username 
    account_data_dict['account_full_name'] = account.full_name
    account_data_dict['account_bio'] = account.biography
    account_data_dict['account_profile_pic_url'] = account.get_profile_picture_url()
    account_data_dict['account_num_published_posts'] = account.media_count
    account_data_dict['account_num_followers'] = account.followed_by_count
    account_data_dict['account_num_follows'] = account.follows_count
    return account_data_dict

# account_data_dicts = []
# accounts = get_accounts() 
# for account in accounts: 
#     account_data = get_account_data(account)
#     account_data_dicts.append(account_data)
# print(account_data_dicts)

# Get follower data
def get_followers(account):
    account_followers = {}
    for subject in subjects:
        username = subject
        sleep(1)
        followers = instagram.get_followers(account.identifier, 10, 1, delayed=True) # Get 10 followers of 'subject', 1 at a time with random delay in between requests. 
        account_followers[subject] = followers
    return account_followers

account_followers_dicts = []
accounts = get_accounts() 
for account in accounts: 
    account_followers = get_followers(account)
    account_followers_dicts.append(account_followers)
print(account_followers_dicts)



