from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests



#### search tool #####

search_tool = DuckDuckGoSearchRun()
# for testing the tool
# result =search_tool.invoke("explain quantum computing in simple terms")
# print("Search Result:", result)



#### weather tool #####

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'

  response = requests.get(url)

  return response.json()
