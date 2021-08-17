#!/bin/bash

# GRANITE ECS ACCOUNTS AUTO DEPLOYMENT SCRIPT

set -e

echo "Starting Deployment Script"

# GET THE COMMAND LINE PARAMETERS

while getopts t:s:c:n: option
do
  case "${option}" in
    t) TASK_FAMILY=${OPTARG};;
    s) SERVICE_NAME=${OPTARG};;
    c) CLUSTER_NAME=${OPTARG};;
    n) FILE_NAME=${OPTARG};;
    *) echo "usage: $0 [-t] [-s] [-c] [-n]" >&4
         exit 1 ;;
  esac
done

echo "Task Family is $TASK_FAMILY"
echo "Service Name is $SERVICE_NAME"
echo "ECS Cluster Name is $CLUSTER_NAME"
echo "Image placeholder is $FILE_NAME"

# GET TASK DEFINITION AND CONTAINER DEFINITION FROM THE TASK JSON FILE

CONTAINER_DEFINITION_FILE=$(aws ecs describe-task-definition --task-definition $TASK_FAMILY)
echo "Task definition from file : $CONTAINER_DEFINITION_FILE"

CONTAINER_DEFINITION=$(echo $CONTAINER_DEFINITION_FILE | jq .taskDefinition.containerDefinitions)
echo "Container definition from file : $CONTAINER_DEFINITION"

# GET TASK VERSION
TASK_VERSION=$(aws ecs register-task-definition --family ${TASK_FAMILY} --execution-role-arn ${EXECUTION_ROLE_ARN} --network-mode ${NETWORK_MODE} --memory ${MEMORY}  --container-definitions "$CONTAINER_DEFINITION" | jq --raw-output '.taskDefinition.revision')
echo "Registered ECS Task Definition: " $TASK_VERSION

# If task exists then deploy service

if [ -n "$TASK_VERSION" ]; then
    echo "Update ECS Cluster: " $CLUSTER_NAME
    echo "Service: " $SERVICE_NAME
    echo "Task Definition: " $TASK_FAMILY:$TASK_VERSION

    DEPLOYED_SERVICE=$(aws ecs update-service --cluster $CLUSTER_NAME --service $SERVICE_NAME --task-definition $TASK_FAMILY:$TASK_VERSION --force-new-deployment | jq --raw-output '.service.serviceName')
    echo "Deployment of $DEPLOYED_SERVICE complete"

    echo "Script Ended"
else
    echo "exit: No task definition"
    echo "Script Exited to End"
    exit;
fi
