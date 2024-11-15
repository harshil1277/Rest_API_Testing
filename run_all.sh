#!/bin/bash

# Define the list of tools and services
TOOLS=("evomaster-whitebox" "evomaster-blackbox" "restler" "restest" "resttestgen" "bboxrt" "schemathesis" "dredd" "tcases" "apifuzzer")
SERVICES=("cwa-verification" "erc20-rest-service" "features-service" "genome-nexus" "languagetool" "market" "ncs" "news" "ocvn" "person-controller" "problem-controller" "project-tracking-system" "proxyporint" "rest-study" "restcountries" "scout-api" "scs" "spring-batch-rest" "spring-boot-sample-app" "user-management") # replace {service_name_list} with actual services, e.g., "service1 service2"

# Initialize port number (start from a base port number, e.g., 8000)
BASE_PORT=8000
PORT=$BASE_PORT

# Activate virtual environment
source venv/bin/activate

# Check if there's an existing tmux session and kill it if it exists
if tmux ls &>/dev/null; then
    echo "Existing tmux session found. Terminating..."
    tmux kill-session
fi

# Loop through each service and each tool
for SERVICE in "${SERVICES[@]}"; do
    for TOOL in "${TOOLS[@]}"; do
        echo "Running $TOOL on $SERVICE using port $PORT..."

        # Run the tool on the service with the specified port
        python3 run_small.py "$TOOL" "$PORT"

        # Generate the report for the current tool and service
        python3 report_small.py "$PORT"

        # Move report files to service-specific folder
        mkdir -p "data/$SERVICE/$TOOL"
        mv "data/$SERVICE/res.csv" "data/$SERVICE/$TOOL/res.csv"
        mv "data/$SERVICE/error.json" "data/$SERVICE/$TOOL/error.json"
        mv "data/$SERVICE/time.json" "data/$SERVICE/$TOOL/time.json"

        # Stop the service after testing
        python3 stop_service.py "$SERVICE"

        # Increment port number for next run
        PORT=$((PORT + 1))
    done
done

# Deactivate virtual environment
deactivate

echo "All tools have been tested against all services. Reports generated and services stopped."

