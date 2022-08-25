from sqlalchemy import create_engine
import pandas as pd
import requests

def main():
    
    url="https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios";
    response = requests.get(url)
    df = pd.DataFrame.from_dict(response.json())
    

    tableName    = "usuarios"
    dataFrame    = pd.DataFrame(data=df)
    sqlEngine    = create_engine('mysql+pymysql://root:root@mydb/api', pool_recycle=3600)
    dbConnection = sqlEngine.connect()

    try:
        dataFrame.to_sql(tableName, dbConnection, if_exists='fail');
    except ValueError as vx:
        print(vx)
    except Exception as ex:
        print(ex)
    else:
        print("Tabla %s creada exitosamente."%tableName);
    finally:
        dbConnection.close()
    
if __name__ == '__main__':
    main()