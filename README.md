# ORIGO 2025

A documentation website for ORIGO 2025 powered by [Hugo](https://gohugo.io/) and the [Lotus Docs](https://github.com/colinwilson/lotusdocs) theme.

---

## 🚀 Prerequisites

To run this project locally, ensure the following are installed:

- [Git](https://git-scm.com/)
- [Go](https://go.dev/) (version **1.25.1** or later)
- [Hugo (Extended Version)](https://gohugo.io/) (version **0.140.0** or later)

---

## ⚙️ Installing Prerequisites

### 🐧 Linux

1. **Install Git**
   ```bash
   sudo apt update
   sudo apt install git
   git --version
   ```


2. **Install Go**
    ```bash
    wget https://go.dev/dl/go1.25.1.linux-amd64.tar.gz
    sudo tar -C /usr/local -xzf go1.25.1.linux-amd64.tar.gz
    echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
    source ~/.bashrc
    go version
    ```


3. **Install Hugo**
    ```bash
    wget https://github.com/gohugoio/hugo/releases/download/v0.140.0/hugo_extended_0.140.0_Linux-64bit.tar.gz
    tar -zxvf hugo_extended_0.140.0_Linux-64bit.tar.gz
    sudo mv hugo /usr/local/bin/hugo
    hugo version
    ```

### Windows

1. **Install Git**
    Download and install from: [here](https://git-scm.com/download/win)

    Verify:

    ```powershell
    git --version
    ```

2. **Install Go (1.25.1 or later)**
    Download the installer from: [here](https://go.dev/dl/)
    (e.g., go1.25.1.windows-amd64.msi)
    Run installer → verify:

    ```powershell
    go version
    ```

3. **Install Hugo Extended (0.140.0 or later)**
    Download from: [here](https://github.com/gohugoio/hugo/releases)

    Extract `hugo.exe`

    Place it in a folder that is in your system PATH, or add the folder manually
    Verify:

    ```powershell
    hugo version
    ```

## 🚀 Deploying website locally for development


1. **Clone the repository:**

    ```powershell
    git clone https://github.com/rignitc/origo25
    cd origo25
    ```


2. **Deploy the Hugo site locally:**

    ```powershell
    hugo server -D
    ```


3. **Open in browser**

    Type or copy `http://localhost:1313/origo25/` into your browser to see the rendered website.
