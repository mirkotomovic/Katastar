import mysql.connector

from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):

    connection = None

    try:
        connection = mysql.connector.connect(
            host=host_name, user=user_name, passwd=user_password, database=db_name
        )
        print("Connection to MariaDB DB successful")

    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(connection, query):

    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()

    except Error as e:
        print(f"The error '{e}' occurred")


def insert_query(connection, query, vals):

    cursor = connection.cursor()

    try:
        cursor.executemany(query, vals)
        connection.commit()

    except Error as e:
        print(f"The error '{e}' occurred")


def select_query(connection, query):

    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except Error as e:
        print(f"The error '{e}' occurred")


def insertData(listing, conn):
    for key in listing.keys():
        if type(listing[key]) is list:
            if key == "imaociParcele":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO imaociParcele(naziv, vrstaPrava, oplikSvojine, udeo, id_lista) VALUES('"
                        + imaoc["naziv"]
                        + "','"
                        + imaoc["vrstaPrava"]
                        + "','"
                        + imaoc["oplikSvojine"]
                        + "','"
                        + imaoc["udeo"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "imaociObjekta":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO imaociObjekta(naziv, vrstaPrava, oplikSvojine, udeo, id_lista) VALUES('"
                        + imaoc["naziv"]
                        + "','"
                        + imaoc["vrstaPrava"]
                        + "','"
                        + imaoc["oplikSvojine"]
                        + "','"
                        + imaoc["udeo"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "imaociPodObjekta":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO imaociPodObjekta(naziv, vrstaPrava, oplikSvojine, udeo, id_lista) VALUES('"
                        + imaoc["naziv"]
                        + "','"
                        + imaoc["vrstaPrava"]
                        + "','"
                        + imaoc["oplikSvojine"]
                        + "','"
                        + imaoc["udeo"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "teretParcele":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO teretParcele(brTereta, vrstaTereta, datumUpisa, trajanjeTereta, datumPrestanka, opisTereta, id_lista) VALUES('"
                        + imaoc["brTereta"]
                        + "', '"
                        + imaoc["vrstaTereta"]
                        + "', '"
                        + imaoc["datumUpisa"]
                        + "', '"
                        + imaoc["trajanjeTereta"]
                        + "', '"
                        + imaoc["datumPrestanka"]
                        + "', '"
                        + imaoc["opisTereta"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "teretObjekta":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO teretObjekta(brTereta, vrstaTereta, datumUpisa, trajanjeTereta, datumPrestanka, opisTereta, id_lista) VALUES('"
                        + imaoc["brTereta"]
                        + "', '"
                        + imaoc["vrstaTereta"]
                        + "', '"
                        + imaoc["datumUpisa"]
                        + "', '"
                        + imaoc["trajanjeTereta"]
                        + "', '"
                        + imaoc["datumPrestanka"]
                        + "', '"
                        + imaoc["opisTereta"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "teretPodObjekta":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO teretPodObjekta(brTereta, vrstaTereta, datumUpisa, trajanjeTereta, datumPrestanka, opisTereta, id_lista) VALUES('"
                        + imaoc["brTereta"]
                        + "', '"
                        + imaoc["vrstaTereta"]
                        + "', '"
                        + imaoc["datumUpisa"]
                        + "', '"
                        + imaoc["trajanjeTereta"]
                        + "', '"
                        + imaoc["datumPrestanka"]
                        + "', '"
                        + imaoc["opisTereta"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "zabelezbaParcele":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO zabelezbaParcele(datum, brPredmeta, opis, id_lista) VALUES('"
                        + imaoc["datum"]
                        + "','"
                        + imaoc["brPredmeta"]
                        + "','"
                        + imaoc["opis"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "zabelezbaObjekta":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO zabelezbaObjekta(datum, brPredmeta, opis, id_lista) VALUES('"
                        + imaoc["datum"]
                        + "','"
                        + imaoc["brPredmeta"]
                        + "','"
                        + imaoc["opis"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

            if key == "zabelezbaPodObjekta":
                for imaoc in listing[key]:
                    query_insert = (
                        "INSERT INTO zabelezbaPodObjekta(datum, brPredmeta, opis, id_lista) VALUES('"
                        + imaoc["datum"]
                        + "','"
                        + imaoc["brPredmeta"]
                        + "','"
                        + imaoc["opis"]
                        + "','"
                        + listing["id"]
                        + "' );"
                    )
                    execute_query(conn, query_insert)

        if type(listing[key]) is dict:
            if key == "nepokretnost":
                query_insert = (
                    "INSERT INTO nepokretnost(RefBr, matBrOpstine, nazivOpstine, matBrKatOpstine, nazivKatOpstine, datumAzuriranja, sluzba, id_lista) VALUES('"
                    + listing[key]["RefBr"]
                    + "','"
                    + listing[key]["matBrOpstine"]
                    + "','"
                    + listing[key]["nazivOpstine"]
                    + "','"
                    + listing[key]["matBrKatOpstine"]
                    + "','"
                    + listing[key]["nazivKatOpstine"]
                    + "','"
                    + listing[key]["datumAzuriranja"]
                    + "','"
                    + listing[key]["sluzba"]
                    + "','"
                    + listing["id"]
                    + "' );"
                )
                execute_query(conn, query_insert)

            if key == "alist":
                query_insert = (
                    "INSERT INTO alist(Ulica, brParcele, podBrParcele, površina, brListaNepokretnosti, id_lista) VALUES('"
                    + listing[key]["Ulica"]
                    + "','"
                    + listing[key]["brParcele"]
                    + "','"
                    + listing[key]["podBrParcele"]
                    + "','"
                    + listing[key]["površina"]
                    + "','"
                    + listing[key]["brListaNepokretnosti"]
                    + "','"
                    + listing["id"]
                    + "' );"
                )
                execute_query(conn, query_insert)

            if key == "deoParcele":
                query_insert = (
                    "INSERT INTO deoParcele(brDela, vrstaZemljista, kultura, povrsinaDela, id_lista) VALUES('"
                    + listing[key]["brDela"]
                    + "','"
                    + listing[key]["vrstaZemljista"]
                    + "','"
                    + listing[key]["kultura"]
                    + "','"
                    + listing[key]["povrsinaDela"]
                    + "','"
                    + listing["id"]
                    + "' );"
                )
                execute_query(conn, query_insert)

            if key == "B1List":
                query_insert = (
                    "INSERT INTO B1List(brObjekta, nazivUlice, brKuce, podBrKuce, povrsinaB1, korisnaPovrsina, gradjPovrsina, nacinKoriscenja, pravniStatus, id_lista) VALUES('"
                    + listing[key]["brObjekta"]
                    + "','"
                    + listing[key]["nazivUlice"]
                    + "','"
                    + listing[key]["brKuce"]
                    + "','"
                    + listing[key]["podBrKuce"]
                    + "','"
                    + listing[key]["povrsinaB1"]
                    + "','"
                    + listing[key]["korisnaPovrsina"]
                    + "','"
                    + listing[key]["gradjPovrsina"]
                    + "','"
                    + listing[key]["nacinKoriscenja"]
                    + "','"
                    + listing[key]["pravniStatus"]
                    + "','"
                    + listing["id"]
                    + "' );"
                )
                execute_query(conn, query_insert)

            if key == "B2List":
                query_insert = (
                    "INSERT INTO B2List(brObjekta_B2List, nazivUlice_B2List, brUlaza_B2List, brEvid_B2List, nacinKoriscenja_B2List, brPosebnogDela_B2List, podBrPosebnogDela_B2List, gradjPovrsinaB2_B2List, korisnaPovrsinaB2_B2List, nacinUtvridjivanjaKorisnePovrsine_B2List, opis_B2List, id_lista) VALUES('"
                    + listing[key]["brObjekta"]
                    + "','"
                    + listing[key]["nazivUlice"]
                    + "','"
                    + listing[key]["brUlaza"]
                    + "','"
                    + listing[key]["brEvid"]
                    + "','"
                    + listing[key]["nacinKoriscenja"]
                    + "','"
                    + listing[key]["brPosebnogDela"]
                    + "','"
                    + listing[key]["podBrPosebnogDela"]
                    + "','"
                    + listing[key]["gradjPovrsinaB2"]
                    + "','"
                    + listing[key]["korisnaPovrsinaB2"]
                    + "','"
                    + listing[key]["nacinUtvridjivanjaKorisnePovrsine"]
                    + "','"
                    + listing[key]["opis"]
                    + "','"
                    + listing["id"]
                    + "' );"
                )
                execute_query(conn, query_insert)


def getParceleDataByNaziv(naziv, conn):
    query = """ 
            SELECT DISTINCT
                id_lista,
                imaociParcele.naziv AS naziv,

                nepokretnost.nazivOpstine AS opstina,
                nepokretnost.nazivKatOpstine AS katastarska_opstina,

                alist.Ulica AS ulica,
                alist.brParcele AS broj_parcele,
                alist.brListaNepokretnosti AS br_lista_nepokretnosti,

                deoParcele.vrstaZemljista AS vrsta_zemljista,
                deoParcele.kultura AS kultura,
                
                teretParcele.vrstaTereta AS vrsta_tereta,
                teretParcele.datumUpisa AS datum_upisa,
                teretParcele.datumPrestanka AS datum_prestanka,

                zabelezbaParcele.opis AS opis_zabelezbe,
                zabelezbaParcele.datum AS datum_zabelezbe
            FROM `nepokretnost`
            LEFT JOIN `alist` USING (id_lista)
            LEFT JOIN `deoParcele` USING (id_lista)
            RIGHT JOIN `imaociParcele` USING (id_lista)
            LEFT JOIN `zabelezbaParcele` USING (id_lista)
            LEFT JOIN `teretParcele` USING (id_lista)
            WHERE naziv LIKE '%{0}%'
            ORDER BY id_lista;
        """.format(
        naziv.upper()
    )
    return select_query(conn, query)


def getObjekatDataByNaziv(naziv, conn):
    query = """ 
            SELECT DISTINCT
                id_lista,
                imaociObjekta.naziv AS naziv_po,
                
                nepokretnost.nazivOpstine AS opstina,
                nepokretnost.nazivKatOpstine AS katastarska_opstina,

                alist.Ulica AS ulica,
                alist.brParcele AS broj_parcele,
                alist.brListaNepokretnosti AS br_lista_nepokretnosti,

                deoParcele.vrstaZemljista AS vrsta_zemljista,
                deoParcele.kultura AS kultura,

                B1List.nacinKoriscenja AS nacin_koriscenja,
                B1List.pravniStatus AS pravni_status,

                teretObjekta.vrstaTereta AS vrsta_tereta,
                teretObjekta.datumUpisa AS datum_upisa,
                teretObjekta.datumPrestanka AS datum_prestanka,

                zabelezbaObjekta.opis AS opis_zabelezbe,
                zabelezbaObjekta.datum AS datum_zabelezbe
            FROM nepokretnost
            LEFT JOIN alist USING (id_lista)
            LEFT JOIN deoParcele USING (id_lista)
            LEFT JOIN B1List USING (id_lista)
            RIGHT JOIN imaociObjekta USING (id_lista)
            LEFT JOIN zabelezbaObjekta USING (id_lista)
            LEFT JOIN teretObjekta USING (id_lista)
            WHERE naziv LIKE '%{0}%'
            ORDER BY id_lista;
        """.format(
        naziv.upper()
    )
    return select_query(conn, query)


def getPodObjekatDataByNaziv(naziv, conn):
    query = """ 
            SELECT DISTINCT
                id_lista,
                imaociPodObjekta.naziv AS naziv_po,

                nepokretnost.nazivOpstine AS opstina,
                nepokretnost.nazivKatOpstine AS katastarska_opstina,

                alist.Ulica AS ulica,
                alist.brParcele AS broj_parcele,
                alist.brListaNepokretnosti AS br_lista_nepokretnosti,

                deoParcele.vrstaZemljista AS vrsta_zemljista,
                deoParcele.kultura AS kultura,

                B1List.nacinKoriscenja AS nacin_koriscenja,
                B1List.pravniStatus AS pravni_status,

                B2List.nacinKoriscenja_B2List AS nacin_koriscenja_b2,
                B2List.opis_B2List AS opis_objekta,

                teretPodObjekta.vrstaTereta AS vrsta_tereta,
                teretPodObjekta.datumUpisa AS datum_upisa,
                teretPodObjekta.datumPrestanka AS datum_prestanka,

                zabelezbaPodObjekta.opis AS opis_zabelezbe,
                zabelezbaPodObjekta.datum AS datum_zabelezbe
            FROM
                nepokretnost
            LEFT JOIN alist USING (id_lista)
            LEFT JOIN deoParcele USING (id_lista)
            LEFT JOIN B1List USING (id_lista)
            LEFT JOIN B2List USING (id_lista)
            RIGHT JOIN imaociPodObjekta USING (id_lista)
            LEFT JOIN zabelezbaPodObjekta USING (id_lista)
            LEFT JOIN teretPodObjekta USING (id_lista)
            WHERE naziv LIKE '%{0}%'
            ORDER BY id_lista;
        """.format(
        naziv.upper()
    )
    return select_query(conn, query)


def getIdsByNaziv(naziv, conn):
    query = """
            SELECT 
                id_lista,
                naziv
            FROM
            (
                SELECT  naziv, vrstaPrava, oplikSvojine, udeo, id_lista 
                FROM    imaociParcele
                UNION   
                SELECT  naziv, vrstaPrava, oplikSvojine, udeo, id_lista
                FROM    imaociObjekta            
                UNION   
                SELECT  naziv, vrstaPrava, oplikSvojine, udeo, id_lista
                FROM    imaociPodObjekta
            ) subquery
            WHERE naziv LIKE '%{0}%'
            ORDER BY id_lista;
            """.format(
        naziv
    )
    return [
        i[0] for i in select_query(conn, query)
    ]  # [[i[0] for t in select_query(conn, query) for i in t], [i[1] for t in select_query(conn, query) for i in t]]


def getNazivById(id, conn):
    query = """
            SELECT  naziv 
            FROM    imaociParcele
            WHERE id_lista LIKE '{0}'
            ORDER BY id_lista;
            """.format(
        id
    )
    return [i for t in select_query(conn, query) for i in t]


def getTeretId(id, conn):
    query = """
            SELECT  
                id_lista,
                brTereta,
                vrstaTereta,
                datumUpisa,
                trajanjeTereta,
                datumPrestanka,
                opisTereta
            FROM
            (
                SELECT  
                    id_lista,
                    brTereta,
                    vrstaTereta,
                    datumUpisa,
                    trajanjeTereta,
                    datumPrestanka,
                    opisTereta
                FROM    
                    teretParcele
                UNION   
                SELECT  
                    id_lista,
                    brTereta,
                    vrstaTereta,
                    datumUpisa,
                    trajanjeTereta,
                    datumPrestanka,
                    opisTereta
                FROM    
                    teretObjekta            
                UNION 
                SELECT
                    id_lista,
                    brTereta,
                    vrstaTereta,
                    datumUpisa,
                    trajanjeTereta,
                    datumPrestanka,
                    opisTereta
                FROM
                    teretPodObjekta
            ) subquery
            WHERE id_lista LIKE '{0}'
            ORDER BY id_lista;
            """.format(
        id
    )
    return [t for t in select_query(conn, query)]


def getZabelezbaId(id, conn):
    query = """
            SELECT  
                id_lista,
                datum,
                brPredmeta,
                opis
            FROM
            (
                SELECT  
                    id_lista,
                    datum,
                    brPredmeta,
                    opis
                FROM    
                    zabelezbaParcele
                UNION   
                SELECT  
                    id_lista,
                    datum,
                    brPredmeta,
                    opis
                FROM    
                    zabelezbaObjekta            
                UNION 
                SELECT
                    id_lista,
                    datum,
                    brPredmeta,
                    opis
                FROM
                    zabelezbaPodObjekta
            ) subquery
            WHERE id_lista LIKE '{0}'
            ORDER BY id_lista;
            """.format(
        id
    )
    return [t for t in select_query(conn, query)]


# for i in getIdsByNaziv('УТВРЂЕН', conn):
# for j in getZabelezbaId(i, conn):
# print(j)
# print(i)
# print()
# print()

# import json
# with open('./data/test.json') as json_file:
#     data = json.load(json_file)
#     for i in data.values():
#         insertData(i, conn)
