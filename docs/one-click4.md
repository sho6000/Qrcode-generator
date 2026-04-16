# One-Click Installer

Sunbird-ED can be deployed in two ways depending on your setup. If you're deploying on your own cloud environment, follow the manual installation method. If you're working within an organisation that has already set up GitHub Actions workflows, use that method instead.

---

## Before you begin

Regardless of which method you use, make sure the following are ready before starting.

### Required

| Requirement | Description |
|-------------|-------------|
| Domain name | A registered domain that will point to your Sunbird-ED instance |
| SSL certificate | A FullChain certificate — includes the private key, certificate, and CA bundle |
| Google OAuth credentials | Used for user authentication — [set up here](https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) |
| Google reCAPTCHA v3 credentials | Used to protect public-facing forms — [set up here](https://www.google.com/recaptcha/admin) |
| Email service provider | Any SMTP-compatible email service for sending platform emails |

### Optional

| Requirement | Description |
|-------------|-------------|
| MSG91 API token | Required if you want to send OTPs via SMS during registration or password reset |
| YouTube API token | Required if you want users to upload video content via YouTube URL |

---

## Method 1 — Manual installation

Use this if you are deploying Sunbird-ED on your own cloud environment. This method works on Azure, AWS, and GCP.

### Required tools

Install the following tools on the machine you'll run the installer from.

| Tool | Description |
|------|-------------|
| `jq` | Command-line JSON processor — [install](https://jqlang.github.io/jq/download/) |
| `yq` | Command-line YAML processor — [install](https://github.com/mikefarah/yq#install) |
| `rclone` | Cloud storage sync tool — [install](https://rclone.org/) |
| `OpenTofu` | Infrastructure provisioning tool — [install](https://opentofu.org/docs/intro/install/) |
| `Terragrunt` | Wrapper for OpenTofu to manage environments — [install](https://terragrunt.gruntwork.io/docs/getting-started/install/) |
| `kubectl` | Kubernetes command-line tool — [install](https://kubernetes.io/docs/tasks/tools/) |
| `helm` | Kubernetes package manager — [install](https://helm.sh/docs/intro/quickstart/#install-helm) |
| `Postman CLI` | Runs the post-install API setup — [install](https://learning.postman.com/docs/getting-started/installation/installation-and-updates/) |
| Python 3 | Required for helper scripts |
| PyJWT | Python package — install via `pip install PyJWT` |

For cloud-specific tools such as the Azure CLI, AWS CLI, or gcloud, follow the instructions in the provider-specific README inside the repository.

> The installer has been verified with **OpenTofu v1.11.4** and **Terragrunt v0.77.5**. If you run into issues with other versions, try these.

### Steps

**1. Clone the repository**

Clone the public installer repository to your local machine. You can find it at `github.com/project-sunbird/sunbird-ed-installer`.

**2. Set up your environment directory**

Inside the repository, navigate to your cloud provider's folder under `opentofu/`. Copy the `template` directory and give it the name of your environment — for example, `dev`, `staging`, or `prod`.

**3. Configure global values**

Open `global-values.yaml` inside your environment directory and fill in your domain, SSL certificate, OAuth credentials, and other required values. Refer to the provider-specific README for field-by-field guidance.

**4. Log in to your cloud provider**

Authenticate with your cloud provider using its CLI before running the installer. Each provider has its own login command — refer to your provider's documentation if needed.

**5. Run the installer**

From inside your environment directory, run `./install.sh`. The installer will provision your infrastructure, deploy all services, and configure the platform.

> The installer will back up and overwrite the rclone and kubeconfig files on your machine if they already exist. Existing versions are saved with a `.bak` extension.

---

## Method 2 — GitHub Actions

Use this if your organisation has already set up GitHub Actions workflows for Sunbird-ED deployment. This method automates the same steps as the manual installation and is specific to teams using the `spark-devops-sandbox` private config repository.

### How it works

Two repositories are involved.

| Repository | Type | Purpose |
|------------|------|---------|
| `sunbird-spark-installer` | Public | Contains the Helm charts and install scripts — fetched fresh at runtime |
| `spark-devops-sandbox` | Private | Contains your environment-specific config, credentials, and workflow files |

Your config files are encrypted using Ansible Vault. The workflows decrypt them at runtime — you never handle raw credentials directly.

### Step 1 — Create the infrastructure

Run this once per environment to provision the Kubernetes cluster. If the cluster already exists, skip to Step 2.

Go to your private config repository on GitHub → **Actions** → **Create Infrastructure (AKS)** → **Run workflow**.

| Input | Description |
|-------|-------------|
| Environment | The environment you're setting up — for example, `sandbox` |
| Config branch | The branch of the config repository to use |
| Source branch | The branch of the installer repository to use |
| Create cluster | Enable this to provision a new AKS cluster |

Once complete, the workflow updates your config repository with cluster details such as storage keys and endpoints — all encrypted automatically.

### Step 2 — Deploy services

Run this every time you want to deploy or update services on the cluster.

Go to your private config repository on GitHub → **Actions** → **Deploy Sunbird to AKS** → **Run workflow**.

| Input | Description |
|-------|-------------|
| Environment | The environment you're deploying to |
| Source branch | The branch of the installer repository to use |
| Installation mode | Either `full` or `selective` |

**Full deployment**

Set the installation mode to `full`. All building blocks are deployed in order and post-install steps run automatically.

**Selective deployment**

Set the installation mode to `selective` and choose which building blocks to deploy.

| Building block | What it includes |
|----------------|-----------------|
| Monitoring | Prometheus, Grafana, Loki |
| edbb | Kong, NGINX, Kafka, Player portal |
| learnbb | Keycloak, YugabyteDB, Redis, Elasticsearch, Flink, Lern |
| knowledgebb | Knowlg, Search, JanusGraph, Flink |
| obsrvbb | Telemetry, Superset |
| additional | Certificate service, web components, volume autoscaler |

**Single service deployment**

To update only one service, use selective mode, enable **Install Helm components**, and specify the building block and service name.

**Upgrading a service image**

To push a new Docker image without redeploying anything else, enable **Upgrade independent service** and provide the building block name, image key, and new image tag.

### Quick reference

| Scenario | Workflow | What to do |
|----------|----------|------------|
| First-time environment setup | Create Infrastructure | Enable create cluster |
| Deploy everything fresh | Deploy Sunbird | Mode: full |
| Deploy one building block | Deploy Sunbird | Mode: selective, pick the building block |
| Deploy one service | Deploy Sunbird | Mode: selective, enable Install Helm components |
| Push a new image | Deploy Sunbird | Enable Upgrade independent service |
| Re-run post-install steps only | Deploy Sunbird | Mode: selective, tick only the steps needed |

> Only one deployment can run at a time. If a workflow is already running, yours will queue up automatically.

---

## Default users

The installer creates the following users automatically. You can update passwords using the **Forgot Password** flow, or create new users via the admin API.

| Role | Email | Default password |
|------|-------|-----------------|
| Admin | admin@yopmail.com | Admin@123 |
| Content Creator | contentcreator@yopmail.com | Creator@123 |
| Content Reviewer | contentreviewer@yopmail.com | Reviewer@123 |
| Book Creator | bookcreator@yopmail.com | Bookcreator@123 |
| Book Reviewer | bookreviewer@yopmail.com | bookReviewer@123 |
| Public User 1 | user1@yopmail.com | User1@123 |
| Public User 2 | user2@yopmail.com | User2@123 |

> Update default passwords after your first login.

---

## SSL certificate setup

### Using Let's Encrypt

To enable automatic SSL certificate management, set `lets_encrypt_ssl` to `true` in your `global-values.yaml`. When enabled, a Kubernetes CronJob handles certificate issuance and renewal automatically.

After each renewal, fetch the updated certificate values from the `nginx-public-ingress` ConfigMap and update the `proxy_private_key` and `proxy_certificate` fields in your `global-values.yaml`.

### Using a custom certificate

If you're managing your own SSL certificate, set `lets_encrypt_ssl` to `false` and provide your certificate and private key under `proxy_certificate` and `proxy_private_key` in your `global-values.yaml`.

---

## Destroying the deployment

To tear down all provisioned infrastructure, navigate to your environment directory and run `./install.sh destroy_tf_resources`.

> This permanently removes all resources provisioned by the installer for that environment. Make sure you have backups before proceeding.