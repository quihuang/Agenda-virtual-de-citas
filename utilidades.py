import re
from datetime import datetime

def validateTypeDocument (typeDoc: str) -> str:

    """
    Función encargada de validar si el tipo de documento ingresado es correcto.

    Parameters
    ------------------
    typeDoc : str
        Numero de la opcion del documento.

    Returns
    ------------------
    validateTypeDoc : str
        Retorna el tipo de documento, de lo contrario devuelve un INVALID
    """

    validateTypeDoc = ""

    if(typeDoc == "1"):
        validateTypeDoc = "CC"
    elif(typeDoc == "2"):
         validateTypeDoc = "CE"
    elif(typeDoc == "3"): 
         validateTypeDoc = "TI"
    elif(typeDoc == "4"):
         validateTypeDoc = "PA"
    else:
        validateTypeDoc = "INVALID"
 
    return validateTypeDoc

def validateDocumentNumber (numberDoc: str) -> bool:

    """
    Función encargada de validar si el numero de documento ingresado es correcto.

    Parameters
    ------------------
    numberDoc : str
        Numero de documento.

    Returns
    ------------------
    valNumDoc : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNumDoc = False
    NumDoc = bool(re.search(r'^\d+$', numberDoc))
    lenNumDoc = len(numberDoc)

    if(NumDoc and lenNumDoc <= 12):
        valNumDoc = True

    return valNumDoc 

def validateNameAndLastName (namesOrLastName: str) -> bool:
    
    """
    Función encargada de validar si nombre o el apellido ingresado es correcto.

    Parameters
    ------------------
    namesOrLastName : str
        Nombre o apellido del suario.

    Returns
    ------------------
    valNumDoc : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNamesDig = bool(re.search(r'\d', namesOrLastName))
    valNames = False

    if(namesOrLastName != "" and valNamesDig !=True and len(namesOrLastName) <= 30):
        valNames = True
    return valNames

def validateBirthDate (date: str) -> bool:

    """
    Función encargada de validar la fecha de nacimiento ingresada es correcto.

    Parameters
    ------------------
    date : str
        fecha de nacimiento.

    Returns
    ------------------
    valDate : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """
    
    valDate = False
    try:
        datetime.strptime(date, '%Y-%m-%d')
        valDate = True
    except:
        valDate = False

    return valDate

def calculateAge (birthDate: str) -> int:

    """
    Función encargada de calcular la edad del usuario.

    Parameters
    ------------------
    birthDate : str
        fecha de nacimiento.

    Returns
    ------------------
    age : int
        Retorna la edad actual del usuario
    """

    daybirthDate = datetime.strptime(birthDate, '%Y-%m-%d')
    currentDate = datetime.now()

    age = currentDate.year - daybirthDate.year

    return age

def validateBloodType (bloodType: str) -> bool:

    """
    Función encargada de validar el tipo de sangre del usuario.

    Parameters
    ------------------
    bloodType : str
        Grupo sanguineo del usuario.

    Returns
    ------------------
    valBloodType : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    letter = ["O","A","B"]
    sign = ["+","-"]
    
    valBloodType = False
    if(len(bloodType) == 2):
        for l in letter :
            if(bloodType[0].upper() == l):
                for s in sign :
                    if(bloodType[1].upper() == s):
                         valBloodType = True

    return valBloodType
        
def validateEmail (email: str) -> bool:

    """
    Función encargada de validar el correo electronico del usuario.

    Parameters
    ------------------
    email : str
        correo electronico del usuario.

    Returns
    ------------------
    valEmail : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valEmailRex = bool(re.search(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email))
    valEmail = False

    if(valEmailRex and len(email) <=50):
        valEmail = True

    return valEmail

