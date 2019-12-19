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
# Create account_data dict
#     account_data = {'external url': account_external_url,
#                     'account id': account_id,
#                     'is verified': account_is_verified,
#                     'username': account_username,
#                     'full name': account_full_name,
#                     'bio': account_bio,
#                     'profile picture url': account_profile_pic_url,
#                     'number of published posts': account_num_published_posts,
#                     'number of followers': account_num_followers,
#                     'number of follows': account_num_follows
#                     }
    account_data_dict = {}
# Create user_account variable
    accounts = get_accounts()
# Create account data variables
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

# bernie_account = instagram.get_account('berniesanders')

# bernie_external_url = bernie_account.external_url
# bernie_id = bernie_account.identifier
# bernie_is_verified = bernie_account.is_verified
# bernie_username = bernie_account.username 
# bernie_full_name = bernie_account.full_name
# bernie_bio = bernie_account.biography
# bernie_profile_pic_url = bernie_account.get_profile_picture_url()
# bernie_num_published_posts = bernie_account.media_count
# bernie_num_followers = bernie_account.followed_by_count
# bernie_num_follows = bernie_account.follows_count

# bernie_account_info = {'external url': bernie_external_url,
#                         'account id': bernie_id,
#                         'is verified': bernie_is_verified,
#                         'username': bernie_username,
#                         'full name': bernie_full_name,
#                         'bio': bernie_bio,
#                         'profile picture url': bernie_profile_pic_url,
#                         'number of published posts': bernie_num_published_posts,
#                         'number of followers': bernie_num_followers,
#                         'number of follows': bernie_num_follows
#                         }

account_data = get_account_data()
print(account_data)