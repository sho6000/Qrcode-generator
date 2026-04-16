# 🚀 Sunbird-ED One-Click Installation Guide

Think of this guide as the "Quick Start" manual for launching your own learning platform. We’ve automated the heavy lifting so you can get Sunbird-ED up and running on the cloud with just a few commands.

---

## 📋 1. Your Pre-Flight Checklist

Before you start the engines, make sure you have these five "must-haves" ready. These are the keys to your platform's house.

### The Essentials
* **🌐 A Domain Name:** You’ll need a web address (like `learn.yourorg.org`) already registered and pointed to your cloud.
* **🔒 Security (SSL) Certificate:** This provides the "HTTPS" lock icon on your site, keeping user data safe.
* **🔑 Google Credentials:** Needed for the "Login with Google" and anti-spam (ReCaptcha) features.
* **✉️ Email Service:** An account (like SendGrid or AWS SES) to send welcome emails and password resets.
* **📱 Optional Extras:** You can also set up SMS services (MSG91) or YouTube integration if you want to send OTPs or host videos.

---

## 🛠️ 2. The Toolbox

You will need a few standard developer tools installed on your computer. These tools act as the "mechanics" that build your platform in the cloud.

| Tool | Purpose |
| :--- | :--- |
| **OpenTofu & Terragrunt** | The architects that build your cloud servers. |
| **kubectl & Helm** | The managers that organize the software inside those servers. |
| **Python 3** | Runs small helper scripts to keep things tidy. |
| **jq & yq** | Simple tools that read and write your configuration files. |

---

## 🏗️ 3. How to Launch (Step-by-Step)

Once your checklist is clear and your toolbox is ready, follow these five simple steps:

### Step 1: Download the "Blueprint"
First, download the installer code to your computer:
```bash
git clone [https://github.com/project-sunbird/sunbird-ed-installer.git](https://github.com/project-sunbird/sunbird-ed-installer.git)
```

### Step 2: Choose Your Cloud
Tell the installer where you want to build (Azure, AWS, or GCP) and create a workspace for your project:
```bash
cd opentofu/<cloud-provider>   # Choose azure, aws, or gcp
cp -r template my-platform     # Create your own environment folder
cd my-platform
```

### Step 3: Fill in Your Details
Open the file named `global-values.yaml` and paste in your domain, email settings, and Google credentials.

### Step 4: Log In to the Cloud
Ensure you are logged into your cloud provider's account via the terminal (e.g., `az login`, `aws configure`, or `gcloud auth login`).

### Step 5: Ignite!
Run the magic command to start the installation:
```bash
time ./install.sh
```

---

## 4. Who Can Log In?

You will need a few standard developer tools installed on your computer. These tools act as the "mechanics" that build your platform in the cloud.

| Role | Username | Password |
| :--- | :--- | :--- | 
| **Admin** | `admin@yopmail.com` | `Admin@123` |
| **Teacher / Creator** | `contentcreator@yopmail.com` | `Creator@123` |
| **Reviewer** | `contentreviewer@yopmail.com` | `Reviewer@123` |
| **Student / User** | `user1@yopmail.com` | `User1@123` |

> **Security Note:** Make sure to change these passwords immediately after your first login using the **Forgot Password** option.

---

## 5. Need to Start Over?

If you ever need to completely remove the platform and stop being charged by your cloud provider, run this command from your project folder:
```bash
time ./install.sh destroy_tf_resources
```

> In your `global-values.yaml`, you can set `lets_encrypt_ssl: true`. This tells Sunbird-ED to automatically renew your security certificates every 85 days so you never have to worry about your site being marked as "unsafe".
