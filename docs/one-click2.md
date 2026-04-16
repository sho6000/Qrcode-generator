# One-Click Installer

The one-click installer sets up a full Sunbird-ED deployment on your cloud infrastructure. It provisions the cluster, installs all services, and configures the platform automatically — you just need to prepare a few things before running it.

---

## Before you begin

Make sure the following are ready before starting the installation.

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

## Required tools

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

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/project-sunbird/sunbird-ed-installer.git
```

### 2. Set up your environment directory

Navigate to your cloud provider's folder and create a copy of the template directory. The template name used here is `demo` — replace it with your preferred environment name such as `dev`, `staging`, or `prod`.

```bash
cd opentofu/<cloud-provider>
cp -r template demo
cd demo
```

### 3. Configure global values

Open `global-values.yaml` and fill in your domain, SSL certificate, OAuth credentials, and other required values. Refer to the provider-specific README for field-by-field guidance.

### 4. Log in to your cloud provider

```bash
# Azure
az login --tenant AZURE_TENANT_ID

# AWS
aws configure

# GCP
gcloud auth login
```

### 5. Run the installer

```bash
time ./install.sh
```

The installer will provision your infrastructure, deploy all services, and configure the platform. This may take a while depending on your cloud provider and network speed.

> **Note:** The installer will back up and overwrite the following files if they already exist on your machine — `~/.config/rclone/rclone.conf` and `~/.kube/config`. Existing versions are saved with a `.bak` extension.

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

To enable automatic SSL certificate management, set the following in your `global-values.yaml`:

```yaml
lets_encrypt_ssl: true
```

When enabled, a Kubernetes CronJob handles certificate issuance and renewal automatically. After each renewal, fetch the updated values from the `nginx-public-ingress` ConfigMap and update your `global-values.yaml`:

```yaml
proxy_private_key: |
  <renewed private key>

proxy_certificate: |
  <renewed certificate>
```

### Using a custom certificate

If you're managing your own SSL certificate, set the flag to false and provide your certificate details manually:

```yaml
lets_encrypt_ssl: false

proxy_private_key: |
  <your private key>

proxy_certificate: |
  <your certificate>
```

---

## Destroying the deployment

To tear down all provisioned infrastructure for an environment:

```bash
cd opentofu/<cloud-provider>/<env>
time ./install.sh destroy_tf_resources
```

> This permanently removes all resources provisioned by the installer for that environment. Make sure you have backups before proceeding.