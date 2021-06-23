country_names = input().split(', ')
capital_cities = input().split(', ')

c = zip(country_names, capital_cities)
a = [print(f"{turtle[0]} -> {turtle[1]}") for turtle in c]