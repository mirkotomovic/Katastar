from bs4 import BeautifulSoup
import urllib3
import re


def getOpstinasIdName(soup):
    return {option["value"]: option.text for option in soup.find_all("option")}


def getOpstinasNameId(soup):
    return {option.text: option["value"] for option in soup.find_all("option")}


def getOpstinasId(soup):
    return [option["value"] for option in soup.find_all("option")]


def getOpstinasName(soup):
    return [option.text for option in soup.find_all("option")]


def getKatOpstinas(soup):
    table = (
        soup.find("table", {"id": "ContentPlaceHolder1_getOpstinaKO_GridView"})
        .find("tbody")
        .find_all("tr")
    )

    return {
        row.find("td", {"style": "width:100px;"}).get_text(): {
            "ImeKatOpstine": row.find("a", href=True).get_text(),
            "Id": row.find("td", {"style": "width:100px;"}).get_text(),
            "ImeOpštine": soup.find("option", selected=True).get_text(),
            "IdOpstine": soup.find("option", selected=True)["value"],
            "href": row.find("a", href=True).get("href"),
        }
        for row in table[1:]
    }


def saveCaptcha(url, name):
    with open("./captchas/" + name, "wb") as f:
        http = urllib3.PoolManager()
        response = http.request("GET", url, timeout=2)
        f.write(response.data)


# soup = BeautifulSoup(open("test.html"), "html.parser")

# Json object one
def getPodatciNepokretnosti(soup):
    return {
        "RefBr": soup.find("span", {"id": "propNepokretnost_lblNepRefBr"}).get_text(),
        "matBrOpstine": soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionOpstinaID_lblText"}
        ).get_text(),
        "nazivOpstine": soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionOpstinaNaziv_lblText"}
        ).get_text(),
        "matBrKatOpstine": soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionKoID_lblText"}
        ).get_text(),
        "nazivKatOpstine": soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionKONaziv_lblText"}
        ).get_text(),
        "datumAzuriranja": soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionDatumAzurnosti_lblText"},
        ).get_text(),
        "sluzba": soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionSluzba_lblText"}
        ).get_text(),
    }


def getAlist(soup):
    return {
        "Ulica": cleanString(
            soup.find(
                "span", {"id": "propParcela_ucLabelPermitionUlica_lblText"}
            ).get_text()
        ),
        "brParcele": soup.find(
            "span", {"id": "propParcela_ucLabelPermitionBrParc_lblText"}
        ).get_text(),
        "podBrParcele": soup.find(
            "span", {"id": "propParcela_ucLabelPermitionPodBrParc_lblText"}
        ).get_text(),
        "površina": soup.find(
            "span", {"id": "propParcela_ucLabelPermitionPovrsina_lblText"}
        ).get_text(),
        "brListaNepokretnosti": soup.find(
            "span", {"id": "propParcela_ucLabelPermitionBrojLN_lblText"}
        ).get_text(),
    }


def getPodatciDeluParcele(soup):
    return {
        "brDela": soup.find(
            "span", {"id": "propParcelaDeo_ucLabelPermitionBrDelaParc_lblText"}
        ).get_text(),
        "vrstaZemljista": cleanString(
            soup.find(
                "span", {"id": "propParcelaDeo_ucLabelPermitionVrstaZemljista_lblText"},
            ).get_text()
        ),
        "kultura": cleanString(
            soup.find(
                "span", {"id": "propParcelaDeo_ucLabelPermitionKultura_lblText"}
            ).get_text()
        ),
        "povrsinaDela": soup.find(
            "span", {"id": "propParcelaDeo_ucLabelPermitionPovrsina_lblText"}
        ).get_text(),
    }


