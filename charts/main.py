from app.read_csv import read_csv
import app.challenge_1 as challenge
print("OK! Todo bien hasta aquí")
from charts import generate_pie_chart


def run():
    country_name,labels, values = challenge.country_population()
    #reading_csv = read_csv("./charts/app/data.csv")
    generate_pie_chart(country_name,labels, values)



if __name__ == "__main__":
    run()