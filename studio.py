Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:\Users\gabri\Downloads\Amostra 2\Trabalho1.py ===========
df = pd.read_excel(r"C:\Users\gabri\Downloads\Amostra 2\Amostra - Big Data.xlsx")
print(df.head())
                                   Dados da Academia  ...       Unnamed: 11
0                                 Principal Contrato  ...  Público Feminino
1  Plano recorrente 2025 - Treinamento Personaliz...  ...               NaN

[2 rows x 12 columns]
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"Regiao Sudeste"
)
print(df.head())
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 7 columns]
df = df.drop("civil", axis=1)
print(df.head())
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 6 columns]
df = df[df["cidade"].str.lower() == "rio de janeiro"]
print(df.head())
      regiao          cidade  ...  pratica atividade qt de x de atividades fisicas
200  SUDESTE  rio de janeiro  ...                sim                         3 a 4
208  SUDESTE  rio de janeiro  ...                não                 Não informado
214  SUDESTE  rio de janeiro  ...                sim                         3 a 4
224  SUDESTE  rio de janeiro  ...      Não informado                 Não informado
237  SUDESTE  rio de janeiro  ...                sim                         1 a 2

[5 rows x 6 columns]
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"CRM Academia"
    print(df.head())
    
SyntaxError: '(' was never closed
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"CRM Academia")
    
print(df.head())
    
                                     Nome  ...   % F
0            ADRIANA NASCIMENTO MAGDALENA  ...  0.79
1                 AGATHA PEREIRA DA SILVA  ...   NaN
2  AGNES ANNE RIBEIRO NASCIMENTO DA SILVA  ...   NaN
3         ALCIONE FERREIRA QUEIROZ FALCÃO  ...   NaN
4      ALESSANDRA DE SOUZA MACHADO MENDES  ...   NaN

[5 rows x 13 columns]
df = df.drop("Nome", axis=1)
    
print(df.head())
    
                                            Contrato    Gênero  ...   % M   % F
0  Plano recorrente 2025 - Treinamento Personaliz...  Feminino  ...  0.21  0.79
1                      STD - Plano Mensal - Pilates2  Feminino  ...   NaN   NaN
2  Plano recorrente 2025 - Treinamento Personaliz...  Feminino  ...   NaN   NaN
3  STD - Plano recorrente - Treinamento Personali...  Feminino  ...   NaN   NaN
4                          STD - Plano Mensal - T.P3  Feminino  ...   NaN   NaN

[5 rows x 12 columns]
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"Dados gerais")
    
print(df.head())
    
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 7 columns]
df = df[df["regiao"].str.lower() == "SUDESTE"]
    
print(df.head())
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, civil, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df.head())
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, civil, pratica atividade, qt de x de atividades fisicas]
Index: []
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"Rio de Janeiro")
    
print(df.head())
    
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 7 columns]
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"Rio de Janeiro")
    
