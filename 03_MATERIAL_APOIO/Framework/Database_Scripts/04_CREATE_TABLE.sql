USE [DQ]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_FONTE_DADO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_FONTE_DADO] DROP CONSTRAINT IF EXISTS [FK_TB_FONTE_DADO_TB_PROJETO]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_ESTRUTURA_FONTE_DADO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO] DROP CONSTRAINT IF EXISTS [FK_TB_ESTRUTURA_FONTE_DADO_TB_FONTE_DADO]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_PROJETO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_PROJETO] DROP CONSTRAINT IF EXISTS [DF__TB_PROJET__DthAl__24927208]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_PROJETO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_PROJETO] DROP CONSTRAINT IF EXISTS [DF__TB_PROJET__DthIn__239E4DCF]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_LOG]') AND type in (N'U'))
ALTER TABLE [dq].[TB_LOG] DROP CONSTRAINT IF EXISTS [DF__TB_LOG__DthInclu__30F848ED]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_FONTE_DADO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_FONTE_DADO] DROP CONSTRAINT IF EXISTS [DF__TB_FONTE___DthAl__286302EC]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_FONTE_DADO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_FONTE_DADO] DROP CONSTRAINT IF EXISTS [DF__TB_FONTE___DthIn__276EDEB3]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_ESTRUTURA_FONTE_DADO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO] DROP CONSTRAINT IF EXISTS [DF__TB_ESTRUT__DthAl__2D27B809]
GO
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[dq].[TB_ESTRUTURA_FONTE_DADO]') AND type in (N'U'))
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO] DROP CONSTRAINT IF EXISTS [DF__TB_ESTRUT__DthIn__2C3393D0]
GO
/****** Object:  Table [dq].[TB_PROJETO]    Script Date: 24/02/2024 11:07:37 ******/
DROP TABLE IF EXISTS [dq].[TB_PROJETO]
GO
/****** Object:  Table [dq].[TB_LOG]    Script Date: 24/02/2024 11:07:37 ******/
DROP TABLE IF EXISTS [dq].[TB_LOG]
GO
/****** Object:  Table [dq].[TB_FONTE_DADO]    Script Date: 24/02/2024 11:07:37 ******/
DROP TABLE IF EXISTS [dq].[TB_FONTE_DADO]
GO
/****** Object:  Table [dq].[TB_ESTRUTURA_FONTE_DADO]    Script Date: 24/02/2024 11:07:37 ******/
DROP TABLE IF EXISTS [dq].[TB_ESTRUTURA_FONTE_DADO]
GO
/****** Object:  Table [dq].[TB_ESTRUTURA_FONTE_DADO]    Script Date: 24/02/2024 11:07:37 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dq].[TB_ESTRUTURA_FONTE_DADO](
	[IdEstruturaFonteDados] [int] IDENTITY(1,1) NOT NULL,
	[IdFonteDados] [int] NOT NULL,
	[IdProjeto] [int] NOT NULL,
	[NomFonteDados] [varchar](200) NULL,
	[NomColuna] [varchar](200) NULL,
	[TpoDado] [varchar](200) NULL,
	[NumCasasDecimais] [varchar](200) NULL,
	[FlagColunaNula] [int] NULL,
	[NumTamanhoMaximo] [int] NULL,
	[FlagColunaObrigatoria] [int] NULL,
	[FlagDadoSensivel] [int] NULL,
	[NumSeqColunaTabela] [int] NULL,
	[DscUltimaAcao] [varchar](100) NULL,
	[DthInclusao] [datetime] NOT NULL,
	[DthAlteracao] [datetime] NOT NULL,
 CONSTRAINT [PK_TB_ESTRUTURA_FONTE_DADO] PRIMARY KEY CLUSTERED 
(
	[IdEstruturaFonteDados] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dq].[TB_FONTE_DADO]    Script Date: 24/02/2024 11:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dq].[TB_FONTE_DADO](
	[IdFonteDados] [int] IDENTITY(1,1) NOT NULL,
	[IdProjeto] [int] NOT NULL,
	[NomFonteDados] [varchar](200) NULL,
	[DscFonteDados] [varchar](2000) NULL,
	[DataLakeFolder] [varchar](2000) NULL,
	[DscExtensaoArquivo] [varchar](20) NULL,
	[TpoDelimitadorArquivo] [varchar](20) NULL,
	[NomTabela] [varchar](200) NULL,
	[NomAbaExcel] [varchar](200) NULL,
	[PathBronzeDestination] [varchar](2000) NULL,
	[NomEncodingArquivo] [varchar](2000) NULL,
	[DscUltimaAcao] [varchar](100) NULL,
	[DthInclusao] [datetime] NOT NULL,
	[DthAlteracao] [datetime] NOT NULL,
 CONSTRAINT [PK_TB_FONTE_DADO] PRIMARY KEY CLUSTERED 
(
	[IdFonteDados] ASC,
	[IdProjeto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dq].[TB_LOG]    Script Date: 24/02/2024 11:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dq].[TB_LOG](
	[IdLog] [int] IDENTITY(1,1) NOT NULL,
	[NomArquivoProcessado] [varchar](1000) NULL,
	[NomProjeto] [varchar](1000) NULL,
	[NomFonteDado] [varchar](1000) NULL,
	[NomEtapa] [varchar](1000) NULL,
	[DscMsgProcessamento] [varchar](2000) NULL,
	[NomStatus] [varchar](1) NULL,
	[DthInclusao] [datetime] NOT NULL,
 CONSTRAINT [PK_TB_LOG] PRIMARY KEY CLUSTERED 
(
	[IdLog] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dq].[TB_PROJETO]    Script Date: 24/02/2024 11:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dq].[TB_PROJETO](
	[IdProjeto] [int] IDENTITY(1,1) NOT NULL,
	[NomCategoriaProjeto] [varchar](200) NULL,
	[NomProjeto] [varchar](200) NULL,
	[NumMaxIteracoes] [int] NULL,
	[NomRespProjeto] [varchar](200) NULL,
	[NomRespTecnico] [varchar](200) NULL,
	[DscUltimaAcao] [varchar](100) NULL,
	[DthInclusao] [datetime] NOT NULL,
	[DthAlteracao] [datetime] NOT NULL,
 CONSTRAINT [PK_TB_PROJETO] PRIMARY KEY CLUSTERED 
(
	[IdProjeto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO] ADD  DEFAULT (getdate()) FOR [DthInclusao]
GO
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO] ADD  DEFAULT (getdate()) FOR [DthAlteracao]
GO
ALTER TABLE [dq].[TB_FONTE_DADO] ADD  DEFAULT (getdate()) FOR [DthInclusao]
GO
ALTER TABLE [dq].[TB_FONTE_DADO] ADD  DEFAULT (getdate()) FOR [DthAlteracao]
GO
ALTER TABLE [dq].[TB_LOG] ADD  DEFAULT (getdate()) FOR [DthInclusao]
GO
ALTER TABLE [dq].[TB_PROJETO] ADD  DEFAULT (getdate()) FOR [DthInclusao]
GO
ALTER TABLE [dq].[TB_PROJETO] ADD  DEFAULT (getdate()) FOR [DthAlteracao]
GO
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO]  WITH CHECK ADD  CONSTRAINT [FK_TB_ESTRUTURA_FONTE_DADO_TB_FONTE_DADO] FOREIGN KEY([IdFonteDados], [IdProjeto])
REFERENCES [dq].[TB_FONTE_DADO] ([IdFonteDados], [IdProjeto])
GO
ALTER TABLE [dq].[TB_ESTRUTURA_FONTE_DADO] CHECK CONSTRAINT [FK_TB_ESTRUTURA_FONTE_DADO_TB_FONTE_DADO]
GO
ALTER TABLE [dq].[TB_FONTE_DADO]  WITH CHECK ADD  CONSTRAINT [FK_TB_FONTE_DADO_TB_PROJETO] FOREIGN KEY([IdProjeto])
REFERENCES [dq].[TB_PROJETO] ([IdProjeto])
GO
ALTER TABLE [dq].[TB_FONTE_DADO] CHECK CONSTRAINT [FK_TB_FONTE_DADO_TB_PROJETO]
GO
