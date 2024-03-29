USE [master]
GO
ALTER DATABASE [ADF_UDEMY] SET  SINGLE_USER WITH ROLLBACK IMMEDIATE
GO
USE [master]
GO
DROP DATABASE [ADF_UDEMY]
GO
CREATE DATABASE ADF_UDEMY
GO
USE ADF_UDEMY
GO


CREATE TABLE dbo.TB_FORMA_PAGAMENTO
(
CODIGO_FORMA_PAGAMENTO	 SMALLINT NOT NULL IDENTITY(1,1)
,DESCRICAO_FORMA_PAGAMENTO VARCHAR(100) NOT NULL
)
GO
ALTER TABLE dbo.TB_FORMA_PAGAMENTO ADD CONSTRAINT [PK_TB_FORMA_PAGAMENTO] PRIMARY KEY (CODIGO_FORMA_PAGAMENTO)
GO

CREATE TABLE dbo.TB_CATEGORIA_PRODUTO
(
CODIGO_CATEGORIA SMALLINT NOT NULL IDENTITY(1,1)
,DECRICAO_CATEGORIA VARCHAR(100) NOT NULL
)
GO
ALTER TABLE dbo.TB_CATEGORIA_PRODUTO ADD CONSTRAINT [PK_TB_CATEGORIA_PRODUTO] PRIMARY KEY (CODIGO_CATEGORIA)
GO

CREATE TABLE dbo.TB_PRODUTO
(
CODIGO_PRODUTO	 SMALLINT NOT NULL IDENTITY(1,1)
,DESCRICAO_PRODUTO	 VARCHAR(100) NOT NULL
,CODIGO_CATEGORIA SMALLINT
)
GO
ALTER TABLE dbo.TB_PRODUTO ADD CONSTRAINT [PK_TB_PRODUTO] PRIMARY KEY (CODIGO_PRODUTO)
GO
ALTER TABLE dbo.TB_PRODUTO ADD CONSTRAINT [FK_TB_PRODUTO_CATEGORIA_PRODUTO] FOREIGN KEY (CODIGO_CATEGORIA) REFERENCES dbo.TB_CATEGORIA_PRODUTO (CODIGO_CATEGORIA)
GO
CREATE NONCLUSTERED INDEX [IX_01] ON dbo.TB_PRODUTO(CODIGO_CATEGORIA)
GO

CREATE TABLE dbo.TB_CLIENTE
(
CODIGO_CLIENTE SMALLINT NOT NULL IDENTITY(1,1)
,NOME_CLIENTE VARCHAR(100) NOT NULL
)
GO
ALTER TABLE dbo.TB_CLIENTE ADD CONSTRAINT [PK_TB_CLIENTE] PRIMARY KEY (CODIGO_CLIENTE)
GO

CREATE TABLE dbo.TB_VENDEDOR
(
CODIGO_VENDEDOR SMALLINT NOT NULL IDENTITY(1,1)
,NOME_VENDEDOR VARCHAR(100) NOT NULL
)
GO
ALTER TABLE dbo.TB_VENDEDOR ADD CONSTRAINT [PK_CODIGO_VENDEDOR] PRIMARY KEY (CODIGO_VENDEDOR)
GO

CREATE TABLE dbo.TB_LOJA
(
CODIGO_LOJA	 SMALLINT NOT NULL IDENTITY(1,1)
,NOME_LOJA	 VARCHAR(100) NOT NULL
,LOCALIDADE_LOJA	 VARCHAR(100) NOT NULL
,TIPO_LOJA VARCHAR(100) NOT NULL
)
GO
ALTER TABLE dbo.TB_LOJA ADD CONSTRAINT [PK_TB_LOJA] PRIMARY KEY (CODIGO_LOJA)
GO

CREATE TABLE dbo.TB_VENDA
(
CODIGO_VENDA SMALLINT NOT NULL IDENTITY(1,1)	
,DATA_VENDA	DATETIME NOT NULL 
,CODIGO_CLIENTE	SMALLINT
,CODIGO_VENDEDOR	SMALLINT
,CODIGO_LOJA	SMALLINT
,VALOR_FINAL DECIMAL(18,2)	
,FORMA_PAGAMENTO	SMALLINT
,TIPO_PAGAMENTO VARCHAR(100) NOT NULL
)
GO

ALTER TABLE dbo.TB_VENDA ADD CONSTRAINT [PK_TB_VENDA] PRIMARY KEY (CODIGO_VENDA)
GO
ALTER TABLE dbo.TB_VENDA ADD CONSTRAINT [FK_TB_VENDA_CLIENTE] FOREIGN KEY (CODIGO_CLIENTE) REFERENCES dbo.TB_CLIENTE (CODIGO_CLIENTE)
GO
ALTER TABLE dbo.TB_VENDA ADD CONSTRAINT [FK_TB_VENDA_FORMA_PAGAMENTO] FOREIGN KEY (FORMA_PAGAMENTO) REFERENCES dbo.TB_FORMA_PAGAMENTO (CODIGO_FORMA_PAGAMENTO)
GO
ALTER TABLE dbo.TB_VENDA ADD CONSTRAINT [FK_TB_VENDA_VENDEDOR] FOREIGN KEY (CODIGO_VENDEDOR) REFERENCES dbo.TB_VENDEDOR (CODIGO_VENDEDOR)
GO
ALTER TABLE dbo.TB_VENDA ADD CONSTRAINT [FK_TB_VENDA_LOJA] FOREIGN KEY (CODIGO_LOJA) REFERENCES dbo.TB_LOJA (CODIGO_LOJA)
GO

CREATE NONCLUSTERED INDEX [IX_01] ON dbo.TB_VENDA(CODIGO_CLIENTE)
GO
CREATE NONCLUSTERED INDEX [IX_02] ON dbo.TB_VENDA(FORMA_PAGAMENTO)
GO
CREATE NONCLUSTERED INDEX [IX_03] ON dbo.TB_VENDA(CODIGO_VENDEDOR)
GO
CREATE NONCLUSTERED INDEX [IX_04] ON dbo.TB_VENDA(CODIGO_LOJA)
GO


CREATE TABLE dbo.TB_ITEM_VENDA
(
CODIGO_VENDA SMALLINT NOT NULL 
,CODIGO_PRODUTO	SMALLINT NOT NULL 
,VALOR_UNITARIO DECIMAL(18,2)	
,QUANTIDADE	SMALLINT
,VALOR_FINAL DECIMAL(18,2)
)
GO

ALTER TABLE dbo.TB_ITEM_VENDA ADD CONSTRAINT [PK_TB_ITEM_VENDA] PRIMARY KEY (CODIGO_VENDA,CODIGO_PRODUTO)
GO
ALTER TABLE dbo.TB_ITEM_VENDA ADD CONSTRAINT [FK_TB_VENDA_ITEM_VENDA] FOREIGN KEY (CODIGO_VENDA) REFERENCES dbo.TB_VENDA (CODIGO_VENDA)
GO
ALTER TABLE dbo.TB_ITEM_VENDA ADD CONSTRAINT [FK_TB_ITEM_VENDA_PRODUTO] FOREIGN KEY (CODIGO_PRODUTO) REFERENCES dbo.TB_PRODUTO (CODIGO_PRODUTO)
GO

CREATE NONCLUSTERED INDEX [IX_01] ON dbo.TB_ITEM_VENDA(CODIGO_VENDA)
GO
CREATE NONCLUSTERED INDEX [IX_02] ON dbo.TB_ITEM_VENDA(CODIGO_PRODUTO)
GO