from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = FastAPI()

@app.get("/embrapa_producao/")
def extracao_producao_ano():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    df = pd.read_csv(url, delimiter=';', header=None, skiprows=1)

    # Renomear as colunas
    df.columns = ["id",
                "id_name",
                    "control",
                    "produto",
                    "1970",
                    "1972",
                    "1973",
                    "1974",
                    "1975",
                    "1976",
                    "1977",
                    "1978",
                    "1979",
                    "1980",
                    "1981",
                    "1982",
                    "1983",
                    "1984",
                    "1985",
                    "1986",
                    "1987",
                    "1988",
                    "1989",
                    "1990",
                    "1991",
                    "1992",
                    "1993",
                    "1994",
                    "1995",
                    "1996",
                    "1997",
                    "1998",
                    "1999",
                    "2000",
                    "2001",
                    "2002",
                    "2003",
                    "2004",
                    "2005",
                    "2006",
                    "2007",
                    "2008",
                    "2009",
                    "2010",
                    "2011",
                    "2012",
                    "2013",
                    "2014",
                    "2015",
                    "2016",
                    "2017",
                    "2018",
                    "2019",
                    "2020",
                    "2021",
                    "2022",
                    "2023"]

    df = df.drop(columns=['id'])

    dict_data = df.to_dict('records')

    return {"message": dict_data}

@app.post("/embrapa_processamento/")
def extracao_processamento(processamento):
    url = f"http://vitibrasil.cnpuv.embrapa.br/download/{processamento}.csv"
    df = pd.read_csv(url, delimiter='\t', header=None, skiprows=1)

    # Renomear as colunas
    df.columns = ["id",
                    "control",
                    "cultivar",
                    "1970",
                    "1971",
                    "1972",
                    "1973",
                    "1974",
                    "1975",
                    "1976",
                    "1977",
                    "1978",
                    "1979",
                    "1980",
                    "1981",
                    "1982",
                    "1983",
                    "1984",
                    "1985",
                    "1986",
                    "1987",
                    "1988",
                    "1989",
                    "1990",
                    "1991",
                    "1992",
                    "1993",
                    "1994",
                    "1995",
                    "1996",
                    "1997",
                    "1998",
                    "1999",
                    "2000",
                    "2001",
                    "2002",
                    "2003",
                    "2004",
                    "2005",
                    "2006",
                    "2007",
                    "2008",
                    "2009",
                    "2010",
                    "2011",
                    "2012",
                    "2013",
                    "2014",
                    "2015",
                    "2016",
                    "2017",
                    "2018",
                    "2019",
                    "2020",
                    "2021",
                    "2022",
    ]

    df = df.drop(columns=['id'])

    dict_data = df.to_dict('records')

    return {"message": dict_data}