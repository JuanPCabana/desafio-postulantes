import json
from selenium.webdriver import Chrome



def create_table(table_rows):
    
    
    '''
        Esta funcion recibe como parametro una lista que contiene todas las filas de la tabla presentada en la pagina.
    
        luego en la primera iteracion del for se crea la lista de las cabeceras de la tabla 
        que serviran como llaves para el diccionario con la data de cada una de las filas
    
        posteriormente se empaqueta las cabeceras con los datos de la fila correspondiente y luego se le agrega al diccionario final 
        el cual sera el json, haciendo uso de la variable auxiliar (i) para que sea la llave del diccionario final.
    
        retorna la tabla final
    '''    
    
    i = 0
    headers = []
    table_item = {}
    table = {}
        
    for row in table_rows:
        
        row_data = []
        header_row = row.find_elements_by_tag_name('th')
        parameters = row.find_elements_by_tag_name('td')
        

        if i == 0:
            for header in header_row:
                headers.append(header.text)

            i += 1

        else:
            for data in parameters:
                row_data.append(data.text)

            row_item = dict(zip(headers, row_data))

            key = str(i)         
            table_item[key] = row_item
            i += 1

            table.update(table_item)
    return table    



if __name__ == '__main__':
    
    # se crea la instancia de chrome con selenium
    # se debe tener el ChromeDriver.exe en la misma carpeta del script
    
    driver = Chrome('./chromedriver.exe')
    
    # se accede a la pagina correspondiente
    
    driver.get('https://www.sii.cl/servicios_online/1047-nomina_inst_financieras-1714.html')
    
    # se obtienen las filas de la tabla
        
    table_rows = driver.find_elements_by_tag_name('tr')
    
    # se abre el archivo donde se van a guardar los datos
    
    with open('./tabla.json', 'w', encoding='utf_8') as f:
        
        table = create_table(table_rows)
        
        # se guardan los datos en el archivo
            
        f.write(json.dumps(table, indent=4, ensure_ascii=False))
        f.write('\n')
    
    # se termina la instancia del navegador            
               
    driver.close()
  