import matplotlib.pyplot as pylot

def generate_pie_chart(name,labels = ["A", "B", "C"],values = [200, 34, 120] ):
    
    fig, ax = pylot.subplots()
    ax.pie(values,labels=labels)
    pylot.savefig(f"./charts/img/{name}.png")
    pylot.close()
    #pylot.show()


if __name__ == "__main__":
    generate_pie_chart()