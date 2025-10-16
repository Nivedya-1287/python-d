#1
has_account = True
email_verified = False
#2
can_login = has_account and email_verified
#3
email = "g@example.com"
is_email_valid = "@" in email
#4
user_age = 17
is_age_valid = user_age >= 18
#5
can_login_final = has_account and email_verified and is_email_valid and is_age_valid
#6
print("Can login (first check):", can_login)
print("Is email valid:", is_email_valid)
print("Is age valid:", is_age_valid)
print("Final login allowed:", can_login_final)
#7
print("Has account is True:", has_account is True)