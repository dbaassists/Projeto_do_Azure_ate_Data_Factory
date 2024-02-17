-- CRIA�AO DO BANCO DE DADOS MONITORAMENTO
CREATE DATABASE MONITORAMENTO
GO

-- SELECIONA O BANCO DE DADOS MONITORAMENTO
USE MONITORAMENTO
GO

-- CRIA��O DO SCHEMA PARA OS OBJETOS DE LOG
CREATE SCHEMA sch_log
GO

-- CRIA��O DA TABELA QUE IR� RECEBER AS INFORMA��ES DE EXECU��O DAS PIPELINES
DROP TABLE IF EXISTS sch_log.tb_log_pipeline
GO
CREATE TABLE sch_log.tb_log_pipeline (
id_log					INT NOT NULL IDENTITY(1,1)
,pipeline_run_id		VARCHAR(100)
,triggered_by_run_id	VARCHAR(100)
,trigger_name			VARCHAR(100)
,pipeline_name			VARCHAR(100)
,ds_status				VARCHAR(100)
,dt_inicio				VARCHAR(100) NOT NULL DEFAULT GETDATE()
,dt_fim					VARCHAR(100)
)
GO

-- CRIA��O DA PROCEDURE QUE SER� RESPONS�VEL POR REGISTRAR AS A��ES
DROP PROCEDURE IF EXISTS sch_log.SP_LOG_PIPELINE
GO
CREATE PROCEDURE sch_log.SP_LOG_PIPELINE
@pipeline_run_id		VARCHAR(100)
,@triggered_by_run_id	VARCHAR(100)
,@trigger_name			VARCHAR(100)
,@pipeline_name			VARCHAR(100)
AS
BEGIN 

	INSERT INTO sch_log.tb_log_pipeline
	(pipeline_run_id
	,triggered_by_run_id
	,trigger_name
	,pipeline_name
	,ds_status)
	VALUES 
	(@pipeline_run_id
	,@triggered_by_run_id
	,@trigger_name
	,@pipeline_name
	,'Processando')

END