def getB1List(soup):
    return {
        "brObjekta": soup.find(
            "span", {"id": "propObjekat_ucLabelPermitionBrDelaParc_lblText"}
        ).get_text(),
        "nazivUlice": cleanString(
            soup.find(
                "span", {"id": "propObjekat_ucLabelPermitionUlicaPotes_lblText"}
            ).get_text()
        ),
        "brKuce": soup.find(
            "span", {"id": "propObjekat_ucLabelPermitionKcBroj_lblText"}
        ).get_text(),
        "podBrKuce": soup.find(
            "span", {"id": "propObjekat_ucLabelPermitionKcPodBr_lblText"}
        ).get_text(),
        "povrsinaB1": soup.find(
            "span", {"id": "propObjekat_ucLabelPermitionPovrsina_lblText"}
        ).get_text(),
        "korisnaPovrsina": soup.find(
            "span", {"id": "propObjekat_ucLabelPermitionPovrsinaKorisna_lblText"}
        ).get_text(),
        "gradjPovrsina": soup.find(
            "span", {"id": "propObjekat_ucLabelPermitionPovrsinaGradjevinska_lblText"},
        ).get_text(),
        "nacinKoriscenja": cleanString(
            soup.find(
                "span", {"id": "propObjekat_ucLabelPermitionObjekatKoriscenje_lblText"},
            ).get_text()
        ),
        "pravniStatus": cleanString(
            soup.find(
                "span", {"id": "propObjekat_ucLabelPermitionObjekatStatus_lblText"}
            ).get_text()
        ),
    }


def getB2List(soup):
    return {
        "brObjekta": soup.find(
            "span", {"id": "propObjekatDeo_ucLabelPermitionBrDelaParc_lblText"}
        ).get_text(),
        "nazivUlice": cleanString(
            soup.find(
                "span", {"id": "propObjekatDeo_ucLabelPermitionUlicaPotes_lblText"}
            ).get_text()
        ),
        "brUlaza": soup.find(
            "span", {"id": "propObjekatDeo_ucLabelPermitionBrUlaza_lblText"}
        ).get_text(),
        "brEvid": soup.find(
            "span", {"id": "propObjekatDeo_ucLabelPermitionEvidBroj_lblText"}
        ).get_text(),
        "nacinKoriscenja": cleanString(
            soup.find(
                "span",
                {"id": "propObjekatDeo_ucLabelPermitionObjekatDeoKoriscenje_lblText"},
            ).get_text()
        ),
        "brPosebnogDela": soup.find(
            "span", {"id": "propObjekatDeo_ucLabelPermitionBrojStana_lblText"}
        ).get_text(),
        "podBrPosebnogDela": soup.find(
            "span", {"id": "propObjekatDeo_ucLabelPermitionPbrStana_lblText"}
        ).get_text(),
        "gradjPovrsinaB2": soup.find(
            "span",
            {
                "id": "propObjekatDeo_ucLabelPermitionObjekatDeoPovrsinaGradjevinska_lblText"
            },
        ).get_text(),
        "korisnaPovrsinaB2": soup.find(
            "span",
            {"id": "propObjekatDeo_ucLabelPermitionObjekatDeoPovrsinaKorisna_lblText"},
        ).get_text(),
        "nacinUtvridjivanjaKorisnePovrsine": cleanString(
            soup.find(
                "span", {"id": "propObjekatDeo_ucLabelPermitionPovrsinaNacUtv_lblText"},
            ).get_text()
        ),
        "opis": cleanString(
            soup.find(
                "span", {"id": "propObjekatDeo_ucLabelPermitionObjekatDeoOpis_lblText"},
            ).get_text()
        ),
    }


