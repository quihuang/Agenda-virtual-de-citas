import os
import utilidades as util

patchFilePacientes ="D:/Frank´s User Data/OneDrive/Documentos/Universidad de Caldas/Fundamentos de Programacion/Algoritmos Python/RETO #6/archivos/pacientes.txt"
patchFileCitas = "D:/Frank´s User Data/OneDrive/Documentos/Universidad de Caldas/Fundamentos de Programacion/Algoritmos Python/RETO #6/archivos/citas.txt"

messageExit = "\nSaliendo del programa..."
messageDataInvalid = "\nEl valor ingresado no es valido."
messageOptionInvalid = "\nLa opción ingresada no es valida."
messageNameInvalid = "\nEl nombre ingresado es invalido.No debe contener numeros o sobre pasar los 30 caracteres."
messageLastNameInvalid = "\nEl apellido ingresado es invalido.No debe contener numeros o sobre pasar los 30 caracteres."
messageUserNotExist = "\nEl usuario ingresado no se encuentra registrado en el sistema."
messageUserRegister = "\nEl usuario se a registrado correctamente."
messageUserExist = "\nEl usuario ya se encuentra registrado en el sistema."
messageDateInvalid = "\nLa fecha no puede ser inferior a la actual."
messageUploadSuccess = "\nEl archivo se a cargado con Exito."
messageUploadFailure = "\nError: El archivo no contiene registros"
messageNotMatch = "\nNo se encontraron valores en la busqueda"
messageFileNotFount = "\nEL archivo que estas intentado cargar no existe"

option = ""
dbUsers = []
dbDataAsig = []


