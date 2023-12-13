
import os
import subprocess

# List of scripts 
scripts = [
    "create_address_script_xml_json.py",
    "create_service_script_xml.py",
    "create_service_script.py",
    "create_user_script.py",
    "delete_address_script.py",
    "delete_service_script.py",
    "get_address_script.py",
    "get_all_addresses_script.py",
    "get_all_services_for_address.py",
    "get_all_services_script.py",
    "get_service_script.py",
    "load_mock_script.py",
    "query_addresses_script.py",
    "update_address_script.py",
    "update_service_script.py"
]

def run_script(script_name):
    # Runs the Python script passed in script_name
    subprocess.run(["python", script_name], check=True)

def main():
    # Main function to display menu and handle user input
    while True:
        print("Please select a script to run (or type 'exit' to quit):")
        for idx, script in enumerate(scripts, 1):
            print(f"{idx}. {script}")
        
        choice = input("Enter your choice (number): ").strip()
        if choice.lower() == 'exit':
            break

        try:
            script_number = int(choice)
            if 1 <= script_number <= len(scripts):
                run_script(scripts[script_number - 1])
            else:
                print("Invalid choice, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()
