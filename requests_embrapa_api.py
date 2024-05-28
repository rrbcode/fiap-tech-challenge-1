from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI()

def process_csv(url: str, delimiter: str, skiprows: int, columns: list):
    try:
        df = pd.read_csv(url, delimiter=delimiter, header=None, skiprows=skiprows, encoding='latin1')
        df.columns = columns
        df = df.drop(columns=['id'])
        return df.to_dict('records')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar o arquivo CSV: {e}")

@app.get("/embrapa_producao/")
def extracao_producao_ano():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Producao.csv"
    columns = ["id", "control", "produto"] + [str(year) for year in range(1970, 2024)]
    data = process_csv(url, delimiter=';', skiprows=1, columns=columns)
    return {"message": data}

@app.post("/embrapa_processamento/")
def extracao_processamento(processamento: str):
    url = f"http://vitibrasil.cnpuv.embrapa.br/download/{processamento}.csv"
    columns = ["id", "control", "cultivar"] + [str(year) for year in range(1970, 2023)]
    data = process_csv(url, delimiter='\t', skiprows=1, columns=columns)
    return {"message": data}

@app.get("/embrapa_comercial/")
def extracao_comercial():
    url = "http://vitibrasil.cnpuv.embrapa.br/download/Comercio.csv"
    columns = ["id", "control", "produto"] + [str(year) for year in range(1970, 2024)]
    data = data.replace({'\(': '', '\)': ''}, regex=True)
    data = process_csv(url, delimiter=';', skiprows=1, columns=columns)
    return {"message": dict(data)}

@app.post("/embrapa_importacao/")
def extracao_importacao(importacao_produto: str):
    url = f"http://vitibrasil.cnpuv.embrapa.br/download/{importacao_produto}.csv"
    columns = ["id", "pais"] + [f"qtde_kg_{year}" for year in range(1970, 2024)] + [f"valor_usd_{year}" for year in range(1970, 2024)]
    data = process_csv(url, delimiter=';', skiprows=1, columns=columns)
    return {"message": data}

@app.post("/embrapa_exportacao/")
def extracao_exportacao(exportacao_produto: str):
    url = f"http://vitibrasil.cnpuv.embrapa.br/download/{exportacao_produto}.csv"
    columns = ["id", "pais"] + [f"qtde_kg_{year}" for year in range(1970, 2024)] + [f"valor_usd_{year}" for year in range(1970, 2024)]
    data = process_csv(url, delimiter=';', skiprows=1, columns=columns)
    return {"message": data}