while option !="7":

    print("\n================================================")
    print(" Bienvenido al software de Agendamiento virtual ")
    print("================================================")
    print("1. Registrarse.")
    print("2. Asignar una cita.")
    print("3. Visualizar citas agendadas.")
    print("4. Visualizar usuarios registrados")
    print("5. Cargar Achivos.")
    print("6. busqueda.")
    print("7. Salir.")
    print("================================================")

    option = input("\nPorfavor ingrese una opción : ")

    if(option == "1"):
        os.system("clear")

        print("\nDiligencie el siguiente formulario para el registro del usuario : ")

        typeDoc = "INVALID"
        numberDoc = False
        name = False
        lastName = False
        birthDate = False
        typeBlood = False
        email = False
        numerPhone = False
        validateDoc = True

        while typeDoc == "INVALID":

            typeDocument = input("\nTipo de documento: \n\n1. CC \n2. CE \n3. TI \n4. PA \n\nIngrese una opción : \n» ")
            typeDoc = util.validateTypeDocument(typeDocument)

            if(typeDoc == "INVALID"):
                os.system("clear")
                print(messageOptionInvalid)

        while numberDoc != True :

            numberDocuments = input("\nIngrese su numero de documento (solo se permiten números, sin puntos ni comas) : \n» ")
            numberDoc = util.validateDocumentNumber(numberDocuments)

            if(numberDoc == False):
                os.system("clear")
                print(messageDataInvalid)

            while validateDoc == True :

                validateDoc = util.validateExistUser(numberDocuments,dbUsers)

                if(validateDoc == True):
                    os.system("clear")
                    print(messageUserExist)
                    validateDoc = False
                    numberDoc = False

            validateDoc = True

        while name != True:

            inputName = input("\nIngrese su nombre : \n» ")
            name = util.validateNameAndLastName(inputName)

            if(name == False):
                os.system("clear")
                print(messageNameInvalid)

        while lastName !=True:

            inputLastName = input("\nIngrese su apellido : \n» ")
            lastName = util.validateNameAndLastName(inputLastName)

            if(lastName == False):
                os.system("clear")
                print(messageLastNameInvalid)

        while birthDate != True:

            inputBirthDate = input("\nDigite su fecha de nacimiento en el formato AAAA-MM-DD: \n» ")
            birthDate = util.validateBirthDate(inputBirthDate)

            if(birthDate == False):
                os.system("clear")
                print(messageDataInvalid)

        while typeBlood != True:

            inputBloodType =  input("\nDigite su tipo de sangre (O+, O-, A-, A+, B-, B+) : \n» ").upper()
            typeBlood = util.validateBloodType(inputBloodType)

            if(typeBlood == False):
                os.system("clear")
                print(messageDataInvalid)

        while email != True:

            inputEmail = input("\nIngrese su correo electronico : \n» ")
            email = util.validateEmail(inputEmail)

            if(email == False):
                os.system("clear")
                print(messageDataInvalid)

        while numerPhone != True:

            inputPhoneNumber = input("\nIngrese su numero de telefono : \n» ")
            numerPhone = util.validatePhoneNumber(inputPhoneNumber)

            if(numerPhone == False):
                os.system("clear")
                print(messageDataInvalid)

        os.system("clear")


        util.inputUserDatabase(typeDoc,numberDocuments,inputName,inputLastName,inputBirthDate,inputBloodType,inputEmail,inputPhoneNumber,dbUsers) 
        
        print(f"\nEl usuario {inputName} {inputLastName} con Identificacion {typeDoc} {numberDocuments} ha sido registro Exitosamente!")

    elif(option == "2"):
        os.system("clear")
        
        validateDoc = False
        numberDoc = False
        date = False
        validDataCurrent = False
        
        while numberDoc != True :

            numberDocuments = input("\nIngrese el numero de documento solo se permiten números, sin puntos ni comas: \n» ")
            numberDoc = util.validateDocumentNumber(numberDocuments)

            if(numberDoc == False):
                os.system("clear")
                print(messageDataInvalid)
                validateDoc = True

            while validateDoc == False :

                validateDoc = util.validateExistUser(numberDocuments,dbUsers)

                if(validateDoc == False):
                    os.system("clear")
                    print(messageUserNotExist)
                    validateDoc = True
                    numberDoc = False

            validateDoc = False

        while date != True:
            inputDate = input("\nDigite la fecha de la cita AAAA-MM-DD HH:MM : \n» ")
            date = util.validateDate(inputDate)

            if(date == False):
                os.system("clear")
                print(messageDataInvalid)
                validDataCurrent = True
        
            while validDataCurrent != True :

                validDataCurrent = util.validarteDateCurrent(inputDate)

                if(validDataCurrent == False):
                    os.system("clear")
                    print(messageDateInvalid)
                    validDataCurrent = True
                    date = False

            validDataCurrent = False

        messageConfirm = util.createDataAppointment(numberDocuments,inputDate,dbUsers,dbDataAsig)

        print(messageConfirm)
    elif(option == "3"):
        os.system("clear")
        
        displayAppointments = util.displayAppointment(dbDataAsig)

        print(displayAppointments)

    elif(option == "4"):
        os.system("clear")
        
        displayUsersRegister = util.displayUsersRegisters(dbUsers)

        print(displayUsersRegister)
    elif(option == "5"):
        os.system("clear")
        load = ""
        while load != "3":
            print("\n======================================================================")
            print("                          CARGAR ARCHIVOS                              ")
            print("=======================================================================")
            print("1. Cargar el archivo llamado pacientes.txt en la lista de pacientes.")
            print("2. Cargar el archivo llamado citas.txt en la lista de citas.")
            print("3. Salir.")
            print("================================================")

            load = input("\nPorfavor ingrese una opción : ")

            if(load == "1"): 
                if os.path.exists(patchFilePacientes):
                    dbUsers = util.loadsFiles(dbUsers,"pacientes")

                    if(len(dbUsers) > 0):
                        os.system("clear")
                        print(messageUploadSuccess)
                    else:
                        os.system("clear")
                        print(messageUploadFailure)
                else:
                    os.system("clear")
                    print(messageFileNotFount)
            elif(load == "2"):
                if os.path.exists(patchFileCitas):
                    dbDataAsig = util.loadsFiles(dbDataAsig,"citas")
                    if(len(dbDataAsig) > 0):
                        os.system("clear")
                        print(messageUploadSuccess)
                    else:
                        os.system("clear")
                        print(messageUploadFailure)
                else:
                    os.system("clear")
                    print(messageFileNotFount)
            elif(load == "3"):
                os.system("clear")
            else:
                os.system("clear")
                print(messageOptionInvalid)
          
    elif(option== "6"):
        os.system("clear")
        searchs = ""
        while searchs != "7":
            print("\n================================================")
            print("                FILTROS DE BUSQUEDA              ")
            print("=================================================")
            print("1. Buscar por nombre.")
            print("2. Buscar por apellido.")
            print("3. Buscar por RH.")
            print("4. Buscar por documento")
            print("5. Buscar por correo electrónico.")
            print("6. Buscar por teléfono.")
            print("7. Salir.")
            print("================================================")

            searchs = input("\nPorfavor ingrese una opción : ")

            if(searchs == "1"):

                name = input("Ingrese el nombre : \n» ")

                search = util.filterSearch("Nombres",name,dbUsers)

                if(len(search) > 0):
                    os.system("clear")
                    print(util.displayMatchSearch(search))
                else:
                    os.system("clear")
                    print(messageNotMatch)

            elif(searchs == "2"):
                
                name = input("Ingrese el apellido : \n» ")

                search = util.filterSearch("Apellidos",name,dbUsers)

                if(len(search) > 0):
                    os.system("clear")
                    print(util.displayMatchSearch(search))
                else:
                    os.system("clear")
                    print(messageNotMatch)

            elif(searchs == "3"):
                 
                name = input("Ingrese el tipo de sangre (O+, O-, A-, A+, B-, B+) : \n» ").upper()

                search = util.filterSearch("RH",name,dbUsers)

                if(len(search) > 0):
                    os.system("clear")
                    print(util.displayMatchSearch(search))
                else:
                    os.system("clear")
                    print(messageNotMatch)

            elif(searchs == "4"):
                 
                name = input("Ingrese el numero Documento : \n» ")

                search = util.filterSearch("Numero Documento",name,dbUsers)

                if(len(search) > 0):
                    os.system("clear")
                    print(util.displayMatchSearch(search))
                else:
                    os.system("clear")
                    print(messageNotMatch)

            elif(searchs == "5"):
                 
                name = input("Ingrese el correo electronico: \n» ")

                search = util.filterSearch("Correo",name,dbUsers)

                if(len(search) > 0):
                    os.system("clear")
                    print(util.displayMatchSearch(search))
                else:
                    os.system("clear")
                    print(messageNotMatch)

            elif(searchs == "6"):
                 
                name = input("Ingrese el numero de telefono : \n» ")

                search = util.filterSearch("Numero de telefono",name,dbUsers)

                if(len(search) > 0):
                    os.system("clear")
                    print(util.displayMatchSearch(search))
                else:
                    os.system("clear")
                    print(messageNotMatch)

            elif(searchs == "7"):
                os.system("clear")
            else:
                os.system("clear")
                print(messageOptionInvalid)

    elif(option == "7"):
         os.system("clear")
         print(messageExit)
    else:
        os.system("clear")
        print(messageOptionInvalid)
