import requests
import pandas as pd

url_login = "https://api.getsec.com.br/login/entrar/"
dados_login = {
    "usuario": "ti@transpiedadebc.com.br",
    "senha": "Piedade123@"
}

response_login = requests.post(url_login, json=dados_login)

if response_login.status_code == 200:
    token = response_login.json().get("token")
    
    if token:
        url_listar_veiculos = "https://api.getsec.com.br/veiculo/listar/"
        data_listar = {
            "token": token
        }
        
        response_listar = requests.post(url_listar_veiculos, json=data_listar)
        
        if response_listar.status_code == 200:
            lista_veiculos = response_listar.json()
            lista_ids_veiculos = [veiculo['id'] for veiculo in lista_veiculos]
            print(f"IDs dos veículos encontrados: {lista_ids_veiculos}")

            url_posicao = "https://api.getsec.com.br/posicao/listar/"

            dados_posicao_base = {
                "token": token,
                "id_veiculo": "2878",
                "data_hora_inicio": "2024-11-08-00:00:00",
                "data_hora_fim": "2099-11-08-23:59:59"
            }

            all_dataframes = []

            for id_veiculo in lista_ids_veiculos:
                dados_posicao = dados_posicao_base.copy()
                dados_posicao['id_veiculo'] = id_veiculo
                
                response_posicao = requests.post(url_posicao, json=dados_posicao)
                
                if response_posicao.status_code == 200:
                    resposta_posicao = response_posicao.json()
                    print(f"Resposta da API para o veículo {id_veiculo}: {resposta_posicao}")
                    
                    if resposta_posicao.get('codigo') != 1:
                        if 'data' in resposta_posicao and isinstance(resposta_posicao['data'], list):
                            df = pd.json_normalize(resposta_posicao['data'])
                            all_dataframes.append(df)
                        else:
                            print(f'Estrutura de dados inesperada ou campo "data" não encontrado para o veículo {id_veiculo}.')
                    else:
                        print(f'Erro na API para o veículo {id_veiculo}:', resposta_posicao.get('mensagem'))
                else:
                    print(f'Erro ao obter informações para o veículo {id_veiculo}:', response_posicao.status_code, response_posicao.text)

            if all_dataframes:
                final_df = pd.concat(all_dataframes, ignore_index=True)
                print(final_df)
            else:
                print('Nenhum dado foi coletado.')
        else:
            print("Erro ao listar veículos:", response_listar.status_code, response_listar.text)
    else:
        print("Erro: Token não encontrado na resposta de login.")
else:
    print("Erro ao fazer login:", response_login.status_code, response_login.text)
