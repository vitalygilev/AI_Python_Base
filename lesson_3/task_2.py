def get_user_data(**kwargs):
    user_info = "User information: "
    for param_name, param_value in kwargs.items():
        if param_value != "":
            user_info = user_info + param_name + " = " + str(param_value) + ","
    return user_info[:len(user_info) - 1]


print(get_user_data(first_name="Alister", last_name="Crowley", bitrh_year=1875, city="London", email="", tel=""))