def validatePhoneNumber(phoneNumber: str) -> bool:

    """
    Función encargada de validar si el numero de telefono ingresado es correcto.

    Parameters
    ------------------
    phoneNumber : str
        Numero de telefono.

    Returns
    ------------------
    valNumPhone : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNumPhone = False
    NumPhone = bool(re.search(r'^\d+$', phoneNumber))
    lenNumphone = len(phoneNumber)

    if(NumPhone and lenNumphone <= 10):
        valNumPhone = True

    return valNumPhone 

def inputUserDatabase(typeDoc: str,numDoc: str,name: str,lastName: str,birthDate: str,typeBlood: str,email: str,phoneNumber: str,table: list): 

    """
    Función encargada insertar los diccionarios al array de usuarios.

    Parameters
    ------------------
    typeDoc : str
        Tipo Documento.
    numDoc : str
        Numero Documento.
    name : str
        Nombres del usaurio.
    lastName : str
        Apellidos del usaurio.
    birthDate : str
        Fecha de nacimiento del usaurio.
    typeBlood : str
        Grupo de sangre.
    email : str
        correo electronico.
    phoneNumber : str
        Numero de telefoono.
    table : list
        Array donde se van a guardar los diccionarios de los usuarios creados. 

    Returns
    ------------------
    No retorna parametros
    """

    fileUserRegister = open("D:/Frank´s User Data/OneDrive/Documentos/Universidad de Caldas/Fundamentos de Programacion/Algoritmos Python/RETO #6/archivos/pacientes.txt", "a", encoding="utf_8")

    user = {
            "Tipo Documento":typeDoc,
            "Numero Documento":numDoc,
            "Nombres":name,
            "Apellidos":lastName,
            "Fecha de nacimiento":birthDate,
            "RH":typeBlood,
            "Correo":email,
            "Numero de telefono":phoneNumber
            }

    fileUserRegister.write(str(user) + "\n")
    fileUserRegister.close()

    table.append(user)

def validateExistUser(numDoc: str,table: str) -> bool:

    """
    Función encargada de validar si un usuario ya se encuentra registrado.

    Parameters
    ------------------
    numDoc : str
        Numero de documento.
    table : str
        Array donde se guardan los usuarios 

    Returns
    ------------------
    valNumDoc : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """

    valNumDoc = False
    for doc in table:
        if doc["Numero Documento"] == numDoc:
            valNumDoc = True
    
    return valNumDoc

def validateDate (date: str) ->bool:

    """
    Función encargada de validar la fecha de la cita ingresada es correcta.

    Parameters
    ------------------
    date : str
        fecha de la cita.

    Returns
    ------------------
    valDate : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """
    
    valDate = False
    try:
        datetime.strptime(date, '%Y-%m-%d %H:%M')
        valDate = True
    except:
        valDate = False

    return valDate

def validarteDateCurrent (date: str) -> bool:

    """
    Función encargada de validar la fecha de la cita ingresada no sea inferior a la actual.

    Parameters
    ------------------
    date : str
        fecha de la cita.

    Returns
    ------------------
    valDate : bool
        Retorna un True en el caso de ser valido, de lo contrario devuelve un False
    """
    valDate = False
    dateCurrent = datetime.now()
    dateUser =  datetime.strptime(date, '%Y-%m-%d %H:%M')
    
    if(dateUser >= dateCurrent):
        valDate = True

    return valDate

def createDataAppointment (numDoc: str,date: str,tableSearch: list,tableInsert: list) -> str:

    """
    Función encargada registar una cita.

    Parameters
    ------------------
    numDoc : str
        Numero de documento del usuario.
    date : str
        Fecha de agendamiendo de la cita.
    tableSearch : list
        Array de busqueda de usuarios registrados.
    tableInsert : list
        Array donde se guarda la informacion de las citas creadas.

    Returns
    ------------------
    messageConfirm : str
        retorna el mensaje de confirmación de la creación de la cita en el siguiente formato : 
        "Estimado xxxxx, su cita fue asignada correctamente para el día xxxxxx a las xxxxx horas"
    """

    fileDataAppointment = open("D:/Frank´s User Data/OneDrive/Documentos/Universidad de Caldas/Fundamentos de Programacion/Algoritmos Python/RETO #6/archivos/citas.txt", "a", encoding="utf_8")

    DataAppointment = ()
    messageConfirm = ""

    for idUser, user in enumerate(tableSearch):
        if user["Numero Documento"] == numDoc:
            controler = idUser
            
    typeDoc = tableSearch[controler].get("Tipo Documento")
    numDoc = tableSearch[controler].get("Numero Documento") 
    name = tableSearch[controler].get("Nombres")
    lastName = tableSearch[controler].get("Apellidos")
    age = calculateAge(tableSearch[controler].get("Fecha de nacimiento"))
    asigDate = date
    
    DataAppointment = (typeDoc,numDoc,name,lastName,age,asigDate)

    fileDataAppointment.write(str(DataAppointment)+"\n")
    fileDataAppointment.close()

    tableInsert.append(DataAppointment)

    dateTemp = asigDate.split(' ')

    messageConfirm = f"\nEstimado {name} {lastName}, su cita fue asignada correctamente para el día {dateTemp[0]} a las {dateTemp[1]} horas"

    return messageConfirm

def displayAppointment(tableAppointment: list) -> str:

    """
    Función de mostrar los usuarios que tienen citas agendadas.

    Parameters
    ------------------
    tableAppointment : list
        Array de usuarios que tienen una cita agendada.

    Returns
    ------------------
    displayAppointment : str
        retorna en caso de que la lista tenga registros muestra los usuarios con
        citas agendadas en el caso q no, muestra el siguiente mensaje: (NO HAY CITAS AGENDADAS)
    """

    if(len(tableAppointment) > 0):
        displayAppointment = "\n======================================\n"
        displayAppointment += "    LISTADO DE DE CITAS AGENDADAS     \n"
        displayAppointment += "======================================\n"

        for id, users in enumerate(tableAppointment):

            displayAppointment += f"\nid : {str(id+1)}\n"
            displayAppointment += f"Tipo Documento : {str(users[0])}\n"
            displayAppointment += f"Numero Documento : {str(users[1])}\n"
            displayAppointment += f"Nombres : {str(users[2])}\n"
            displayAppointment += f"Apellidos : {str(users[3])}\n"
            displayAppointment += f"Edad : {str(users[4])}\n"
            displayAppointment += f"Fecha de cita : {str(users[5])}\n"

            displayAppointment += "\n---------------------------------------\n"
    else:

        displayAppointment = "\n---------------------------------------\n"
        displayAppointment += "         NO HAY CITAS AGENDADAS         \n"
        displayAppointment += "---------------------------------------\n"
    
    return displayAppointment

def displayUsersRegisters(tableUserRegisters: list)-> str:

    """
    Función se encarga de mostrar los usuarios que estan registrados en el sistema.

    Parameters
    ------------------
    tableUserRegisters : list
        Array de usuarios que estan registrados.

    Returns
    ------------------
    displayUsersRegisters : str
        retorna en caso de que la lista tenga registros muestra los usuarios registado en 
        el sistema en el caso q no, muestra el siguiente mensaje: (NO HAY USUARIOS REGISTRADOS)
    """

    if(len(tableUserRegisters) > 0):
        displayUsersRegisters = "\n======================================\n"
        displayUsersRegisters += "  LISTADO DE DE USUARIOS REGISTRADOS   \n"
        displayUsersRegisters += "======================================\n"

        for id, users in enumerate(tableUserRegisters):
            displayUsersRegisters += f"\nid : {str(id+1)}\n"
            for user in users:
                displayUsersRegisters += f"{user} : {str(users[user])}\n"
            displayUsersRegisters += "\n---------------------------------------\n"

        displayUsersRegisters += "======================================\n"
    else:

        displayUsersRegisters = "\n---------------------------------------\n"
        displayUsersRegisters += "      NO HAY USUARIOS REGISTRADOS      \n"
        displayUsersRegisters += "---------------------------------------\n"
    
    return displayUsersRegisters


def loadsFiles(array: list,fileName: str) -> list:

    """
    Función encargada de cargar en listas la data de los archivos .txt

    Parameters
    ------------------
    array : list
        Array donde se cargara la data.

    fileName : str
        Nombre del archivo a cargar.

    Returns
    ------------------
    array : list
        Retorna la lista ya con los datos cargados.
    """

    file = open(f"D:/Frank´s User Data/OneDrive/Documentos/Universidad de Caldas/Fundamentos de Programacion/Algoritmos Python/RETO #6/archivos/{fileName}.txt","r")
    array = []

    try:
        for linea in file:
            array.append(eval(linea))
        file.close()
        return array
    except:
        return array

    
def filterSearch(filterType: str,search: str,arrayData: list) -> list:
  
    """
    Función encargada de filtrar los datos de los pacientes y ordenarlos por apellido.

    Parameters
    ------------------
    filterType : str
        Nombre de la llave por la cual se va hacer la busqueda.

    search : str
        Valor que se quiere buscar.

    arrayData : list
        Lista de usuarios.

    Returns
    ------------------
    array : list
        Retorna la lista con los datos de las coincidencias encontradas ordenados por apellidos.
    """

    arrayMatchSearch = []
    arrayMatchSearchSort = []
    searchResult = {}
    arrayLastName = []

    # Ciclo que saca el apellido del array de mapas y lo guarda en un Array 
    for id,lastName in enumerate(arrayData):
        lastName = arrayData[id].get("Apellidos").lower()
        arrayLastName.append(lastName)

    # Ordena el array de apellidos
    arrayLastName.sort()

    # Ciclo que busca incidencias con el apellido guardando en orden los usuarios, tambien valida que no se repitan los usuarios.
    for lastName in arrayLastName:
        for idUser, userData in enumerate(arrayData):
           if arrayData[idUser].get("Apellidos").lower() == lastName:
               if userData not in arrayMatchSearchSort:
                   arrayMatchSearchSort.append(userData)

    #Ciclo que estructura los mapas con las incidencias buscadas de cada filtro.
    for idUser, userData in enumerate(arrayMatchSearchSort):
        if userData[filterType] == search:
            controler = idUser
            
            typeDoc = arrayMatchSearchSort[controler].get("Tipo Documento")
            numDoc = arrayMatchSearchSort[controler].get("Numero Documento") 
            name = arrayMatchSearchSort[controler].get("Nombres")
            lastName = arrayMatchSearchSort[controler].get("Apellidos")
            rh = arrayMatchSearchSort[controler].get("RH")
            email = arrayMatchSearchSort[controler].get("Correo")
            phoneNumber = arrayMatchSearchSort[controler].get("Numero de telefono")
    
    
            searchResult = {
                                "Tipo Documento":typeDoc,
                                "Numero Documento":numDoc,
                                "Nombres y pellidos":name +" "+ lastName,
                                "RH":rh,
                                "Correo":email,
                                "Numero de telefono":phoneNumber
                            }

            arrayMatchSearch.append(searchResult)

    return arrayMatchSearch


def displayMatchSearch(arrayMatchSearch: list) -> str :

    """
    Función encargada de mostrar el resultado del filtro de los datos de los pacientes.

    Parameters
    ------------------
    arrayMatchSearch : list
        Listado de los pacientes (Usuarios).

    Returns
    ------------------
    array : str
        Retorna la estructura la informacion del usuario filtrado.
    """

    displayMatchSearchs = "\n======================================\n"
    displayMatchSearchs += "        RESULTADO DE LA BUSQUEDA      \n"
    displayMatchSearchs += "======================================\n"

    for cont,users in enumerate(arrayMatchSearch):
        displayMatchSearchs += f"\n           Resultado # {cont+1}       \n"
        displayMatchSearchs += "---------------------------------------\n"
        for user in users:
            displayMatchSearchs += f"{user} : {str(users[user])}\n"
        displayMatchSearchs += "---------------------------------------\n"

    return displayMatchSearchs