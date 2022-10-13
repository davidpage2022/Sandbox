""" Load country data and display sorted and formatted """

FILENAME = "countries.csv"


def main():
    countries = load_data()
    # print(countries)
    sort_countries(countries)
    display_countries(countries)


def load_data():
    return
    [ #Country (or territory),Capital,Population,% of country,Source,
"China","Beijing","21,542,000",1.50,2010,
"Japan","Tokyo","13,921,000",11.20,2019,
"DR Congo","Kinshasa","12,691,000",13.20,2017,
"Russia","Moscow","12,655,050",8.70,2021]
    # with open(FILENAME) as in_file:
    #     print(in_file.readline())
    #
    # return []  # Or {}


def sort_countries(countries):
    pass


def display_countries(countries):
    pass


main()
