

# 🌐 Wake-on-LAN Flask Server

A simple, modern Flask project that provides a web interface and API to wake computers on the local network using Wake-on-LAN. 🚀

## 📋 Project Overview
This project uses Flask to provide both a web interface and an API. It allows users to wake a computer in the network via a simple web interface. It supports Wake-on-LAN functionality and can be run as a `.exe` file without requiring Python installation.

## 📂 Project Structure
```plaintext
wol/
├── .venv/             # Virtual environment (optional)
├── templates/         # HTML files
│   └── index.html
└── main.py            # Main script
```

## 🚀 Installation and Usage

### 1. Using the `.exe` File
If you have the `.exe` file, you can run it directly on a Windows PC without needing Python installed.

1. Navigate to the `dist` folder where the `main.exe` file is located.
2. Double-click `main.exe` to start the server.
3. Open a web browser and go to `http://localhost:5000` to access the web interface.

> **Note:** On the first run, Windows may prompt you to allow network access. Grant this access so the app can function on the network.

### 2. Running with Python

If Python is installed, you can run the project directly through the `main.py` script.

#### Requirements
- **Python 3.7 or higher**
- Install dependencies from `requirements.txt`.

#### Steps

1. **Activate the virtual environment** (recommended):
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server**:
   ```bash
   python main.py
   ```

4. Open a web browser and go to `http://localhost:5000`.

## 🛠 Requirements
To run the project with Python, the following libraries are needed:

```plaintext
Flask==2.1.2
Wakeonlan==3.0.0
```

These are listed in `requirements.txt` and can be installed with `pip install -r requirements.txt`.

## 🌐 Endpoints

### Web Interface
- **URL**: `http://localhost:5000`
- **Description**: Provides a web-based GUI to wake devices in the network.

### API Endpoint
- **URL**: `http://localhost:5000/api/wake`
- **Method**: `POST`
- **Parameters**:
  - `mac_address` (required): The MAC address of the device to be woken.
- **Example**:
  ```bash
  curl -X POST http://localhost:5000/api/wake -d "mac_address=XX:XX:XX:XX:XX:XX"
  ```

## 📖 License
This project is licensed under the MIT License.

---

### 💡 Tips
- Make sure the computer you want to wake supports Wake-on-LAN and that the feature is enabled in the BIOS.
- When creating an `.exe` file with PyInstaller, some antivirus software may flag it. Add the file to the exception list if necessary.

## ✨ Screenshots
![Web Interface Screenshot](path/to/your/screenshot.png)

