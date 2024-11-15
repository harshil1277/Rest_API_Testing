import sys
import subprocess
import random
import csv
import matplotlib.pyplot as plt

def run_tools(toolname, service_name):
    # Generate a viable port number (assuming the range 1024-49151 for dynamic/private ports)
    port_number = random.randint(1024, 49151)

    print(f"Running {toolname} on port {port_number}...")
    
    # Run run_small.py with the tool name and port number
    run_command = ["python3", "run_small.py", toolname, str(port_number)]
    try:
        subprocess.run(run_command, check=True)
        print(f"{toolname} ran successfully on port {port_number}.")
    except subprocess.CalledProcessError as e:
        print(f"Error running {toolname}: {e}")
        return

    print(f"Generating report for {toolname} on port {port_number}...")
    
    # Run report_small.py with the port number
    report_command = ["python3", "report_small.py", str(port_number)]
    try:
        subprocess.run(report_command, check=True)
        print(f"Report generated successfully for {toolname} on port {port_number}.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating report for {toolname}: {e}")
        return

    print(f"Stopping service {service_name}...")
    
    # Run stop_service.py with the service name
    stop_command = ["python3", "stop_service.py", service_name]
    try:
        subprocess.run(stop_command, check=True)
        print(f"Service {service_name} stopped successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping service {service_name}: {e}")
        
    # Plotting the graph after running all the tools
    plot_graph_from_csv()

def plot_graph_from_csv():
    # Path to the CSV file
    csv_file_path = 'data/project-tracking-system/res.csv'

    try:
        # Read the CSV file
        with open(csv_file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            rows = list(csv_reader)
            
            # Extract first column (y values)
            y = [float(row[0].replace('%', '').strip()) for row in rows]  # Convert to float if necessary
            
            # Create x values as column numbers (1, 2, 3, ...)
            x = list(range(1, len(y) + 1))  # Column numbers as x values (1, 2, 3,...)
            
            # Plot the graph
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, marker='o', linestyle='-', color='b')
            plt.xlabel('Column Number')
            plt.ylabel('First Column Values')
            plt.title('Graph of Column Number vs. First Column Values')
            
            # Save the plot as an image
            plot_image_path = 'static/output_graph.png'
            plt.savefig(plot_image_path)
            plt.close()
            
            y = [float(row[1].replace('%', '').strip()) for row in rows]  # Convert to float if necessary
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, marker='o', linestyle='-', color='b')
            plt.xlabel('Column Number')
            plt.ylabel('First Column Values')
            plt.title('Graph of Column Number vs. First Column Values')
            
            # Save the plot as an image
            plot_image_path = 'static/output_graph2.png'
            plt.savefig(plot_image_path)
            plt.close()
            
            y = [float(row[2].replace('%', '').strip()) for row in rows]  # Convert to float if necessary
            plt.figure(figsize=(10, 6))
            plt.plot(x, y, marker='o', linestyle='-', color='b')
            plt.xlabel('Column Number')
            plt.ylabel('First Column Values')
            plt.title('Graph of Column Number vs. First Column Values')
            
            # Save the plot as an image
            plot_image_path = 'static/output_graph3.png'
            plt.savefig(plot_image_path)
            plt.close()
            
            print(f"Graph saved as {plot_image_path}")
    except FileNotFoundError:
        print(f"CSV file not found at {csv_file_path}. Please ensure the path is correct.")
    except Exception as e:
        print(f"An error occurred while plotting the graph: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        toolname = sys.argv[1]
        service_name = sys.argv[2]
        run_tools(toolname, service_name)
    else:
        print("Error: Tool name and service name arguments are required.")

