import pyodbc
from datetime import date
import random

# Define The ConnectionString of SQL Database
conn_str = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:sql-apio-any.database.windows.net;DATABASE=db-apio-any;UID=sqladmin;PWD=Apio2021@"id_Prefix = "1GBJ7T1C1YJ51"
possible_EngineSizes = [3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000]
possible_Tonnages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
possible_FuelTypes = ["Diesel", "Benzin", "Electric"]
possible_Maunfacturers = ["Daimler", "Iveco", "Volvo", "GMC", "Scania"]
possible_FirstRegYears = [2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
possible_FirstRegMonths = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
possible_PlateLetters = ["B", "M", "FR", "MH", "F", "D", "J"]
possible_RegPlusYears = [0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def corporate_data_generator():
    f_date = date(2015, 11, 3)
    l_date = date.today()
    delta = l_date - f_date

    i = delta.days-6
    while (i <= delta.days):
        vin = id_Prefix + str(i)
        engine_size = random.choice(possible_EngineSizes)
        tonnage = random.choice(possible_Tonnages)
        fuel_type = random.choice(possible_FuelTypes)
        manufacturer = random.choice(possible_Maunfacturers)
        first_reg_year = random.choice(possible_FirstRegYears)
        first_reg_month = random.choice(possible_FirstRegMonths)

        str_TQuery1 = "Insert Into Trucks (TruckId, Vin, EngineSize, Tonnage, FuelType, Manufacturer, FirstRegDate)"
        str_TQuery2 = f" VALUES ({str(i)}, '{vin}', {engine_size}, {tonnage}, '{fuel_type}', '{manufacturer}', '{first_reg_year}-{first_reg_month}-15')"
        str_TQuery = str_TQuery1 + str_TQuery2
        executeQuery(str_TQuery)

        plate_letter = random.choice(possible_PlateLetters)
        reg_plus_years = random.choice(possible_RegPlusYears)
        reg_year_raw = first_reg_year + reg_plus_years
        reg_year = 2020 if (reg_year_raw > 2020)  else reg_year_raw

        str_RQuery1 = "Insert Into Registrations (RegistrationId, Vin, LicencePlate, RegistrationDate)"
        str_RQuery2 = f" VALUES ({str(i)}, '{vin}', '{plate_letter}-AP-{str(i)}', '{reg_year}-{first_reg_month}-15');"
        str_RQuery = str_RQuery1 + str_RQuery2
        executeQuery(str_RQuery)

        if(i%5==0):
            new_reg_year = (reg_year + 2) if (reg_year <= 2018) else reg_year
            new_tr_id = i + 5000
            str_RRQuery1 = "Insert Into Registrations (RegistrationId, Vin, LicencePlate, RegistrationDate)"
            str_RRQuery2 = f" VALUES ({new_tr_id}, '{vin}', '{plate_letter}-AP-{new_tr_id}', '{new_reg_year}-12-25');"
            str_RRQuery = str_RRQuery1 + str_RRQuery2
            executeQuery(str_RRQuery)

        i = i + 1

def executeQuery(strQuery):
    cnxn = pyodbc.connect(conn_str)
    cursor = cnxn.cursor()
    cursor.execute(strQuery)
    cnxn.commit()

if __name__ == '__main__':
    print ( "Data Generator Quickstart" )
    print ( "Press Ctrl-C to exit" )
    corporate_data_generator()
