# cdc-pipeline-project
#  Change Data Capture (CDC) Pipeline with Azure Data Factory and Databricks

This project implements a real-time, scalable **Change Data Capture (CDC)** pipeline using **Azure Data Factory**, **Azure Databricks**, and **SQL Server**. It captures data changes (inserts, updates, deletes) from source tables and reflects them efficiently into the **Azure Data Lake Storage (ADLS)** using **Delta Lake** and Apache Spark.

---

##  Tech Stack

- Microsoft SQL Server (on-prem/local)
- Azure Data Factory (ADF)
- Azure Databricks (Delta Lake + Spark)
- Azure Data Lake Storage Gen2 (ADLS)
- JDBC, Spark, Delta Tables
- GitHub for version control

---

## 🎯 Project Objectives

- Build a near real-time data ingestion pipeline.
- Capture and reflect changes from SQL Server source tables (CDC).
- Use Apache Spark with Databricks for efficient Delta Lake updates.
- Ensure high performance and data consistency with minimal latency.
- Schedule hourly ETL jobs.
- Notify stakeholders via email on successful job execution.

---

## 📁 Source Tables

The following source tables are created in SQL Server:

| Table     | Description |
|-----------|-------------|
| `Customer` | Customer ID, Name, Email, Phone, Address |
| `Product`  | Product ID, Name, Price, Description, Category |
| `Order`    | Order ID, Customer ID, Product ID, Date, Quantity, Amount |
| `Inventory`| Product ID, Quantity, Location |

Each table has **20 sample records** inserted for testing the pipeline.

---

## 🛠️ Implementation Steps

###  Step 1: Create Source Tables in SQL Server

- Tables: `Customer`, `Product`, `Order`, `Inventory`
- Insert sample data (20 rows each)
- Enable remote connection + TCP/IP for JDBC access

###  Step 2: Connect SQL Server to Azure Data Factory (ADF)

- Create a **Linked Service** in ADF to connect to on-prem SQL Server
- Use **Self-hosted Integration Runtime (SHIR)** for secure local connectivity

###  Step 3: Build ADF Pipeline

- **Copy Activity**: Load data from SQL Server to ADLS (raw zone)
- **Databricks Notebook Activity**: Execute CDC logic using Delta Lake
- Add **dynamic parameters** for table names and filenames

###  Step 4: Implement CDC Logic in Databricks

- CDC implemented via **Delta Lake `MERGE` statements**
- Compare raw data vs. processed Delta tables
- Handle inserts, updates, deletes

###  Step 5: Schedule Execution + Notification

- Trigger the ADF pipeline to run **every 1 hour**
- On success, **send email notification** with updated table status (via Logic App or Databricks)

---
