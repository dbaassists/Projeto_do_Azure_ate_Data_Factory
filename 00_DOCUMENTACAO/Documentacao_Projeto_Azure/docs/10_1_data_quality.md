# Workshop BI com Azure e seus componentes

### 10.1 - Data Quality - Como que funciona?

O processo de Data Quality desenvolvido possui ALGUMAS etapas.

1 - Cadastro da Fonte de Dado;

* 1.1 - Preenchimento de uma planilha com informações da fonte;

2 - Validação da Fonte

* 2.1 - Validação da planilha preenchida conforme as regras pré-definidas.

3 - Cadastro da Fonte no Data Quality

* 3.1 - Após validação da planilha, a fonte será cadastrada em nossa solução de Data Quality.

### 1 - Preenchimento da Planilha

Regras comuns para todas as abas.

| Seq | Etapa | Regra | Descrição |
| ------ |  ------ |  ------ |  ------ |
| Seq 01 | Validação Abas Planilha | A planilha deve conter apenas as abas Projeto, FonteDado, EstruturaFonteDado. | Caso exista alguma aba que com nomenclatura diferente, o arquivo deve ser rejeitado. |
| Seq 02 | Etapas permitidas no fluxo. | Cada aba possui uma coluna ETAPA. Nessa coluna são permitidos apenas os seguintes valores CADASTRAR, ALTERAR e EXCLUIR.  | Caso exista algum valor diferente, o arquivo deve ser rejeitado. |
| Seq 03 | Validação Planilha sem Dados | Todas as abas da planilha são validadas para garantir que estejam preenchidas. | Caso alguma aba esteja sem informação, o arquivo deve ser rejeitado. |
| Seq 04 | Abas Projeto e FonteDados | Nessas abas, só é permitido a existência de um único registro. | Caso existam 2 ou mais registros nas abas Projeto e FonteDados, o arquivo deve ser rejeitado. |

### 2 - Validação dos Dados antes do Cadastro

### 2.1 - Aba Projeto

| Seq | Etapa | Regra | Descrição |
| ------ |  ------ |  ------ |  ------ |
| Seq 01 | Preenchimento Coluna "Etapa" | Caso esteja assinalado como CADASTRAR, a coluna "Código Projeto" não pode estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 02 | Preenchimento Coluna "Etapa" | Caso esteja assinalado como ATUALIZAR ou EXCLUIR, a coluna "Código Projeto" deverá estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 03 | Preenchimento da Coluna "Código do Projeto" | Essa coluna deverá ser preenchida apenas caso a coluna "Etapa" esteja preenchida com as informações "ALTERAR" ou "EXCLUIR". O valor dessa coluna é gerado no momento do cadastro do projeto. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 04 | Preenchimento Coluna "Categoria Projeto" | Essa coluna deverá estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 05 | Preenchimento Coluna "Nome Projeto" | Essa coluna deverá estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 06 | Preenchimento Coluna "Número de Execuções" | Essa coluna não possui seu preenchimento obrigatório, porém caso seja, são aceitos apenas valores inteiros no intervalo de 1 à 10. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 07 | Validação do Preenchimento Colunas "Nome Reponsável Projeto" e "Nome Responsável Técnico"| Essa coluna deverá estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 08 | Validação do Preenchimento Colunas "Nome Reponsável Projeto" e "Nome Responsável Técnico"| É realizada uma validação para garantir que um e-mail foi informado. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |

### 2.2 - Aba FonteDado

| Seq | Etapa | Regra | Descrição |
| ------ |  ------ |  ------ |  ------ |
| Seq 01 | Preenchimento Coluna "Etapa" | Caso esteja assinalado como CADASTRAR, a coluna "Código Projeto" não pode estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 02 | Preenchimento Coluna "Etapa" | Caso esteja assinalado como ATUALIZAR ou EXCLUIR, a coluna "Código Projeto" deverá estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 03 | Preenchimento da Coluna "Código da Fonte" | Essa coluna deverá ser preenchida apenas caso a coluna "Etapa" esteja preenchida com as informações "ALTERAR" ou "EXCLUIR". O valor dessa coluna é gerado no momento do cadastro da fonte de dado. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 04 | Preenchimento da Coluna "Nome Fonte Dado" | Essa coluna deverá ser preenchida. Essa coluna representa o nome do arquivo que será importado. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 05 | Preenchimento da Coluna "Breve Descrição" | Essa coluna deverá ser preenchida. Ela funciona como uma forma de dicionário de dados da fonte. Essa coluna possui uma breve descrição. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 06 | Preenchimento da Coluna "Diretório Raiz Arquivo" | Essa coluna o local onde o arquivo será disponibilizado no data lake. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 07 | Preenchimento da Coluna "Extensão Arquivo" | Essa coluna identifica qual a extensão do arquivo que deverá ser consumido. Os tipos aceitos são: csv, txt e xlsx | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado.
| Seq 08 | Preenchimento da Coluna "Delimitador" | Essa coluna identificará qual o delimitador de coluna para um arquivo. | Caso a coluna "Extensão Arquivo" esteja preenchida com "csv" ou "txt", essa informação é obrigatória. |
| Seq 09 | Preenchimento da Coluna "Delimitador" | Essa coluna identificará qual o delimitador de coluna para um arquivo. | Caso a coluna "Extensão Arquivo" esteja preenchida com "xlsx" ou "txt", essa coluna não deverá ser preenchida. |
| Seq 10 | Preenchimento da Coluna "Nome Tabela Data Lake" | Essa coluna deverá ser preenchida. Essa coluna identifica o nome da tabela ao qual o dado será persistida no data lake. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 11 | Preenchimento da Coluna "Aba" | Essa coluna identificará qual á e a aba do arquivo do excel (planilha) os dados deverão ser consumidos. | Caso a coluna "Extensão Arquivo" esteja preenchida com "xlsx", essa coluna tem seu preenchimento obrigatório. |
| Seq 12 | Preenchimento da Coluna "Aba" | Essa coluna identificará qual á e a aba do arquivo do excel (planilha) os dados deverão ser consumidos. | Caso a coluna "Extensão Arquivo" esteja preenchida com "csv" ou "txt", não poderá ser preenchida. |
| Seq 13 | Preenchimento da Coluna "Encoding" | Essa coluna identifica a codificação dos dados.  | Caso a coluna "Extensão Arquivo" esteja preenchida com "csv" ou "txt", essa informação é obrigatória. |

