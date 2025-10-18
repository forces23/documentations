# **Amazon Athena**

---

## 1. **What is Amazon Athena?**

Amazon Athena is a **serverless, interactive query service** that lets you  **analyze data directly in S3 using SQL** .

* No servers to manage.
* Pay only for the data you query.
* Great for  **ad hoc analysis, reporting, and big data exploration** .

👉 Think of Athena as **“SQL on top of S3.”**

---

## 2. **Why Athena?**

Traditional data warehouses require:

* Loading data into DB → extra cost & time.
* Infrastructure scaling → admin work.

Athena solves this by:

* Querying  **directly on S3** .
* Scaling automatically.
* Using **Presto/Trino engine** (distributed SQL query engine).

---

## 3. **Core Features**

1. **Serverless**
   * No provisioning of clusters.
   * Fully managed by AWS.
2. **Standard SQL**
   * Queries written in ANSI SQL.
   * Easy for analysts/developers who already know SQL.
3. **Schema-on-Read**
   * Data doesn’t need to be structured when stored.
   * Schema applied at query time.
4. **Wide Format Support**
   * CSV, JSON, ORC, Avro, Parquet.
   * Works best with **columnar formats like Parquet/ORC** (cheaper + faster).
5. **Integrates with AWS Services**
   * **S3** → raw data.
   * **Glue Data Catalog** → metadata/schema management.
   * **QuickSight** → dashboards.
   * **CloudTrail logs** → audit queries.

---

## 4. **How Athena Works**

1. Data lands in **S3** (raw logs, CSV, JSON, Parquet).
2. You define a **table schema** in Athena (or Glue).
3. Run SQL queries on that table.
4. Athena reads only the relevant data → returns results.
5. You can export results to S3, Power BI, or QuickSight.

---

## 5. **Architecture Example**

### Insurance Company Workflow

1. Call center logs stream into  **S3** .
2. **Glue Crawler** detects schema + updates Data Catalog.
3. Analysts query the data using  **Athena** :
   ```sql
   SELECT claim_id, AVG(payout) 
   FROM insurance_claims 
   WHERE claim_type = 'Auto' 
   GROUP BY claim_id;
   ```
4. Results visualized in **QuickSight** or  **Power BI** .

---

## 6. **Use Cases**

* **Ad hoc queries** : “What’s the average claim amount this month?”
* **Log analysis** : Query **CloudTrail, ELB, or VPC Flow logs** in S3.
* **Data lake exploration** : Part of a **Lakehouse architecture** with S3 + Glue + Redshift.
* **Business reporting** : Athena → QuickSight dashboards.
* **ETL pipelines** : Transform S3 data into structured formats.

---

## 7. **Performance Best Practices**

1. **Partition Data** in S3 (e.g., by date, region):

   ```bash
   s3://claims-data/year=2025/month=10/day=04/
   ```

   Query only scans relevant partitions.
2. **Use Columnar Formats (Parquet/ORC)** → reduces scanned data.
3. **Compress Data** (Snappy, GZIP, Zstd).
4. **Optimize Schema** → avoid too many small files (“small file problem”).

---

## 8. **Security in Athena**

* 🔑 **IAM Policies** → restrict who can run queries.
* 🔒 **S3 Bucket Policies** → secure underlying data.
* 🔑 **KMS Encryption** → encrypt S3 data at rest.
* 🔒 **Athena Query Results** → always written to S3 (make sure result bucket is secure).
* 🕵️ **CloudTrail Integration** → log who ran which query.

---

## 9. **Pricing**

* Charged  **per TB of data scanned** .
* Example: $5 per TB scanned.
* Reduce costs with:
  * Columnar formats.
  * Compression.
  * Partitioning.

👉 If you query a 100GB dataset but only scan 10GB (via partitioning), you’re billed only for 10GB.

---

## 10. **Hands-On Example**

### Dataset: Insurance Claims in S3 (CSV)

```bash
claim_id,customer,amount,type,date
123,John Doe,2500,Auto,2025-09-01
124,Jane Smith,1500,Health,2025-09-02
125,Mike Ross,3200,Auto,2025-09-02
```

### Create Table

```sql
CREATE EXTERNAL TABLE insurance_claims (
  claim_id INT,
  customer STRING,
  amount DOUBLE,
  type STRING,
  date STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
LOCATION 's3://insurance-data/claims/';
```

### Query Example

```sql
SELECT type, AVG(amount) as avg_claim
FROM insurance_claims
GROUP BY type;
```

**Result:**

| type   | avg_claim |
| ------ | --------- |
| Auto   | 2850      |
| Health | 1500      |

---

## 11. **Athena vs Redshift**

| Feature     | Athena                         | Redshift                                |
| ----------- | ------------------------------ | --------------------------------------- |
| Use Case    | Ad hoc queries, S3 data lakes  | Data warehouse, complex analytics       |
| Infra       | Serverless                     | Cluster-based                           |
| Pricing     | Pay per query (per TB scanned) | Pay per hour/instance                   |
| Performance | Depends on data format         | Optimized for heavy joins, BI workloads |
| Best For    | Log analysis, quick reporting  | Enterprise-scale analytics              |

👉 Many companies use **Athena + Redshift Spectrum** together.

---

## 12. **Quick Recap**

* **Athena = serverless SQL on S3** .
* Integrates with **Glue** (schema), **QuickSight** (visualization).
* Great for  **ad hoc queries, log analysis, reporting** .
* **Best practices** : partitioning, Parquet, compression.
* **Security** : IAM, KMS, CloudTrail, S3 policies.
* **Cost** : $5/TB scanned → optimize data to reduce cost.

---

✅  **Analogy** :

Athena is like **Google Search for your S3 data** — you don’t move the data; you just query it where it lives.
