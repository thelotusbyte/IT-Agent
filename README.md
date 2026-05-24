# IT Agent - Windows Diagnostic Utility

A Python-based diagnostic tool for Windows systems that provides insights into battery health, disk usage, system performance, and network connectivity.

## Features

### 🔋 Battery Health Analysis
- Generates a comprehensive Windows battery report using `powercfg`.
- Parses HTML reports to extract Design Capacity, Full Charge Capacity, and Cycle Count.
- Provides health percentage, wear level, and status recommendations.

### 💽 Disk Check
- Scans all local drives for usage statistics (Total, Used, Free space).
- Automatically detects drive types (SSD, NVMe, HDD) using PowerShell.
- Flags critical and warning states based on capacity thresholds (80% for Warning, 90% for Critical).

### 🚀 Performance Monitoring
- **RAM Usage:** Displays total and used memory with percentage.
- **CPU Usage:** Real-time CPU utilization percentage.
- **Process Tracking:** Lists top 5 CPU and RAM consuming processes.

### 🌐 Network Diagnostics
- Verifies Internet connectivity via Google DNS.
- Checks DNS resolution functionality.
- Measures network latency using TCP ping.
- Provides detailed I/O statistics (bytes and packets sent/received).

## Prerequisites

- **Operating System:** Windows (Required for full functionality)
- **Python:** 3.6 or higher

## Installation

1. Clone or download this repository.
2. Install the required Python dependencies:
   ```bash
   pip install psutil beautifulsoup4
   ```

## Usage

Run the main utility script using Python:

```bash
python main.py
```

*Note: Some features like battery report generation may require administrative privileges.*

## Project Structure

- `main.py`: The entry point that orchestrates all diagnostic checks.
- `battery_check.py`: Logic for battery report generation, parsing, and health analysis.
- `disk_check.py`: Drive scanning and type detection logic.
- `performance_check.py`: CPU/RAM usage and process monitoring functions.
- `network_check.py`: Connectivity, DNS, and network I/O statistics.
- `os_check.py`: Utility to verify Windows environment compatibility.

## License

This project is open-source and available for modification and distribution.
