# %% 

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

# %% 

def registra_log(arquivo, nomeProjeto, fonteDado, nomEtapa, nomStatus, dscMsgProcessamento, paramJson):
    
    v_arquivo = arquivo
    v_nomeProjeto = nomeProjeto
    v_fonteDado = fonteDado
    v_nomEtapa = nomEtapa
    v_nomStatus = nomStatus
    v_dscMsgProcessamento = dscMsgProcessamento 
    v_paramJson = paramJson

    file 		= open(v_paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
    try:

        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()
        
        cur.execute("""INSERT INTO dq.TB_LOG
        (
            NomArquivoProcessado
            ,NomProjeto
            ,NomFonteDado
            ,NomEtapa
            ,DscMsgProcessamento
            ,NomStatus
        )
        values(?,?,?,?,?,?)"""
        , v_arquivo
        , v_nomeProjeto
        , v_fonteDado
        , v_nomEtapa
        , v_dscMsgProcessamento
        , v_nomStatus)  
        
        cnxn.commit()
        cur.close()   
    
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)
        
        v_dscMsgProcessamento = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:"
        
        cur.execute("""INSERT INTO dq.TB_LOG
        (
            NomArquivoProcessado
            ,NomProjeto
            ,NomFonteDado
            ,NomEtapa
            ,DscMsgProcessamento
            ,NomStatus
        )
        values(?,?,?,?,?,?)"""
        , v_arquivo
        , v_nomeProjeto
        , v_fonteDado
        , v_nomEtapa
        , v_dscMsgProcessamento
        , v_nomStatus)  

        cnxn.commit()
        cur.close()   

    except pc.Error as e:
        
        print("Error: Failed to insert data into the database:", e)
        
        v_dscMsgProcessamento = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:"
        
        cur.execute("""INSERT INTO dq.TB_LOG
        (
            NomArquivoProcessado
            ,NomProjeto
            ,NomFonteDado
            ,NomEtapa
            ,DscMsgProcessamento
            ,NomStatus
        )
        values(?,?,?,?,?,?)"""
        , v_arquivo
        , v_nomeProjeto
        , v_fonteDado
        , v_nomEtapa
        , v_dscMsgProcessamento
        , v_nomStatus)     

        cnxn.commit()
        cur.close()                
        
    finally:
        
        print("Processo Finalizado!")

# %% 
        
