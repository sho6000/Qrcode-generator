# Sunbird Deployment via GitHub Actions — A Simple Guide

This guide explains how we deploy Sunbird on Azure using two GitHub Actions workflows. Think of it as a two-step process: first you set up the infrastructure (the servers/cluster), then you deploy the actual services on top of it.

---

## The Big Picture

```
Step 1: Create Infrastructure  →  Step 2: Deploy Services
   (infra.yaml)                      (deploy.yaml)
```

Both workflows live in the **private config repo** (`spark-devops-sandbox`). They pull the actual installer code from the **public repo** (`sunbird-spark-installer`) at runtime.

---

## Step 1 — Create the AKS Cluster (`infra.yaml`)

> **When to use:** Only once, when setting up a new environment. Once the cluster exists, skip this.

### How to trigger it

Go to the repo on GitHub → **Actions** → **"Create Infrastructure (AKS)"** → **Run workflow**

### Inputs you fill in

| Input | What it means | Default |
|---|---|---|
| `environment` | Which environment to deploy to (e.g. `sandbox`) | `sandbox` |
| `config_branch` | Branch of the config repo to use | `sandbox` |
| `source_branch` | Branch of the installer repo to use | `sandbox` |
| `create_cluster` | Tick this to actually create the AKS cluster | `true` |

### What happens behind the scenes

1. Checks out your private config repo (has your `global-values.yaml` with domain, creds, etc.)
2. Clones the public `sunbird-spark-installer` repo
3. Logs into Azure using OIDC (no passwords stored — secure token exchange)
4. Decrypts your config files (they're stored encrypted using Ansible Vault)
5. If the AKS cluster doesn't already exist → creates it (takes ~10-15 mins)
6. Encrypts the updated configs and commits them back to the config repo

> **Note:** After this step, your configs folder in the private repo will have an updated `global-cloud-values.yaml` with things like storage keys, cluster endpoints, etc. — all encrypted.

---

## Step 2 — Deploy Services (`deploy.yaml`)

> **When to use:** Every time you want to deploy or update services on the cluster.

### How to trigger it

Go to the repo on GitHub → **Actions** → **"Deploy Sunbird to AKS"** → **Run workflow**

### Inputs you fill in

| Input | What it means |
|---|---|
| `environment` | Which environment (e.g. `sandbox`) |
| `source_branch` | Which branch of the installer to use |
| `installation_mode` | `full` (everything) or `selective` (you pick what runs) |

---

### The 3 Ways to Deploy

#### Option A — Deploy Everything at Once (`full` mode)

Set `installation_mode` to `full`. That's it. It will deploy all building blocks in order:

```
monitoring → edbb → learnbb → knowledgebb → obsrvbb → additional
```

Then it runs post-install steps: certificate config, DNS wait, Postman validation.

---

#### Option B — Deploy Specific Building Blocks (`selective` mode)

Set `installation_mode` to `selective`, then tick only the building blocks you want:

| Checkbox | What it deploys |
|---|---|
| `Monitoring` | Prometheus, Grafana, Loki |
| `edbb` | Kong, NGINX, Kafka, Player portal |
| `learnbb` | Keycloak, YugabyteDB, Redis, Elasticsearch, Flink, Lern |
| `knowledgebb` | Knowlg, Search, JanusGraph, Flink |
| `obsrvbb` | Telemetry, Superset |
| `additional` | cert-ng, NL web, volume autoscaler |

You can also tick the post-install steps individually:

| Checkbox | What it does |
|---|---|
| Restart workloads | Rolls out deployments to pick up new certs/keys |
| Configure certificate keys | Injects RSA keys into the registry service |
| Wait for DNS mapping | Polls until DNS propagates (up to 20 min) |
| Generate Postman environment | Creates `env.json` for API tests |
| Run post-install scripts | Runs Postman collection to validate APIs |
| Create client forms | Sets up ED forms/collections |

---

#### Option C — Deploy a Single Service Inside a Building Block

This is the fastest option when you just want to update one service (e.g. redeploy only `lern` inside `learnbb`).

In `selective` mode, tick `Install Helm components` and fill in:

| Field | Example |
|---|---|
| `service_bundle` | `learnbb` |
| `service_chart` | `lern` |

Or to deploy multiple services in one shot:

| Field | Example |
|---|---|
| `service_bundle` | `learnbb` |
| `service_chart` | `lern keycloak flink` |

---

### Bonus — Upgrade a Service Image Tag

If you just want to push a new Docker image for a service without redeploying anything else, tick `Upgrade independent service` and fill in:

| Field | Example |
|---|---|
| `upgrade_service_component` | `edbb` |
| `upgrade_service_image_key` | `images.player.tag` |
| `upgrade_service_image_tag` | `v1.2.3` |

There's also a shortcut specifically for the Player service — if you're deploying `edbb`, you can fill in the `Player image tag` field directly.

---

## Summary — What to Run When

| Scenario | Workflow | What to pick |
|---|---|---|
| First-time environment setup | `infra.yaml` | Tick `create_cluster` |
| Deploy everything fresh | `deploy.yaml` | Mode: `full` |
| Deploy one building block (e.g. learnbb) | `deploy.yaml` | Mode: `selective`, tick `learnbb` |
| Deploy one service (e.g. lern inside learnbb) | `deploy.yaml` | Mode: `selective`, tick `Install Helm components`, set bundle=`learnbb` chart=`lern` |
| Push a new image for a service | `deploy.yaml` | Tick `Upgrade independent service`, fill in component/image key/tag |
| Re-run post-install steps only | `deploy.yaml` | Mode: `selective`, tick only the steps you need |

---

## A Few Things to Know

- **Config files are encrypted:** `global-values.yaml` and `global-cloud-values.yaml` in the config repo are encrypted with Ansible Vault. The workflow decrypts them at runtime using a secret — you never see raw credentials.
- **Two repos involved:** The config repo (private, has your environment-specific values) and the installer repo (public, has the Helm charts and install scripts). The workflow always fetches the installer fresh at runtime.
- **Concurrency lock:** Only one deploy can run at a time. If someone else is deploying, yours will queue up — it won't cancel theirs.
