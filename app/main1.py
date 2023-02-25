import utils
import read_csv
import charts

def run():

  menu = """"
Elija un contiente que desea vizualizar

1 - Asia
2 - Europe
3 - Africa
4 - Oceania
5 - North America
6 - South America

"""

  option = input(menu)

  def continent(option):
    data = read_csv.read_csv('/home/erick/Descargas/world_population.csv')
    data = list(filter(lambda item: item['Continent'] == option, data))
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts.generate_pie_chart(countries, percentages)

  if option == '1':
      continent('Asia')
  elif option == '2':
      continent('Europe')
  elif option == '3':
      continent('Africa')
  elif option == '4':
      continent('Oceania')
  elif option == '5':
      continent('North America')
  elif option == '6':
      continent('South America')
  else:
      print("Ingrese la opcion indicada en el menu")

  


if __name__ == '__main__':
  run()