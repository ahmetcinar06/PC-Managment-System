import random
import time


class PC:
    
    CPU = "AMD Ryzen 5 2600 6-Core Processor"
    GPU = "Radeon RX 570"
    RAM = "16GB"
    SSD_C = "224GB"
    SSD_D = "224GB"

    def about_PC(self):
        print(f"CPU: {self.CPU}, GPU: {self.GPU}, RAM: {self.RAM}, SSD C: {self.SSD_C}, SSD D: {self.SSD_D}")

    def PC_status(self):
        CPU_utilization = random.randint(0, 100)
        GPU_utilization = random.randint(0, 100)
        RAM_utilization = random.randint(0, 100)
        SSD_C_utilization = random.randint(0, 100)
        SSD_D_utilization = random.randint(0, 100)

        print(f"CPU Utilization: {CPU_utilization}%, GPU Utilization: {GPU_utilization}%, RAM Utilization: {RAM_utilization}%, SSD C Utilization: {SSD_C_utilization}%, SSD D Utilization: {SSD_D_utilization}%")

        if CPU_utilization > 80 or GPU_utilization > 80 or RAM_utilization > 80 or SSD_C_utilization > 80 or SSD_D_utilization > 80:
            print("Warning: High resource utilization detected!")
            question = input("Do you want to optimize your PC performance? (yes/no): ")
            if question.lower() == "yes":
                print("Optimizing PC performance...")
            elif question.lower() == "no":
                print("No optimization will be performed.")
                time.sleep(0.5)
                print("Warning: Using your PC with high resource utilization for extended periods may affect performance and may shorten the lifespan of your hardware.")

        else:
            print("Your PC is running optimally.")

    def antivirus_scan(self):
        print("Performing antivirus scan...")
        time.sleep(2)
        scan_result = random.choice(["No threats found.", "Threats detected!"])
        print(scan_result)
        if scan_result == "Threats detected!":
            scan_query = input("Is this a false positive? (yes/no): ")
            if scan_query.lower() == "yes":
                print("Marking as false positive.")
            elif scan_query.lower() == "no":
                print("Removing potential threats...")

    def system_update(self):
        print("Checking for system updates...")
        time.sleep(2)
        update_available = random.choice([True, False])
        if update_available:
            update_query = input("Updates are available. Do you want to update your system? (yes/no): ")
            if update_query.lower() == "yes":
                print("Updating system...")
                time.sleep(1)
                print("System updated.")
            elif update_query.lower() == "no":
                print("Skipping system update.")
        else:
            print("Your system is up to date.")

    def processes(self):
        print("Listing running processes...")
        time.sleep(1)
        processes = ["Visual Studio Code", "Google Chrome", "File Explorer"]
        bg_processes = ["AMD External Events Client Module", "AMD Crash Defender", "Windows Security Service"]
        for process in processes:
            print(process)
        for bg_process in bg_processes:
            print(bg_process)
        print("End of process list.")


pc = PC()

while True:
    time.sleep(2)
    print("\nPC Management System")
    print("=================================")
    time.sleep(0.1)
    print("1. About PC")
    time.sleep(0.1)
    print("2. PC Status")
    time.sleep(0.1)
    print("3. Antivirus Scan")
    time.sleep(0.1)
    print("4. System Update")
    time.sleep(0.1)
    print("5. Processes")
    time.sleep(0.1)
    print("6. Exit")

    choice = input("Please select an option (1-6): ")

    if choice == "1":
        pc.about_PC()
    elif choice == "2":
        pc.PC_status()
    elif choice == "3":
        pc.antivirus_scan()
    elif choice == "4":
        pc.system_update()
    elif choice == "5":
        pc.processes()
    elif choice == "6":
        print("Exiting the PC Management System.")
        break
    else:
        print("Invalid choice, please try again.")