print(df.head())
    
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 7 columns]
print(df[df["regiao"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, civil, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df[df["cidade"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, civil, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df.head())
    
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 7 columns]
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"CRM Academia")
    
print(df.head())
    
                                     Nome  ...   % F
0            ADRIANA NASCIMENTO MAGDALENA  ...  0.79
1                 AGATHA PEREIRA DA SILVA  ...   NaN
2  AGNES ANNE RIBEIRO NASCIMENTO DA SILVA  ...   NaN
3         ALCIONE FERREIRA QUEIROZ FALCÃO  ...   NaN
4      ALESSANDRA DE SOUZA MACHADO MENDES  ...   NaN

[5 rows x 13 columns]
df = df.drop("Nome", axis=1)
    
print(df.head())
    
                                            Contrato    Gênero  ...   % M   % F
0  Plano recorrente 2025 - Treinamento Personaliz...  Feminino  ...  0.21  0.79
1                      STD - Plano Mensal - Pilates2  Feminino  ...   NaN   NaN
2  Plano recorrente 2025 - Treinamento Personaliz...  Feminino  ...   NaN   NaN
3  STD - Plano recorrente - Treinamento Personali...  Feminino  ...   NaN   NaN
4                          STD - Plano Mensal - T.P3  Feminino  ...   NaN   NaN

[5 rows x 12 columns]
print(df[df["Contrato"].isna()])
    
Empty DataFrame
Columns: [Contrato, Gênero, Idade, Tipo do contrato, Valor do contrato, Principal Contrato, Média de idade, Ticket Médio, Qt Masculino, Qt Masculino.1, % M, % F]
Index: []
print(df[df["Gênero"].isna()])
    
Empty DataFrame
Columns: [Contrato, Gênero, Idade, Tipo do contrato, Valor do contrato, Principal Contrato, Média de idade, Ticket Médio, Qt Masculino, Qt Masculino.1, % M, % F]
Index: []
print(df[df["Idade"].isna()])
    
Empty DataFrame
Columns: [Contrato, Gênero, Idade, Tipo do contrato, Valor do contrato, Principal Contrato, Média de idade, Ticket Médio, Qt Masculino, Qt Masculino.1, % M, % F]
Index: []
print(df[df["Tipo do contrato"].isna()])
    
Empty DataFrame
Columns: [Contrato, Gênero, Idade, Tipo do contrato, Valor do contrato, Principal Contrato, Média de idade, Ticket Médio, Qt Masculino, Qt Masculino.1, % M, % F]
Index: []
print(df[df["Valor do contrato"].isna()])
    
Empty DataFrame
Columns: [Contrato, Gênero, Idade, Tipo do contrato, Valor do contrato, Principal Contrato, Média de idade, Ticket Médio, Qt Masculino, Qt Masculino.1, % M, % F]
Index: []
df.to_excel("C:\Users\gabri\Downloads\Amostra 2\Amostra Tratada.xlsx", index=False)
    
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
df.to_excel("C:\Users\gabri\Downloads\Amostra 2\Amostra Tratada.xlsx", index=False)
    
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
df.to_excel(r"C:\Users\gabri\Downloads\Amostra 2\Amostra Tratada.xlsx", index=False)
    
df = pd.read_excel(r"C:\Users\gabri\Downloads\Amostra 2\Amostra Tratada.xlsx")
    
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"CRM Academia")
    
print(df.head())
    
                                     Nome  ...   % F
0            ADRIANA NASCIMENTO MAGDALENA  ...  0.79
1                 AGATHA PEREIRA DA SILVA  ...   NaN
2  AGNES ANNE RIBEIRO NASCIMENTO DA SILVA  ...   NaN
3         ALCIONE FERREIRA QUEIROZ FALCÃO  ...   NaN
4      ALESSANDRA DE SOUZA MACHADO MENDES  ...   NaN

[5 rows x 13 columns]
df = df.drop("Nome", axis=1)
    
df.to_excel(r"C:\Users\gabri\Downloads\Amostra 2\Amostra Tratada.xlsx", index=False)
    
df = pd.read_excel(r"C:\Users\gabri\Downloads\Amostra 2\Amostra - Big Data.xlsx")
    
print(df.head())
    
                                   Dados da Academia  ...       Unnamed: 11
0                                 Principal Contrato  ...  Público Feminino
1  Plano recorrente 2025 - Treinamento Personaliz...  ...               NaN

[2 rows x 12 columns]
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"Dados gerais"
    )
    
df = pd.read_excel(
    r"C:\Users\gabri\Downloads\Amostra\Amostra - Big Data.xlsx",
    sheet_name=r"Dados gerais")
    
print(df.head())
    
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 7 columns]
df = df.drop("civil", axis=1)
    
print(df.head())
    
         regiao  ... qt de x de atividades fisicas
0  CENTRO-OESTE  ...                 Não informado
1  CENTRO-OESTE  ...                         1 a 2
2      NORDESTE  ...                 todos os dias
3  CENTRO-OESTE  ...                         5 a 6
4      NORDESTE  ...                 todos os dias

[5 rows x 6 columns]
print(df[df["regiao"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df[df["cidade"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df[df["idade"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df[df["genero"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df[df["pratica atividade"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, pratica atividade, qt de x de atividades fisicas]
Index: []
print(df[df["qt de x de atividades fisicas"].isna()])
    
Empty DataFrame
Columns: [regiao, cidade, idade, genero, pratica atividade, qt de x de atividades fisicas]
Index: []
df.to_excel(r"C:\Users\gabri\Downloads\Amostra 2\Amostra (Dados gerais).xlsx", index=False)
    
