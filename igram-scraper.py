from igramscraper.instagram import Instagram 

instagram = Instagram()

subjects = ['berniesanders']

def get_accounts():
    accounts = []
    for subject in subjects:
        account = instagram.get_account(subject)
        accounts.append(account)
    return accounts

def get_account_data():
# Create data dict
    account_data_dict = {}
# Create object variable
    accounts = get_accounts()
# Create {key: value} pairs
    for account in accounts:
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

account_data = get_account_data()
print(account_data)