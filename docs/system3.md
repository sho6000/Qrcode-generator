<div align="center">

# ⚙️ System Requirements

**Sunbird-ED is deployed entirely on cloud infrastructure.**
Before running the installer, make sure your cloud environment is provisioned and ready.

[![Azure](https://img.shields.io/badge/Azure-Verified-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)](https://azure.microsoft.com)
[![AWS](https://img.shields.io/badge/AWS-Supported-FF9900?style=flat-square&logo=amazonaws&logoColor=white)](https://aws.amazon.com)
[![GCP](https://img.shields.io/badge/GCP-Supported-4285F4?style=flat-square&logo=googlecloud&logoColor=white)](https://cloud.google.com)

</div>

---

## Table of Contents

- [Minimum Requirements](#minimum-requirements)
- [Recommended Requirements](#recommended-requirements)
- [Requirements with Add-ons Enabled](#requirements-with-add-ons-enabled)

---

## Minimum Requirements

Sunbird-ED runs on a **two-node Kubernetes cluster**. The installer sets everything up automatically — you just need the nodes ready on your cloud provider.

### Supported Cloud Providers

| Provider | Status | Notes |
|----------|--------|-------|
| **Microsoft Azure** | ✅ Reference platform | Tested and verified with the installer |
| **Amazon Web Services** | ✅ Supported | Provision equivalent VM types to the Azure reference |
| **Google Cloud Platform** | ✅ Supported | Provision equivalent VM types to the Azure reference |

### Node Specification

Each node should meet the following specification. **Both nodes must be identical.**

| Specification | Requirement |
|---------------|-------------|
| VM type (Azure) | `Standard_B16as_v2` |
| vCPU per node | 16 vCPU |
| RAM per node | 64 GB |

> [!NOTE]
> Using AWS or GCP? Provision VM types that match or exceed 16 vCPU and 64 GB RAM per node. Azure is the reference platform for verified specs — the installer works on any cloud.

### Databases

All databases are **installed and managed automatically** within the cluster. No external database setup is required.

| Database | Purpose |
|----------|---------|
| **YugabyteDB** | Primary distributed database for all platform data |
| **Elasticsearch** | Powers content search and discovery across the platform |
| **JanusGraph** | Graph database for knowledge and content relationships |
| **Redis** | Optional caching layer — disabled by default |

### What Else Runs on the Cluster

Beyond databases, the cluster also runs the following:

| Component | Description |
|-----------|-------------|
| **Background processors** | Handles certificate generation, notifications, and event processing |
| **Application services** | The APIs and web portals that users and admins interact with |
| **Monitoring stack** | Dashboards and alerting for system health and logs |
| **Backup system** | Automated backup and disaster recovery |

---

## Recommended Requirements

The recommended setup uses the **same two-node cluster** as the minimum. No additional nodes or upgrades are needed.

The cluster is sized to leave comfortable headroom beyond what the base platform uses. This means you can enable add-ons, absorb traffic spikes, and grow — all without touching your infrastructure.

> [!TIP]
> The same 2-node cluster handles everything — base platform and all add-ons — without any infrastructure changes.

---

## Requirements with Add-ons Enabled

Add-ons are optional features that are **disabled by default**. They can be enabled at any time after the base installation.

Even with all add-ons running at once, **no additional nodes are required**. The base cluster has enough capacity to handle them comfortably.

### Available Add-ons

<details>
<summary><b>DIAL</b> — QR code–based content linking</summary>

<br>

Enables QR code–based content linking. Learners can scan a code and land directly on the linked course or resource.

</details>

<details>
<summary><b>Discussion Forum</b> — Community threads and group management</summary>

<br>

Adds community discussion threads and group management to the platform, powered by NodeBB.

</details>

<details>
<summary><b>Video Streaming</b> — HLS video format conversion</summary>

<br>

Converts uploaded videos into a streamable format for smooth playback across devices and network conditions.

</details>

<br>

> [!NOTE]
> All add-ons are self-contained — they run inside the existing cluster and do not require additional storage or infrastructure.

---

<div align="center">

For a full per-component infrastructure breakdown, see the **[INFRA_DETAILS.md →](https://github.com/Sunbird-Spark/sunbird-spark-installer/blob/develop/INFRA_DETAILS.md)**

</div>