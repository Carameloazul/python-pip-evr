from app.read_csv import read_csv
from app.types_charts import generate_bar_chart

complete_data = read_csv("./charts/app/data.csv")

def country_population():
    population = {}
    search_country = input("Ingrese el país a buscar ")
    for country in complete_data:  
        if country['Country/Territory'] == search_country:
            population = {key[:4] : int(value) for (key, value) in country.items() if key[:4].isnumeric()}
            #value tengo que convertirlo a int para que matplotlib lo lea bien
            return search_country,population.keys(), population.values()
    return f"No se ha encontrado {search_country}"  

if __name__ == "__main__":
    country_name,labels, value = country_population()    
    generate_bar_chart(labels, value)
    