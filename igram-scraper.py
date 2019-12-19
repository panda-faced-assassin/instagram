from igramscraper.instagram import Instagram 
# from context import Instagram

instagram = Instagram()

bernie_account = instagram.get_account('berniesanders')

bernie_external_url = bernie_account.external_url
bernie_id = bernie_account.identifier
bernie_is_verified = bernie_account.is_verified
bernie_username = bernie_account.username 
bernie_full_name = bernie_account.full_name
bernie_bio = bernie_account.biography
bernie_profile_pic_url = bernie_account.get_profile_picture_url()
bernie_num_published_posts = bernie_account.media_count
bernie_num_followers = bernie_account.followed_by_count
bernie_num_follows = bernie_account.follows_count

bernie_account_info = {'external url': bernie_external_url,
                        'account id': bernie_id,
                        'is verified': bernie_is_verified,
                        'username': bernie_username,
                        'full name': bernie_full_name,
                        'bio': bernie_bio,
                        'profile picture url': bernie_profile_pic_url,
                        'number of published posts': bernie_num_published_posts,
                        'number of followers': bernie_num_followers,
                        'number of follows': bernie_num_follows
                        }

print(bernie_account_info)