def consulta_projeto(nomArquivo, nomeProjeto, paramJson, nomEtapa):
    
    v_filtroNomeProjeto = nomeProjeto
    v_fonteDado = ''
    v_nomArquivo  = nomArquivo
    v_paramJson = paramJson
    v_nomEtapa = nomEtapa

    file 		= open(v_paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
    try:

        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()

        queryIdProjeto = f"""SELECT ISNULL(idProjeto,-1) idProjeto 
                            FROM [dq].[TB_PROJETO] 
                            WHERE [NomProjeto] = '{v_filtroNomeProjeto}';"""

        dfNomeProjeto = pd.read_sql(queryIdProjeto, cnxn)

        cur.close()
        cnxn.close()   

        if dfNomeProjeto.empty:

            idProjeto = -1

        else:

            idProjeto = dfNomeProjeto['idProjeto'].to_string(index=None)
            
        v_nomStatus = 'S'
        v_dscMsgProcessamento = "3.1 - Consulta realizada com sucesso."
        
        registra_log(v_nomArquivo
                     , v_filtroNomeProjeto
                     , v_fonteDado
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  
            
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:", e
        
        registra_log(v_nomArquivo
                     , v_filtroNomeProjeto
                     , v_fonteDado
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)

    except pc.Error as e:
        
        print("consulta_projeto - Error: Failed to insert data into the database:", e)        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:"
        
        registra_log(v_nomArquivo
                     , v_filtroNomeProjeto
                     , v_fonteDado
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)        
        
    finally:

        print("consulta_projeto - Processo Finalizado!")
        #cur.close()
        #cnxn.close()            
    
    return idProjeto
    

# %%

def consulta_fonte_dado(nomArquivo, idProjeto, nomeFonteDado, paramJson, nomEtapa):
    
    v_filtroidProjeto = idProjeto
    v_filtroNomFonteDados = nomeFonteDado
    v_paramJson = paramJson
    v_nomEtapa = nomEtapa
    v_arquivo = nomArquivo
    
    file 		= open(v_paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
    try:

        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()

        queryIdFonteDados = f"""
        SELECT ISNULL(SUM(tFDado.idFonteDados),-1) idFonteDados 
                , tPro.NomProjeto
        FROM [dq].[TB_FONTE_DADO] tFDado
        inner join [dq].[TB_PROJETO] tPro
        on tFDado.IdProjeto = tPro.IdProjeto                            
        where tFDado.[NomFonteDados] = '{v_filtroNomFonteDados}'
        and tPro.[IdProjeto] = {v_filtroidProjeto}
        GROUP BY tPro.NomProjeto;
        """
        
        dfNomFonteDados = pd.read_sql(queryIdFonteDados, cnxn)

        idFonteDados = dfNomFonteDados['idFonteDados'].to_numpy()
        v_filtroNomeProjeto = dfNomFonteDados['NomProjeto'].to_string(index=False)

        if len(idFonteDados) == 0:
            idFonteDados = -1
        else:
            idFonteDados = dfNomFonteDados['idFonteDados'].to_string(index=False)
            
        v_nomStatus = 'S'

        v_dscMsgProcessamento = "5 - Etapa de Verificar se a Fonte de Dados está Cadastrada."

        registra_log(v_arquivo
                     , v_filtroNomFonteDados
                     , v_filtroNomFonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)         
            
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:"
        
        registra_log(v_arquivo
                     , v_filtroNomFonteDados
                     , v_filtroNomFonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)

    except pc.Error as e:
        
        print("importa_projeto - Error: Failed to insert data into the database:", e)        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:"
        
        registra_log(v_arquivo
                     , v_filtroNomFonteDados
                     , v_filtroNomFonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  
        
    except NameError as e:

        print("Error: Name is not defined:", e)        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = e
        
        registra_log(v_arquivo
                     , v_filtroNomFonteDados
                     , v_filtroNomFonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)           

    finally:

        print("consulta_fonte_dado - Processo Finalizado!")
        cur.close()
        cnxn.close()    
   
    return idFonteDados


# %% 

def importa_projeto(arquivo, aba, nomEtapa, paramJson):
    
    v_arquivo = arquivo
    v_aba = aba
    v_paramJson = paramJson
    v_nomEtapa = nomEtapa
    
    df = pd.read_excel(v_arquivo
                       , sheet_name=v_aba
                       , names=['DscUltimaAcao'
                                ,'IdProjeto'
                                ,'NomCategoriaProjeto'
                                ,'NomProjeto'
                                ,'NumMaxIteracoes'
                                ,'NomRespProjeto'
                                ,'NomRespTecnico'
                                ]
                        , dtype={'DscUltimaAcao':'str'
                                ,'IdProjeto':'str'
                                ,'NomCategoriaProjeto':'str'
                                ,'NomProjeto':'str'
                                ,'NumMaxIteracoes':'str'
                                ,'NomRespProjeto':'str'
                                ,'NomRespTecnico':'str'
                                }
                        , header=0
                       )
   
    paramJson 	= v_paramJson
    file 		= open(paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
    try:

        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()

        nomeProjeto = df['NomProjeto'].to_string(index=False)

        nomEtapa = '2 - Etapa de Consulta Projeto.'

        idProjeto = consulta_projeto(v_arquivo
                                     , nomeProjeto
                                     , paramJson
                                     , nomEtapa)

        if idProjeto != -1:

            print('Projeto já cadastrado!')
            
            v_nomStatus = 'S'

            v_dscMsgProcessamento = "3 - Não será realizado o cadastro pois o projeto já está cadastrado em nossa base de dados."

            registra_log(v_arquivo
                         , nomeProjeto
                         , nomeProjeto
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  

        elif idProjeto == -1:

            for index, rowProjeto in df.iterrows():
                 
                 cur.execute("""INSERT INTO dq.TB_PROJETO
                             (
                             NomCategoriaProjeto
                             ,NomProjeto
                             ,NumMaxIteracoes
                             ,NomRespProjeto
                             ,NomRespTecnico
                             ,DscUltimaAcao
                             )
                             values(?,?,?,?,?,?)"""
                             , rowProjeto.NomCategoriaProjeto
                             , rowProjeto.NomProjeto
                             , rowProjeto.NumMaxIteracoes
                             , rowProjeto.NomRespProjeto
                             , rowProjeto.NomRespTecnico
                             , rowProjeto.DscUltimaAcao)
                               
            v_nomStatus = 'S'
            
            v_dscMsgProcessamento = "3 - Cadastrado do Projeto realizado com sucesso."

            registra_log(v_arquivo
                         , nomeProjeto
                         , nomeProjeto
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  

        cnxn.commit()
        cur.close()     

        v_nomEtapa = '3.1 - Consulta do Código do Projeto Cadastrado.'

        idProjeto = consulta_projeto(v_arquivo
                                     , nomeProjeto
                                     , paramJson
                                     , v_nomEtapa)
            
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:"
        
        registra_log(v_arquivo
                     , nomeProjeto
                     , nomeProjeto
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  

    except pc.Error as e:
        
        print("importa_projeto - Error: Failed to insert data into the database:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:"
        
        registra_log(v_arquivo
                     , nomeProjeto
                     , nomeProjeto
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson) 

    else:

        print("Dado Inserido com Sucesso.")

    finally:

        print("importa_projeto - Processo de Cadastro do Projeto Finalizada.")
        #cur.close()
        #cnxn.close()       
    
    return idProjeto, nomeProjeto


# %% 

def importa_fonte_dado(arquivo, nomeProjeto, aba, paramJson, nomEtapa):
    
    v_arquivo = arquivo
    v_projeto = nomeProjeto
    v_aba = aba
    v_paramJson = paramJson
    v_nomEtapa = nomEtapa
    
    df = pd.read_excel(v_arquivo
                        , sheet_name = v_aba 
                        , names=['DscUltimaAcao'
                        ,'IdProjeto'
                        ,'NomFonteDados'
                        ,'DscFonteDados'
                        ,'DataLakeFolder'
                        ,'DscExtensaoArquivo'
                        ,'TpoDelimitadorArquivo'
                        ,'NomTabela'
                        ,'NomAbaExcel'
                        ,'PathBronzeDestination'
                        ,'NomEncodingArquivo']
                        , dtype={'DscUltimaAcao':'str'
                                ,'IdProjeto' : 'str'
                                ,'NomFonteDados' : 'str'
                                ,'DscFonteDados' : 'str'
                                ,'DataLakeFolder' : 'str'
                                ,'DscExtensaoArquivo' : 'str'
                                ,'TpoDelimitadorArquivo' : 'str'
                                ,'NomTabela' : 'str'
                                ,'NomAbaExcel' : 'str'
                                ,'PathBronzeDestination' : 'str'
                                ,'NomEncodingArquivo' : 'str'}
                        , header=0)
        
    paramJson 	= v_paramJson
    file 		= open(paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
    try:

        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()

        nomeFonteDados = df['NomFonteDados'].to_string(index=False)

        v_fonteDados = nomeFonteDados
        
        nomEtapa = '4 - Etapa de Consulta Projeto.'

        idProjeto = consulta_projeto(v_arquivo
                                     , nomeProjeto
                                     , v_paramJson
                                     , nomEtapa)

        nomEtapa = '5 - Etapa de Consulta Fonte Dados'

        idFonteDados = consulta_fonte_dado(v_arquivo
                                           , idProjeto
                                           , nomeFonteDados
                                           , v_paramJson
                                           , nomEtapa)

        df['IdProjeto'] = idProjeto   

        if idFonteDados == 1:
            
            print('Fonte de Dados Cadastrada!')            
                        
            v_nomStatus = 'S'

            v_dscMsgProcessamento = "6 - Fonte de Dados já está cadastrado na base de dados."        

            registra_log(v_arquivo
                         , v_fonteDados
                         , v_fonteDados
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  

        elif idFonteDados == -1:

            for index, rowFonteDado in df.iterrows():

                cur.execute("""INSERT INTO [dq].[TB_FONTE_DADO]
                         (
                             [IdProjeto]
                             ,[NomFonteDados]
                             ,[DscFonteDados]
                             ,[DataLakeFolder]
                             ,[DscExtensaoArquivo]
                             ,[TpoDelimitadorArquivo]
                             ,[NomTabela]
                             ,[NomAbaExcel]
                             ,[PathBronzeDestination]
                             ,[NomEncodingArquivo]
                             ,[DscUltimaAcao]
                         ) values(?,?,?,?,?,?,?,?,?,?,?)"""
                         , rowFonteDado.IdProjeto
                         , rowFonteDado.NomFonteDados
                         , rowFonteDado.DscFonteDados
                         , rowFonteDado.DataLakeFolder
                         , rowFonteDado.DscExtensaoArquivo
                         , rowFonteDado.TpoDelimitadorArquivo
                         , rowFonteDado.NomTabela
                         , 'rowFonteDado.NomAbaExcel'
                         , rowFonteDado.PathBronzeDestination
                         , rowFonteDado.NomEncodingArquivo
                         , rowFonteDado.DscUltimaAcao)

                v_nomStatus = 'S'

                v_dscMsgProcessamento = "6 - Fonte de Dados Cadastrada com Sucesso."

                registra_log(v_arquivo
                            , v_fonteDados
                            , v_fonteDados
                            , v_nomEtapa
                            , v_nomStatus
                            , v_dscMsgProcessamento
                            , v_paramJson)

                cnxn.commit()
                cur.close()   
  
        nomEtapa = '7 - Retorno do código da fonte de dados cadastrada.'

        idFonteDados = consulta_fonte_dado(v_arquivo
                                           , idProjeto
                                           , nomeFonteDados
                                           , v_paramJson
                                           , nomEtapa)
            
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:"
        
        registra_log(v_arquivo
                     , v_fonteDados
                     , v_fonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  

    except pc.Error as e:
        
        print("importa_projeto - Error: Failed to insert data into the database:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:"
        
        registra_log(v_arquivo
                     , v_fonteDados
                     , v_fonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)

    except NameError as e:
        print("Error: Name is not defined:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = e
        
        registra_log(v_arquivo
                     , v_fonteDados
                     , v_fonteDados
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)
        
        
    finally:

        print("importa_fonte_dado - Processo Finalizado!")

        #cur.close()
        #cnxn.close()     
 
    return idFonteDados


# %% 

def consulta_estrutura_fonte_dado(arquivo, abaEstruturaFonteDado, idProjeto, idFonteDado, paramJson, nomEtapa):
    
    v_arquivo = arquivo
    v_abaEstruturaFonteDado = abaEstruturaFonteDado
    v_paramJson = paramJson    
    v_idProjeto = idProjeto
    v_idFonteDado = idFonteDado
    v_nomEtapa = nomEtapa
    
    df = pd.read_excel(v_arquivo
                        , sheet_name = v_abaEstruturaFonteDado)
    
    file 		= open(v_paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']
            
    try:

        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()
        
        queryNomProjeto = f"""SELECT ISNULL(b.NomProjeto,'-1') NomProjeto
                        FROM [dq].[TB_PROJETO] B
                        WHERE B.[IdProjeto] = {str(v_idProjeto)};"""
        
        dfNomProjeto = pd.read_sql(queryNomProjeto, cnxn)

        if dfNomProjeto.empty:

            v_idProjeto = -1

            v_nomStatus = 'S'
            
            v_dscMsgProcessamento = "8 - Não foi encontrado o projeto cadastrado na base de Data Quality."
            
            v_filtroNomeProjeto = str(v_idProjeto)
            
            IdEstruturaFonteDados = -1

            print(v_dscMsgProcessamento)
            
            registra_log(v_arquivo
                         , v_filtroNomeProjeto
                         , v_filtroNomeProjeto
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  

        else:        

            queryIdProjeto = f"""SELECT ISNULL(max(a.IdEstruturaFonteDados),0) IdEstruturaFonteDados
                                    FROM [dq].[TB_ESTRUTURA_FONTE_DADO] a 
                                    inner join [dq].[TB_PROJETO] B
                                    on a.[IdProjeto] = b.[IdProjeto]
                                    WHERE a.[IdProjeto] = {v_idProjeto} 
                                    AND a.[IdFonteDados] = {v_idFonteDado};"""
            
            dfFonteDados = pd.read_sql(queryIdProjeto, cnxn)

            IdEstruturaFonteDados = dfFonteDados['IdEstruturaFonteDados'].to_string(index=False)

            v_filtroNomeProjeto = dfNomProjeto['NomProjeto'].to_string(index=False)

            if IdEstruturaFonteDados != '0':
                
                print('Etapa de confirmação do cadastro da Estrutura da Fonte de Dados.')
                print('Estrutura da Fonte de Dados Cadastrada!')

            elif IdEstruturaFonteDados == '0':

                importa_estrutura_fonte_dado(arquivo
                                             , abaEstruturaFonteDado
                                             , paramJson
                                             , v_idProjeto
                                             , v_idFonteDado
                                             , IdEstruturaFonteDados
                                             , nomEtapa)
                
            v_nomStatus = 'S'

            v_dscMsgProcessamento = "9 - Consulta realizada com sucesso!"
            
            registra_log(v_arquivo
                         , v_filtroNomeProjeto
                         , v_filtroNomeProjeto
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  
                        
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:"
        
        registra_log(v_arquivo
                     , v_filtroNomeProjeto
                     , v_filtroNomeProjeto
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)

    except pc.Error as e:
        
        print("importa_projeto - Error: Failed to insert data into the database:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:"
        v_nomEtapa = 'importa_projeto - Consulta Projeto'
        
        registra_log(v_arquivo
                     , v_filtroNomeProjeto
                     , v_filtroNomeProjeto
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  

    else:

        if v_idProjeto == -1:

            print("Não existe um projeto cadastrado para essa estrutura!")

        else:

            print("Existe um projeto cadastrado para essa estrutura!")

    finally:

        print("consulta_estrutura_fonte_dado - Processo Finalizado!")

        cur.close()
        cnxn.close()     
    
    return IdEstruturaFonteDados
    
# %% 

def importa_estrutura_fonte_dado(arquivo, aba, paramJson, idProjeto, idFonteDado, IdEstruturaFonteDados, nomEtapa):
    
    v_arquivo = arquivo
    v_aba = aba
    v_paramJson = paramJson
    v_idProjeto = int(idProjeto)
    v_idFonteDado = int(idFonteDado)
    v_nomEtapa = nomEtapa
    v_IdEstruturaFonteDados = IdEstruturaFonteDados
    
    df = pd.read_excel(v_arquivo
                        , sheet_name = v_aba
                        , names=['DscUltimaAcao'
                                ,'IdProjeto'
                                ,'NomFonteDados'
                                ,'IdFonteDados'
                                ,'NomColuna'
                                ,'TpoDado'
                                ,'NumCasasDecimais'
                                ,'FlagColunaNula'
                                ,'NumTamanhoMaximo'
                                ,'FlagColunaObrigatoria'
                                ,'FlagDadoSensivel'
                                ,'NumSeqColunaTabela'
                                ]
                        , dtype={'DscUltimaAcao':'str'
                                ,'IdProjeto':'str'
                                ,'NomFonteDados':'str'
                                ,'IdFonteDados':'str'
                                ,'NomColuna':'str'
                                ,'TpoDado':'str'
                                ,'NumCasasDecimais':'str'
                                ,'FlagColunaNula':'str'
                                ,'NumTamanhoMaximo':'str'
                                ,'FlagColunaObrigatoria':'str'
                                ,'FlagDadoSensivel':'str'
                                ,'NumSeqColunaTabela':'str'
                                }
                        , header=0)        
    
    v_NomFonteDados = df['NomFonteDados'].drop_duplicates(keep='last').head(1).values[0]

    #print(v_NomFonteDados)

    paramJson 	= v_paramJson
    file 		= open(paramJson)
    dfJson 		= json.load(file)

    for tag in dfJson:

        if tag == 'Config':

            server 		= dfJson[tag]['server']
            database 	= dfJson[tag]['database']
            username 	= dfJson[tag]['username']
            password 	= dfJson[tag]['password']

    try:
            
        connection_string = f"""Driver=SQL Server;
                                Server={server};
                                Database={database};
                                UID={username};
                                PWD={password};
                                Trusted_Connection=Yes;"""

        cnxn = pc.connect(connection_string)    

        cur=cnxn.cursor()

        queryNomProjeto = f"""SELECT P.IdProjeto, FD.IdFonteDados, P.NomProjeto, FD.NomFonteDados
                                FROM dq.TB_PROJETO P
                                INNER JOIN dq.TB_FONTE_DADO FD
                                ON P.IdProjeto = FD.IdProjeto
                                WHERE FD.[NomFonteDados] = '{v_NomFonteDados}';"""
        
        dfNomProjeto = pd.read_sql(queryNomProjeto, cnxn)

        v_NomeProjeto = dfNomProjeto['NomProjeto'].to_string(index=False)
        v_FonteDados = dfNomProjeto['NomFonteDados'].to_string(index=False) 
        v_IdFonteDados = dfNomProjeto['IdFonteDados'].to_string(index=False) 
        v_IdProjeto = dfNomProjeto['IdProjeto'].to_string(index=False)        

        #v_projetoFonteDado = v_filtroNomeProjeto + ' - ' + v_filtroFonteDados
        
        if v_IdEstruturaFonteDados != '0':
            
            v_nomStatus = 'S'

            v_dscMsgProcessamento = "A estrutura do arquivo já está cadastrado em nossa base de dados!"

            registra_log(v_arquivo
                         , v_NomeProjeto
                         , v_NomeProjeto
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  

        elif v_IdEstruturaFonteDados == '0':            
            
            df['IdFonteDados'] = v_IdFonteDados
            df['IdProjeto'] = v_IdProjeto

            for index, rowEstruturaFonteDado in df.iterrows():


                    queryFD = f"""INSERT INTO [dq].[TB_ESTRUTURA_FONTE_DADO](
                                  [IdProjeto]
                                 ,[IdFonteDados]
                                 ,[NomFonteDados]
                                 ,[NomColuna]
                                 ,[TpoDado]
                                 ,[NumCasasDecimais]
                                 ,[FlagColunaNula]
                                 ,[NumTamanhoMaximo]
                                 ,[FlagColunaObrigatoria]
                                 ,[FlagDadoSensivel]
                                 ,[NumSeqColunaTabela]
                                 ,[DscUltimaAcao]) 
                                 values(
                                    {rowEstruturaFonteDado.IdProjeto}
                                    ,{rowEstruturaFonteDado.IdFonteDados}
                                    ,{rowEstruturaFonteDado.NomFonteDados}
                                    ,{rowEstruturaFonteDado.NomColuna}
                                    ,{rowEstruturaFonteDado.TpoDado}
                                    ,{rowEstruturaFonteDado.NumCasasDecimais}
                                    ,{rowEstruturaFonteDado.FlagColunaNula}
                                    ,{rowEstruturaFonteDado.NumTamanhoMaximo}
                                    ,{rowEstruturaFonteDado.FlagColunaObrigatoria}
                                    ,{rowEstruturaFonteDado.FlagDadoSensivel}
                                    ,{rowEstruturaFonteDado.NumSeqColunaTabela}
                                    ,{rowEstruturaFonteDado.DscUltimaAcao}
                                    )"""

                    #print(queryFD)

                    cur.execute("""INSERT INTO [dq].[TB_ESTRUTURA_FONTE_DADO](
                                  [IdProjeto]
                                 ,[IdFonteDados]
                                 ,[NomFonteDados]
                                 ,[NomColuna]
                                 ,[TpoDado]
                                 ,[NumCasasDecimais]
                                 ,[FlagColunaNula]
                                 ,[NumTamanhoMaximo]
                                 ,[FlagColunaObrigatoria]
                                 ,[FlagDadoSensivel]
                                 ,[NumSeqColunaTabela]
                                 ,[DscUltimaAcao]) values(?,?,?,?,?,?,?,?,?,?,?,?)"""
                                 ,rowEstruturaFonteDado.IdProjeto  
                                 ,rowEstruturaFonteDado.IdFonteDados
                                 ,rowEstruturaFonteDado.NomFonteDados
                                 ,rowEstruturaFonteDado.NomColuna
                                 ,rowEstruturaFonteDado.TpoDado
                                 ,rowEstruturaFonteDado.NumCasasDecimais
                                 ,rowEstruturaFonteDado.FlagColunaNula
                                 ,rowEstruturaFonteDado.NumTamanhoMaximo
                                 ,rowEstruturaFonteDado.FlagColunaObrigatoria
                                 ,rowEstruturaFonteDado.FlagDadoSensivel
                                 ,rowEstruturaFonteDado.NumSeqColunaTabela
                                 ,rowEstruturaFonteDado.DscUltimaAcao)
                    
            v_nomStatus = 'S'
            v_dscMsgProcessamento = "Projeto Cadastrado com sucesso!"

            registra_log(v_arquivo
                         , v_NomeProjeto
                         , v_NomeProjeto
                         , v_nomEtapa
                         , v_nomStatus
                         , v_dscMsgProcessamento
                         , v_paramJson)  

            cnxn.commit()
            cur.close()   

            nomEtapa = '10 - Etapa de Consulta da Estrutura Cadastrada'
            
            IdEstruturaFonteDados = consulta_estrutura_fonte_dado(v_arquivo
                                                                , v_aba
                                                                , v_idProjeto
                                                                , v_idFonteDado
                                                                , v_paramJson
                                                                , nomEtapa)
                                
    except pc.IntegrityError as e:
        
        print("Error: Integrity constraint violation occurred:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Integrity constraint violation occurred:", e
        #omEtapa = 'Consulta Projeto'
        
        registra_log(v_arquivo
                     , v_NomeProjeto
                     , v_NomeProjeto
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  

    except pc.Error as e:
        
        print("importa_estrutura_fonte_dado - Error: Failed to insert data into the database:", e)
        
        v_nomStatus = 'E'
        v_dscMsgProcessamento = "Error: Failed to insert data into the database:" #, e
        v_nomEtapa = 'importa_estrutura_fonte_dado - Consulta Projeto'
        
        registra_log(v_arquivo
                     , v_NomeProjeto
                     , v_NomeProjeto
                     , v_nomEtapa
                     , v_nomStatus
                     , v_dscMsgProcessamento
                     , v_paramJson)  

    finally:

        print("importa_estrutura_fonte_dado - Processo Finalizado! Aquiiiiiiiii")


        cur.close()
        cnxn.close()           
        
    return IdEstruturaFonteDados

# %% 

def importa_planilha_dq(arquivo, abaProjeto, abaFonteDado, abaEstruturaFonteDado, paramJson):
    
    v_arquivo = arquivo
    v_abaProjeto = abaProjeto
    v_abaFonteDado = abaFonteDado
    v_abaEstruturaFonteDado = abaEstruturaFonteDado
    v_paramJson = paramJson
    
    idProjeto, nomeProjeto = importa_projeto(v_arquivo
                                , v_abaProjeto
                                , '2 - Etapa de Cadastro de Projeto'
                                , v_paramJson
                                )
    
    idFonteDados = importa_fonte_dado(v_arquivo
                                      , nomeProjeto
                                      , v_abaFonteDado
                                      , v_paramJson
                                      , '6 - Etapa de Cadastro de Fonte Dados'
                                      )
    
    print('idProjeto')
    print(int(idProjeto))
    print('idFonteDados')
    print(idFonteDados)
    
    IdEstruturaFonteDados = consulta_estrutura_fonte_dado(arquivo
                                                          , abaEstruturaFonteDado
                                                          , int(idProjeto)
                                                          , idFonteDados
                                                          , paramJson
                                                          , '7 - Etapa de Consulta Estrutura da Fonte de Dado')
   
    print('O idProjeto cadastrado é: ')
    print(idProjeto)
    
    print('--------------------------------------------------------')
    
    print('O idFonteDados cadastrado é: ')
    print(idFonteDados)
    
    print('--------------------------------------------------------')
    print('O IdEstruturaFonteDados cadastrado é: ')
    print(IdEstruturaFonteDados)

# %%

# %%
