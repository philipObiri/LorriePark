def user_listing_path(instance, filename):
    return "seller_{0}/listings/{1}".format(instance.seller.user.username, filename)
