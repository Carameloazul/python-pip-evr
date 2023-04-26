from read_csv import read_csv
from charts import generate_pie_chart


def world_population():
    all_country = read_csv("./charts/app/data.csv")
    
    filter_countries = filter(lambda x:x['Continent']=='South America',all_country)
    population_countries = {}
    for country in filter_countries:   
        print(country)
        population_countries[country['Country/Territory']]=country['World Population Percentage']
                
    return population_countries.keys(), population_countries.values()









if __name__ == "__main__":
    keys,values = world_population()    
    generate_pie_chart(keys, values)
    