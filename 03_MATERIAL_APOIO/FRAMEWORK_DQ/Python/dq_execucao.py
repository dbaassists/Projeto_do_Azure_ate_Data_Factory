# %%

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

# %%

pd.options.display.max_rows = 999
pd.options.display.max_columns=999
#warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.filterwarnings('ignore')

# %%

arquivo = '../Framework/Arquivos/arq_teste_insert.xlsx'
paramJson 	= "../Framework/config/config.json"

abaProjeto = 'Projeto'
abaFonteDado = 'FonteDado'
abaEstruturaFonteDado = 'EstruturaFonteDado'

# %%

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import consulta_projeto,consulta_fonte_dado,importa_projeto,importa_fonte_dado,consulta_estrutura_fonte_dado

paramJson 	= "../Framework/config/config.json"
arquivo = '../Framework/Arquivos/arq_teste_insert.xlsx'
abaProjeto = 'Projeto'
nomeProjeto = 'TESTE'
nomEtapa = '1 - Etapa de Consulta Projeto'

rt_idprojeto = consulta_projeto(arquivo, nomeProjeto, paramJson, nomEtapa)

#print(rt_idprojeto)

# %% 

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import consulta_projeto,consulta_fonte_dado,importa_projeto,importa_fonte_dado,consulta_estrutura_fonte_dado

paramJson 	= "../Framework/config/config.json"
arquivo = '../Framework/Arquivos/arq_teste_insert.xlsx'
nomeFonteDado = 'TESTE'
idProjeto = 57
nomeProjeto = 'TESTE'
nomEtapa= '2 - Etapa de Consulta Fonte de Dado'

rt_idprojeto = consulta_fonte_dado(arquivo, idProjeto, nomeFonteDado, paramJson, nomEtapa)

print(rt_idprojeto)

# %% 

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import consulta_projeto,consulta_fonte_dado,importa_projeto,importa_fonte_dado,consulta_estrutura_fonte_dado

paramJson 	= "../Framework/config/config.json"
arquivo = '../Framework/Arquivos/arq_teste_insert.xlsx'
abaProjeto = 'Projeto'
nomEtapa = '3 - Etapa de Cadastro de Projeto'

rt_idprojeto, nomeProjeto = importa_projeto(arquivo, abaProjeto, nomEtapa, paramJson)

# %% 

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import consulta_projeto,consulta_fonte_dado,importa_projeto,importa_fonte_dado,consulta_estrutura_fonte_dado

paramJson 	= "../Framework/config/config.json"
arquivo = '../Framework/Arquivos/ibge.xlsx'
aba = 'FonteDado'
nomeProjeto = 'TESTE'
nomEtapa = '6 - Etapa de Cadastro de Fonte Dados'

rt_fonteDado = importa_fonte_dado(arquivo, nomeProjeto, aba, paramJson, nomEtapa)

# %% 

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import consulta_projeto,consulta_fonte_dado,importa_projeto,importa_fonte_dado,consulta_estrutura_fonte_dado

arquivo = '../Framework/Arquivos/arq_teste_insert.xlsx'
abaEstruturaFonteDado = 'EstruturaFonteDado'
idProjeto = 2
idFonteDado = 2
paramJson 	= "../Framework/config/config.json"
nomEtapa = 'Consulta a Estrutura da Fonte de Dado'

IdEstruturaFonteDados = consulta_estrutura_fonte_dado(arquivo, abaEstruturaFonteDado, idProjeto, idFonteDado, paramJson, nomEtapa)

print(IdEstruturaFonteDados)

# %% 

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import importa_estrutura_fonte_dado


pd.options.display.max_rows = 999
pd.options.display.max_columns=999
#warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.filterwarnings('ignore')

paramJson 	= "../Framework/config/config.json"
arquivo = '../Framework/Arquivos/arq_teste_insert.xlsx'
idProjeto = 2
idFonteDados = 2
abaProjeto = 'Projeto'
abaFonteDado = 'FonteDado'
abaEstruturaFonteDado = 'EstruturaFonteDado'
nomEtapa = '9 - Etapa de Cadastro da Estrutura dos Dados'

importa_estrutura_fonte_dado(arquivo, abaEstruturaFonteDado, paramJson, idProjeto, idFonteDados, IdEstruturaFonteDados, nomEtapa)

# %%

import pandas as pd
import json
import warnings
import pandas as pd 
import pyodbc as pc  

from dq_funcao import importa_planilha_dq

pd.options.display.max_rows = 999
pd.options.display.max_columns=999
#warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)
warnings.filterwarnings('ignore')

paramJson 	= fr"C:\Temp\Python_YT\Git\Projeto_do_Azure_ate_Data_Factory\04_ARQUIVO_CONFIG\config_dq.json"
#arquivo = fr"C:\Temp\Python_YT\Git\Projeto_do_Azure_ate_Data_Factory\03_MATERIAL_APOIO\FRAMEWORK_DQ\Arquivos\arq_teste_insert.xlsx"
arquivo = fr"C:\Temp\Python_YT\Git\Projeto_do_Azure_ate_Data_Factory\03_MATERIAL_APOIO\FRAMEWORK_DQ\Arquivos\ibge.xlsx"
abaProjeto = 'Projeto'
abaFonteDado = 'FonteDado'
abaEstruturaFonteDado = 'EstruturaFonteDado'

importa_planilha_dq(arquivo, abaProjeto, abaFonteDado, abaEstruturaFonteDado, paramJson)

# %%

import pandas as pd

df = pd.read_excel('../Framework/Arquivos/ibge.xlsx'
                        , sheet_name = 'FonteDado'
                        , names=['TpoAcao'
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
                        , dtype={'TpoAcao':'str'
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
                        , header=0
                        )

df.info()

#v_projeto = df['NomFonteDados'].values

#print(v_projeto)


# %%