def getImaoceParcele(soup):
    imaoci = []
    data = [
        cleanString(x.find_next("td").get_text())
        for x in soup.find("span", {"id": "getNosiociPravaNaParceli_lblCaption"})
        .find_next("table")
        .find_all(["b", "strong"])
    ]
    for i in range(len(data) // 4):
        imaoci.append(
            {
                "naziv": data[4 * i],
                "vrstaPrava": data[4 * i + 1],
                "oplikSvojine": data[4 * i + 2],
                "udeo": data[4 * i + 3],
            }
        )
    return imaoci


def getTeretParcele(soup):
    teretParcele = []
    if soup.find("span", {"id": "getTeretiNaParceli_lbInfo"}):
        teretParcele = "NEMA"
    else:
        data = [
            cleanString(x.find_next("td").get_text())
            for x in soup.find("span", {"id": "getTeretiNaParceli_lblCaption"})
            .find_next("table")
            .find_all(["b", "strong"])
        ]
        for i in range(len(data) // 6):
            teretParcele.append(
                {
                    "brTereta": data[6 * i],
                    "vrstaTereta": data[6 * i + 1],
                    "datumUpisa": data[6 * i + 2],
                    "trajanjeTereta": data[6 * i + 3],
                    "datumPrestanka": data[6 * i + 4],
                    "opisTereta": data[6 * i + 5],
                }
            )
    return teretParcele


def getZabelezbaParcele(soup):
    zabelezbaParcele = []
    if soup.find("span", {"id": "getNapomenaNaParceli_lbInfo"}):
        zabelezbaParcele = "NEMA"
    else:
        data = [
            cleanString(x.find_next("td").get_text())
            for x in soup.find("span", {"id": "getNapomenaNaParceli_lblCaption"})
            .find_next("table")
            .find_all(["b", "strong"])
        ]
        for i in range(len(data) // 3):
            zabelezbaParcele.append(
                {
                    "datum": data[3 * i],
                    "brPredmeta": data[3 * i + 1],
                    "opis": data[3 * i + 2],
                }
            )
    return zabelezbaParcele


def getImaoceObjekta(soup):
    imaoci = []
    data = [
        cleanString(x.find_next("td").get_text())
        for x in soup.find("span", {"id": "getNosiociPravaNaObjektu_lblCaption"})
        .find_next("table")
        .find_all(["b", "strong"])
    ]
    for i in range(len(data) // 4):
        imaoci.append(
            {
                "naziv": data[4 * i],
                "vrstaPrava": data[4 * i + 1],
                "oplikSvojine": data[4 * i + 2],
                "udeo": data[4 * i + 3],
            }
        )
    return imaoci


def getTeretObjekta(soup):
    teretObjekta = []
    if soup.find("span", {"id": "getTeretiNaObjetu_lbInfo"}):
        teretObjekta = "NEMA"
    else:
        data = [
            cleanString(x.find_next("td").get_text())
            for x in soup.find("span", {"id": "getTeretiNaObjetu_lblCaption"})
            .find_next("table")
            .find_all(["b", "strong"])
        ]
        for i in range(len(data) // 6):
            teretObjekta.append(
                {
                    "brTereta": data[6 * i],
                    "vrstaTereta": data[6 * i + 1],
                    "datumUpisa": data[6 * i + 2],
                    "trajanjeTereta": data[6 * i + 3],
                    "datumPrestanka": data[6 * i + 4],
                    "opisTereta": data[6 * i + 5],
                }
            )
    return teretObjekta


def getZabelezbaObjekta(soup):
    zabelezbaObjekta = []
    if soup.find("span", {"id": "getNapomenaNaObjektu_lbInfo"}):
        zabelezbaObjekta = "NEMA"
    else:
        data = [
            cleanString(x.find_next("td").get_text())
            for x in soup.find("span", {"id": "getNapomenaNaObjektu_lblCaption"})
            .find_next("table")
            .find_all(["b", "strong"])
        ]
        for i in range(len(data) // 3):
            zabelezbaObjekta.append(
                {
                    "datum": data[3 * i],
                    "brPredmeta": data[3 * i + 1],
                    "opis": data[3 * i + 2],
                }
            )
    return zabelezbaObjekta


def getImaocePodObjekta(soup):
    imaoci = []
    data = [
        cleanString(x.find_next("td").get_text())
        for x in soup.find("span", {"id": "getNosiociPravaNaPosebnomDelu_lblCaption"})
        .find_next("table")
        .find_all(["b", "strong"])
    ]
    for i in range(len(data) // 4):
        imaoci.append(
            {
                "naziv": data[4 * i],
                "vrstaPrava": data[4 * i + 1],
                "oplikSvojine": data[4 * i + 2],
                "udeo": data[4 * i + 3],
            }
        )
    return imaoci


def getTeretPodObjekta(soup):
    teretPodObjekta = []
    if soup.find("span", {"id": "getTeretiNaPosebnomDelu_lbInfo"}):
        teretPodObjekta = "NEMA"
    else:
        data = [
            cleanString(x.find_next("td").get_text())
            for x in soup.find("span", {"id": "getTeretiNaPosebnomDelu_lblCaption"})
            .find_next("table")
            .find_all(["b", "strong"])
        ]
        for i in range(len(data) // 6):
            teretPodObjekta.append(
                {
                    "brTereta": data[6 * i],
                    "vrstaTereta": data[6 * i + 1],
                    "datumUpisa": data[6 * i + 2],
                    "trajanjeTereta": data[6 * i + 3],
                    "datumPrestanka": data[6 * i + 4],
                    "opisTereta": data[6 * i + 5],
                }
            )
    return teretPodObjekta


def getZabelezbaPodObjekta(soup):
    zabelezbaPodObjekta = []
    if soup.find("span", {"id": "getNapomenaNaPosebnomDelu_lbInfo"}):
        zabelezbaPodObjekta = "NEMA"
    else:
        data = [
            cleanString(x.find_next("td").get_text())
            for x in soup.find("span", {"id": "getNapomenaNaPosebnomDelu_lblCaption"})
            .find_next("table")
            .find_all(["b", "strong"])
        ]
        for i in range(len(data) // 3):
            zabelezbaPodObjekta.append(
                {
                    "datum": data[3 * i],
                    "brPredmeta": data[3 * i + 1],
                    "opis": data[3 * i + 2],
                }
            )
    return zabelezbaPodObjekta


def getAllData(soup):
    id = (
        soup.find(
            "span", {"id": "propNepokretnost_ucLabelPermitionKoID_lblText"}
        ).get_text()
        + "_"
        + soup.find(
            "span", {"id": "propParcela_ucLabelPermitionBrParc_lblText"}
        ).get_text()
        + "_"
        + soup.find(
            "span", {"id": "propParcela_ucLabelPermitionPodBrParc_lblText"}
        ).get_text()
        + "_"
        + soup.find(
            "span", {"id": "propParcelaDeo_ucLabelPermitionBrDelaParc_lblText"}
        ).get_text()
    )

    nepoktetnost = {
        "nepokretnost": getPodatciNepokretnosti(soup),
        "alist": getAlist(soup),
        "deoParcele": getPodatciDeluParcele(soup),
        "imaociParcele": getImaoceParcele(soup),
        "teretParcele": getTeretParcele(soup),
    }

    if soup.find("td", text=re.compile(".*В1.*"), attrs={"class": "print_form_item_h"}):
        id += (
            "_"
            + soup.find(
                "span", {"id": "propObjekat_ucLabelPermitionBrDelaParc_lblText"}
            ).get_text()
        )
        nepoktetnost.update(
            {
                "B1List": getB1List(soup),
                "imaociObjekta": getImaoceObjekta(soup),
                "teretObjekta": getTeretObjekta(soup),
                "zabelezbaObjekta": getZabelezbaObjekta(soup),
            }
        )

    if soup.find("td", text=re.compile(".*В2.*"), attrs={"class": "print_form_item_h"}):
        id += (
            "_"
            + soup.find(
                "span", {"id": "propObjekatDeo_ucLabelPermitionBrojStana_lblText"}
            ).get_text()
        )
        nepoktetnost.update(
            {
                "B2List": getB2List(soup),
                "imaociPodObjekta": getImaocePodObjekta(soup),
                "teretPodObjekta": getTeretPodObjekta(soup),
                "zabelezbaPodObjekta": getZabelezbaPodObjekta(soup),
            }
        )

    return {id: nepoktetnost}


def stripLinks(soup):
    baseUrl = "katastar.rgz.gov.rs/eKatastarPublic/"
    setUrl = set()
    if soup.find("table", {"id": "ContentPlaceHolder1_GridView1"}):
        setUrl.update(
            [
                baseUrl + x["href"].split("'")[1]
                for x in soup.find(
                    "table", {"id": "ContentPlaceHolder1_GridView1"}
                ).find_all("a")
                if "nepID" in str(x)
            ]
        )
    if soup.find("table", {"id": "ContentPlaceHolder1_GridView2"}):
        setUrl.update(
            [
                baseUrl + x["href"].split("'")[1]
                for x in soup.find(
                    "table", {"id": "ContentPlaceHolder1_GridView2"}
                ).find_all("a")
                if "nepID" in str(x)
            ]
        )
    if soup.find("table", {"id": "ContentPlaceHolder1_GridView3"}):
        setUrl.update(
            [
                baseUrl + x["href"].split("'")[1]
                for x in soup.find(
                    "table", {"id": "ContentPlaceHolder1_GridView3"}
                ).find_all("a")
                if "nepID" in str(x)
            ]
        )
    return setUrl, len(setUrl)


# Helpers
def cleanString(str):
    return " ".join(str.split())

