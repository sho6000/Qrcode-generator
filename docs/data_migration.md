#  Data Migration

**A step-by-step guide to migrating data from your existing Sunbird cluster to the new Sunbird Spark setup.**



## Overview

This migration moves data from an existing Sunbird installation running on legacy databases to the new Sunbird Spark cluster. The new cluster runs on a different database stack — YugabyteDB replaces both Cassandra and PostgreSQL, and JanusGraph replaces Neo4j.

| From (old cluster) | To (new cluster) |
|--------------------|-----------------|
| PostgreSQL | YugabyteDB (YSQL) |
| Cassandra | YugabyteDB (YCQL) |
| Neo4j | JanusGraph |
| Elasticsearch | Elasticsearch |

Migration is handled by a Helm chart that runs Kubernetes Jobs. Each migration is a separate job that must be run **one at a time** — never simultaneously. This ensures data integrity and makes it easier to isolate issues if something goes wrong.

> [!CAUTION]
> Always verify data after each migration step before moving to the next. Migrating multiple databases simultaneously can cause resource conflicts and data loss.

---

## Before You Begin

Make sure the following are in place before starting any migration:

- ✅ The new Sunbird Spark cluster is fully installed and all core services are running
- ✅ The old cluster's databases are **network-reachable** from inside the new Kubernetes cluster
- ✅ `kubectl` is configured and connected to the new cluster
- ✅ `helm` 3.x is installed
- ✅ You have the IP addresses of the old cluster's databases

### Configure `values.yaml`

Before running any migration, open `migration/db-migration/values.yaml` and fill in the source host IPs from your old cluster:

**PostgreSQL source:**
```yaml
postgres:
  host: "<old-postgresql-ip>"
  port: 5432
  username: "postgres"
  password: "<your-password>"
  databases:
    - keycloak
    - registry
```

**Cassandra source:**
```yaml
cassandra:
  host: "<old-cassandra-ip>"
  port: 9042
```

**Neo4j source:**
```yaml
neo4j:
  host: "<old-neo4j-ip>"
  port: 7687
  username: "neo4j"
  password: "<your-password>"
```

**Elasticsearch source:**
```yaml
elasticsearchMigration:
  oldEsHost: "http://<old-elasticsearch-ip>:9200"
  newEsHost: "http://elasticsearch.sunbird.svc.cluster.local:9200"
```

> [!NOTE]
> All jobs are disabled by default in `values.yaml`. You enable each job only when you are ready to run that specific migration.

---

## Migration Order

Run migrations strictly in this order. Do not proceed to the next step until the current one has completed successfully and data has been verified.

```
Step 1 — PostgreSQL → YugabyteDB
            ↓  verify
Step 2 — Cassandra → YugabyteDB
            ↓  verify
Step 3 — Neo4j → JanusGraph
            ↓  verify
Step 4 — Elasticsearch → Elasticsearch
```

---

## Step 1 — PostgreSQL → YugabyteDB

Migrates the `keycloak` and `registry` databases from PostgreSQL to YugabyteDB's PostgreSQL-compatible YSQL interface.

### Enable the job

In `values.yaml`, enable only the PostgreSQL job:

```yaml
jobs:
  postgres:
    enabled: true
  cassandra:
    enabled: false
  neo4j:
    enabled: false
  elasticsearch:
    enabled: false
  createdat:
    enabled: false
```

### Run the migration

```bash
helm upgrade --install db-migration ./migration/db-migration \
  -n sunbird \
  -f ./migration/db-migration/values.yaml
```

### Verify

Check the job completed successfully:

```bash
kubectl get jobs -n sunbird
kubectl logs -n sunbird -l app=migration -f
```

Confirm the databases are accessible in YugabyteDB before proceeding.

---

## Step 2 — Cassandra → YugabyteDB

Migrates all Cassandra keyspaces to YugabyteDB's Cassandra-compatible YCQL interface.

The following keyspaces are migrated:

