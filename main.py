import sys
from os_check import is_windows
from battery_check import (generate_battery_report,parse_battery_report,analyze_battery_health)
from disk_check import (disk_check,display_disk_check)
from performance_check import (
    get_ram_usage,
    get_cpu_usage,
    get_top_cpu_processes,
    get_top_ram_processes
)
from network_check import (
    check_internet_connection,
    check_dns_resolution,
    tcp_ping,
    get_network_stats
)
from startup_check import get_startup_apps
from browser_check import browser_check

def main():
    if not is_windows():
        print("Error: Unsupported Operating System", file=sys.stderr)
        print("This software currently supports only Windows.", file=sys.stderr)
        sys.exit(1)

    print("Windows detected")
    print("Proceeding with the utility...")
    
    result = generate_battery_report()

    if result["success"]:

        print("Battery report generated successfully")
        print(f"Report saved at: {result['report_path']}")
        battery_data = parse_battery_report(
            result["report_path"]
        )

        print("\nBattery Information")
        print("-------------------")

        print(f"Design Capacity: {battery_data['design_capacity']}")
        print(f"Full Charge Capacity: {battery_data['full_charge_capacity']}")
        print(f"Cycle Count: {battery_data['cycle_count']}")
        analysis = analyze_battery_health(
            battery_data
        )

        print("\nBattery Health Analysis")
        print("-----------------------")

        print(
            f"Battery Health: "
            f"{analysis['health_percent']}%"
        )

        print(
            f"Battery Wear: "
            f"{analysis['wear_percent']}%"
        )

        print(
            f"Status: "
            f"{analysis['status']}"
        )

        print(
            f"Recommendation: "
            f"{analysis['recommendation']}"
        )
    else:

        print("Failed to generate report")
        print(result["error"])


    # Disk Check
    disk_results = disk_check()

    display_disk_check(disk_results)
    # RAM
    ram_data = get_ram_usage()

    print("RAM USAGE")
    print(f"Total RAM: {ram_data['total_ram_gb']} GB")
    print(f"Used RAM : {ram_data['used_ram_gb']} GB")
    print(f"RAM Usage: {ram_data['ram_percent']}%\n")


    # CPU
    cpu_data = get_cpu_usage()

    print("CPU USAGE")
    print(f"CPU Usage: {cpu_data['cpu_percent']}%\n")


    # Top CPU Processes
    print("TOP CPU PROCESSES")

    top_cpu = get_top_cpu_processes()

    for process in top_cpu:
        print(
            f"PID: {process['pid']} | "
            f"Name: {process['name']} | "
            f"CPU: {process['cpu_percent']}% | "
            f"RAM: {process['memory_mb']} MB"
        )

    print()


    # Top RAM Processes
    print("TOP RAM PROCESSES")

    top_ram = get_top_ram_processes()

    for process in top_ram:
        print(
            f"Name: {process['name']} | "
            f"Instances: {process['instances']} | "
            f"RAM: {process['total_memory_mb']} MB"
        )

    print()

    print("Starting network diagnostics...\n")

    # Internet Check
    internet_status = check_internet_connection()

    if internet_status:
        print("✓ Internet Connection: Available")
    else:
        print("✗ Internet Connection: Not Available")

    print()

    # DNS Check
    dns_result = check_dns_resolution()

    if dns_result["dns_working"]:
        print("✓ DNS Resolution: Working")
        print(f"Resolved IP: {dns_result['resolved_ip']}")
    else:
        print("✗ DNS Resolution: Failed")

    print()

    # TCP Ping + Latency
    tcp_result = tcp_ping()

    if tcp_result["reachable"]:
        print("✓ TCP Connectivity: Reachable")
        print(f"Latency: {tcp_result['latency_ms']} ms")
    else:
        print("✗ TCP Connectivity: Failed")

    print()

    # Network Statistics
    network_stats = get_network_stats()

    print("Network Statistics:")
    print(f"Bytes Sent: {network_stats['bytes_sent']}")
    print(f"Bytes Received: {network_stats['bytes_received']}")
    print(f"Packets Sent: {network_stats['packets_sent']}")
    print(f"Packets Received: {network_stats['packets_received']}")
    
    # STARTUP APPS
    startup_data = get_startup_apps()

    print("\nSTARTUP APPS")

    if "error" in startup_data:
        print(f"Error: {startup_data['error']}")
    else:
        print(f"Startup App Count: {startup_data['startup_app_count']}")

        print("Startup Applications:")

        for app in startup_data["startup_apps"]:
            print(f"- {app}")


    


    browser_name = input("Enter browser: ")

    browser_data = browser_check(browser_name)


    print("\n===== BROWSER CHECK =====\n")

    print(f"Browser           : {browser_data['browser']}")
    print(f"Browser Found     : {browser_data['browser_found']}")

    print(f"\nCache Size (MB)   : {browser_data['cache_size_mb']}")
    print(f"Cache Status      : {browser_data['cache_status']}")

    print(f"\nExtension Count   : {browser_data['extension_count']}")
    print(f"Extension Status  : {browser_data['extension_status']}")

    print(f"\nBrowser Version   : {browser_data['browser_version']}")

    print(f"\nDefault Browser   : {browser_data['default_browser']}")

    if browser_data["error_messages"]:
        print("\nErrors:")

        for error in browser_data["error_messages"]:
            print(f"- {error}")
        
if __name__ == "__main__":
    main()
