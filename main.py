country_code = {'India': '0091', 'Australia': '0025', "Nepal": '00977', "Bangladesh": '00880', 'United Kingdom': '0044', 'Albania': '00355', 'Algeria': '00213', "Argentina": '0054', 'Austria': '0043'}


print(country_code.get('Nepal', 'Nepal Not found'))

print(country_code.get('India', 'India Not found'))

print(country_code.get('Australia', 'Australia Not found'))