- `sunbird`
- `sunbird_courses`
- `sb_content_store`
- `sb_hierarchy_store`
- `sb_dialcode_store`
- `sb_question_store`
- `sunbird_notifications`
- `sb_category_store`
- `dialcodes`
- and others defined in `values.yaml`

### Enable the job

In `values.yaml`, disable the previous job and enable only Cassandra:

```yaml
jobs:
  postgres:
    enabled: false
  cassandra:
    enabled: true
  neo4j:
    enabled: false
  elasticsearch:
    enabled: false
  createdat:
    enabled: false
```

### Run the migration

```bash
helm upgrade --install db-migration ./migration/db-migration \
  -n sunbird \
  -f ./migration/db-migration/values.yaml
```

### Verify

```bash
kubectl get jobs -n sunbird
kubectl logs -n sunbird -l app=migration -f
```

Confirm all keyspaces are present and accessible in YugabyteDB before proceeding.

---

## Step 3 — Neo4j → JanusGraph

Migrates all graph nodes and relationships from Neo4j to JanusGraph. The migration script exports data from Neo4j to CSV, copies the files into the JanusGraph pod, and imports them via a Gremlin script.

### Enable the job

```yaml
jobs:
  postgres:
    enabled: false
  cassandra:
    enabled: false
  neo4j:
    enabled: true
  elasticsearch:
    enabled: false
  createdat:
    enabled: false
```

### Run the migration

```bash
helm upgrade --install db-migration ./migration/db-migration \
  -n sunbird \
  -f ./migration/db-migration/values.yaml
```

### Verify

```bash
kubectl get jobs -n sunbird
kubectl logs -n sunbird -l app=migration -f
```

Confirm node and edge counts in JanusGraph match the source Neo4j data before proceeding.

---

## Step 4 — Elasticsearch → Elasticsearch

Migrates all indices from the old Elasticsearch cluster to the new one running inside the Sunbird Spark cluster using Elasticsearch's reindex API.

> [!IMPORTANT]
> Before running this migration, you must add `reindex.remote.whitelist` to `elasticsearch.yml` in the learnbb Helm values. Without this, the reindex API will not be permitted to reach the old cluster.

### Enable the job

```yaml
jobs:
  postgres:
    enabled: false
  cassandra:
    enabled: false
  neo4j:
    enabled: false
  elasticsearch:
    enabled: true
  createdat:
    enabled: false
```

### Run the migration

```bash
helm upgrade --install db-migration ./migration/db-migration \
  -n sunbird \
  -f ./migration/db-migration/values.yaml
```

### Verify

```bash
kubectl get jobs -n sunbird
kubectl logs -n sunbird -l app=migration -f
```

Confirm all indices and document counts match between old and new Elasticsearch.

---

## createdat Backfill

> [!NOTE]
> This is a **separate operation** and is not part of the migration sequence above. It adds a new `createdat` column to Elasticsearch by backfilling user timestamps from YugabyteDB.

Run this independently after all migrations are complete and verified:

```yaml
jobs:
  postgres:
    enabled: false
  cassandra:
    enabled: false
  neo4j:
    enabled: false
  elasticsearch:
    enabled: false
  createdat:
    enabled: true
```

```bash
helm upgrade --install db-migration ./migration/db-migration \
  -n sunbird \
  -f ./migration/db-migration/values.yaml
```

---

## Monitoring Logs

To watch live logs for any running migration job:

```bash
kubectl logs -n sunbird -l app=migration -f
```

To check the status of all migration jobs:

```bash
kubectl get jobs -n sunbird
```

---

## Important Notes

- **Run one job at a time.** Enabling multiple jobs simultaneously risks resource conflicts and data corruption.
- **Jobs are idempotent.** If a job fails halfway, it is safe to re-run.
- **Logs are retained for 7 days** after job completion.
- **The old cluster must remain running** and network-accessible throughout the entire migration process.
- **Do not shut down the old cluster** until all migrations are verified and the new cluster is confirmed stable.