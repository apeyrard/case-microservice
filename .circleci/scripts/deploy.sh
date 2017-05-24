#!/usr/bin/env bash

# more bash-friendly output for jq
JQ="jq --raw-output --exit-status"
IMAGE_URL=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REGISTRY_REPO_NAME:$CIRCLE_SHA1

configure_aws_cli(){
	aws --version
	aws configure set default.region $AWS_REGION
	aws configure set default.output json
}

deploy_cluster() {

    family=$REGISTRY_REPO_NAME

    make_task_def
    #register_definition
    #if [[ $(aws ecs update-service --cluster sample-webapp-cluster --service sample-webapp-service --task-definition $revision | \
                   #$JQ '.service.taskDefinition') != $revision ]]; then
        #echo "Error updating service."
        #return 1
    #fi

    ## wait for older revisions to disappear
    ## not really necessary, but nice for demos
    #for attempt in {1..30}; do
        #if stale=$(aws ecs describe-services --cluster sample-webapp-cluster --services sample-webapp-service | \
                       #$JQ ".services[0].deployments | .[] | select(.taskDefinition != \"$revision\") | .taskDefinition"); then
            #echo "Waiting for stale deployments:"
            #echo "$stale"
            #sleep 5
        #else
            #echo "Deployed!"
            #return 0
        #fi
    #done
    #echo "Service update took too long."
    #return 1
}

make_task_def(){
   envsubst < ask_definition.json
}

push_ecr_image(){
	eval $(aws ecr get-login --region $AWS_REGION)
	docker push $IMAGE_URL
}

register_definition() {

    if revision=$(aws ecs register-task-definition --container-definitions "$task_def" --family $family | $JQ '.taskDefinition.taskDefinitionArn'); then
        echo "Revision: $revision"
    else
        echo "Failed to register task definition"
        return 1
    fi

}

configure_aws_cli
push_ecr_image
deploy_cluster
