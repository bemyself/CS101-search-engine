#Given the variable countries defined as:


#             Name      Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

#Write code to print out the capital of India
#by accessing the array.

def find_cap (country):
    for i in range(len(countries)):
        for j in range(len(countries[i])):
            if countries[i][j] == country:
                print countries[i][j+1]

find_cap('India')
