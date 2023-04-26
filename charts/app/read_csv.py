import csv

def read_csv(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter= "," )
        header = next(reader)
        data = []
        #print(list(reader))#reader tiene una lista de listas, donde cada lista independiente es una fila
        for row  in reader:
            
            iterable = zip(header, row)
            country_dict = {key : value for key, value in iterable}
            data.append(country_dict)
            #print(list(iterable))
            #print("***" * 5)
          #  print(row)
        return data

if __name__ == "__main__":
    data = read_csv("./charts/app/data.csv")
    print(data)