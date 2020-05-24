import dependency_injector.containers as containers
import dependency_injector.providers as providers
from .ioc_class import APIConnection,DogToJSON,DogToCSV,das
import json
class Container(containers.DeclarativeContainer):
    api_connection = providers.Singleton(APIConnection,
                                         url='http://127.0.0.1:8000/dog-api/?format=json')
    download_json =  providers.Singleton(DogToJSON,
                                         data=api_connection)
    download_csv = providers.Singleton(DogToCSV,
                                         data=api_connection)


if __name__ == '__main__':
    container = Container()
    a_file = open("data.json", "w")
    json.dump(das(container.api_connection()), a_file)
    a_file.close()
    # print(das(container.api_connection())[0])
    # print(container.api_connection)
