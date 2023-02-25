import utils
import read_csv
import charts

def run():
  
  data = read_csv.read_csv('app/world_population.csv')
  country = input('Ingresa el pais que desea => ')
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

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
 
  if option == '1':
    option ='Asia'
  elif option == '2':
    option ='Europe'
  elif option == '3':
    option ='Africa'
  elif option == '4':
    option ='Oceania'
  elif option == '5':
    option = 'North America'
  elif option == '6':
    option = 'South America'
  else:
    print("Ingrese la opcion indicada en el menu")

  data = list(filter(lambda item: item['Continent'] == option, data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(option, countries, percentages)

if __name__ == '__main__':
  run()