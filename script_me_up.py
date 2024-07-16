import os

# Function to get the type of script from the user
def get_script_type():
    while True:
        script_type = input("Enter script type (batch, powershell, vbscript): ").lower()
        if script_type in ['batch', 'powershell', 'vbscript']:
            return script_type
        else:
            print("Invalid script type. Please enter 'batch', 'powershell', or 'vbscript'.")

# Function to display available tasks and get the selected task from the user
def get_task():
    tasks = {
        1: "Map Network Drive",
        2: "Remove Network Drive",
        3: "Set Environment Variable",
        4: "Clear Temp Files",
        5: "Deploy Printer",
        6: "Update Group Policy",
        7: "Configure Power Settings",
        8: "Enable Remote Desktop",
        9: "Block Specific Websites",
        10: "Sync Time with NTP Server",
        11: "Create Local Admin Account",
        12: "Log User Logon Times",
        13: "Disable USB Ports",
        14: "Map Network Drives Based on Group Membership",
        15: "Configure Windows Firewall Settings",
        16: "Deploy Software",
        17: "Change Desktop Wallpaper",
        18: "Restrict Access to Control Panel",
        19: "Log Off Idle Users",
        20: "Enable BitLocker"
    }
    
    # Display task options
    for key, value in tasks.items():
        print(f"{key}. {value}")
    
    # Get the user's task selection
    while True:
        try:
            task = int(input("Enter the number of the task you want to automate: "))
            if task in tasks:
                return task, tasks[task]
            else:
                print("Invalid task number. Please enter a number between 1 and 20.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 20.")

# Function to generate the script based on user inputs
def generate_script(script_type, task, task_name):
    script = ""
    
    # Generate script based on type and task
    if script_type == "batch":
        if task == 1:  # Map Network Drive
            drive_letter = input("Enter drive letter (e.g., H:): ")
            share_path = input("Enter network share path (e.g., \\\\server\\share): ")
            script = f"@echo off\nnet use {drive_letter} {share_path}\n"
        
        elif task == 2:  # Remove Network Drive
            drive_letter = input("Enter drive letter (e.g., H:): ")
            script = f"@echo off\nnet use {drive_letter} /delete\n"
        
        elif task == 3:  # Set Environment Variable
            var_name = input("Enter environment variable name: ")
            var_value = input("Enter environment variable value: ")
            script = f"@echo off\nsetx {var_name} {var_value}\n"
        
        elif task == 4:  # Clear Temp Files
            script = f"@echo off\ndel /q /s %TEMP%\\*\n"
        
        elif task == 5:  # Deploy Printer
            printer_name = input("Enter printer name: ")
            driver_name = input("Enter printer driver name: ")
            port_name = input("Enter printer port name: ")
            script = f"@echo off\nrundll32 printui.dll,PrintUIEntry /if /b \"{printer_name}\" /f \"{driver_name}\" /r \"{port_name}\" /m \"{driver_name}\"\n"
        
        # More batch tasks can be added here...
        
    elif script_type == "powershell":
        if task == 1:  # Map Network Drive
            drive_letter = input("Enter drive letter (e.g., H:): ")
            share_path = input("Enter network share path (e.g., \\\\server\\share): ")
            script = f"New-PSDrive -Name {drive_letter[0]} -PSProvider FileSystem -Root {share_path}\n"
        
        elif task == 2:  # Remove Network Drive
            drive_letter = input("Enter drive letter (e.g., H:): ")
            script = f"Remove-PSDrive -Name {drive_letter[0]}\n"
        
        elif task == 3:  # Set Environment Variable
            var_name = input("Enter environment variable name: ")
            var_value = input("Enter environment variable value: ")
            script = f"[System.Environment]::SetEnvironmentVariable(\"{var_name}\", \"{var_value}\", \"User\")\n"
        
        elif task == 4:  # Clear Temp Files
            script = f"Remove-Item -Path $env:TEMP\\* -Recurse -Force\n"
        
        elif task == 5:  # Deploy Printer
            printer_name = input("Enter printer name: ")
            driver_name = input("Enter printer driver name: ")
            port_name = input("Enter printer port name: ")
            script = f"Add-Printer -Name \"{printer_name}\" -DriverName \"{driver_name}\" -PortName \"{port_name}\"\n"
        
        # More PowerShell tasks can be added here...
        
    elif script_type == "vbscript":
        if task == 1:  # Map Network Drive
            drive_letter = input("Enter drive letter (e.g., H:): ")
            share_path = input("Enter network share path (e.g., \\\\server\\share): ")
            script = f'Set objNetwork = CreateObject("WScript.Network")\nobjNetwork.MapNetworkDrive "{drive_letter}", "{share_path}"\n'
        
        elif task == 2:  # Remove Network Drive
            drive_letter = input("Enter drive letter (e.g., H:): ")
            script = f'Set objNetwork = CreateObject("WScript.Network")\nobjNetwork.RemoveNetworkDrive "{drive_letter}", True, True\n'
        
        elif task == 3:  # Set Environment Variable
            var_name = input("Enter environment variable name: ")
            var_value = input("Enter environment variable value: ")
            script = f'Set objShell = CreateObject("WScript.Shell")\nobjShell.Environment("User").Item("{var_name}") = "{var_value}"\n'
        
        elif task == 4:  # Clear Temp Files
            script = 'Set objFSO = CreateObject("Scripting.FileSystemObject")\nobjFSO.DeleteFile(objFSO.GetSpecialFolder(2) & "\\*.*")\n'
        
        elif task == 5:  # Deploy Printer
            printer_name = input("Enter printer name: ")
            driver_name = input("Enter printer driver name: ")
            port_name = input("Enter printer port name: ")
            script = f'Set objNetwork = CreateObject("WScript.Network")\nobjNetwork.AddWindowsPrinterConnection "{printer_name}", "{driver_name}", "{port_name}"\n'
        
        # More VBScript tasks can be added here...
    
    return script

# Function to save the generated script to a file
def save_script(script_type, task_name, script):
    filename = f"{task_name.replace(' ', '_').lower()}.{script_type}"
    with open(filename, 'w') as file:
        file.write(script)
    print(f"Script saved as {filename}")

# Main function to drive the script generation process
def main():
    print("Script Generator for Administrators")
    script_type = get_script_type()  # Get the type of script from the user
    task, task_name = get_task()  # Get the task the user wants to automate
    script = generate_script(script_type, task, task_name)  # Generate the script
    save_script(script_type, task_name, script)  # Save the script to a file

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