### 2.3 - Aba EstruturaFonteDado

| Seq | Etapa | Regra | Descrição |
| ------ |  ------ |  ------ |  ------ |
| Seq 01 | Preenchimento Coluna "Etapa" | Caso esteja assinalado como CADASTRAR, a coluna "Código Projeto" não pode estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 02 | Preenchimento Coluna "Etapa" | Caso esteja assinalado como ATUALIZAR ou EXCLUIR, a coluna "Código Projeto" deverá estar preenchida. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 03 | Preenchimento Coluna "Codigo Projeto" | Essa coluna deverá ser preenchida caso a coluna "Etapa" esteja preenchida com as informações "ALTERAR" ou "EXCLUIR". O valor dessa coluna é gerado no momento do cadastro do projeto. Para identificar qual o código correto do projeto, basta consultar na base de dados. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 04 | Preenchimento Coluna "Codigo Fonte Dado" | Essa coluna deverá ser preenchida apenas caso a coluna "Etapa" esteja preenchida com as informações "ALTERAR" ou "EXCLUIR". O valor dessa coluna é gerado no momento do cadastro da fonte de dado. Para identificar qual o código correto da fonte do dado, basta consultar na base de dados. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 05 | Preenchimento das Colunas "Codigo Projeto" e "Codigo Fonte Dado" | Essas colunas deverão ser preenchida apenas caso a coluna "Etapa" esteja preenchida com as informações "ALTERAR" ou "EXCLUIR". O valor dessa coluna é gerado no momento do cadastro da fonte de dado. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |
| Seq 06 | Preenchimento da Coluna "Nome Fonte de Dado" | Essa coluna deverá ser preenchida com o nome da fonte. Mesma informação usada na coluna "Nome Fonte Dado" da aba FonteDado | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 07 | Preenchimento da coluna "Sequencia Coluna" | Essa coluna identifica a ordem das colunas dentro da tabela. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 08 | Preenchimento da coluna "Sequencia Coluna" | Essa coluna deve ser preenchida com valores numéricos, sequenciais e únicos | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. |  
| Seq 09 | Preenchimento da coluna "Nome da Coluna" | Esse coluna deve ser preenchida com o nome da colunas da tabela. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 10 | Preenchimento da coluna "Tipo de Dado"  | Essa coluna deve conter apenas os valores INT, STRING, DATETIME , NUMERIC. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 11 | Preenchimento da coluna "Flag Coluna Nula" | Essa coluna deverá ser preenchida apenas com valores 0 ou 1. Onde 0 aceita nulo e 1 não aceita nulo. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 12 | Preenchimento da coluna "Flag Coluna Obrigatorio" | Essa coluna deverá ser preenchida apenas com valores 0 ou 1. Onde 0 o preenchimento da coluna no arquivo é obrigatória e 1 não possui preenchimento obrigatório. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 13 | Preenchimento da coluna "Flag Coluna Chave" | Essa coluna deverá ser preenchida apenas com valores 0 ou 1. Onde 0 informa que a coluna faz parte da chave primária e 1 não não faz parte. | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 
| Seq 14 | Preenchimento da coluna "Flag Tipo Dado Armazenado" | Essa coluna é usada para identificar o tipo de dado que é armazenado em cada coluna. Aceita apenas os valores INTEIRO, NUMERIC, STRING, DATA, EMAIL | Caso esteja em desacordo com a regra, o arquivo deverá ser rejeitado. | 

### 3 - Cadastro da Fonte de Dado