import boto3

batch = boto3.client('batch')  # establishes a session to the ecs API

def start(jn,jq,jd,co):
    job = batch.submit_job(
        jobName=jn, 
        jobQueue=jq,
        jobDefinition=jd,
        containerOverrides= co,
    )
    return job

def handler(event, context):
    jn=event['jobName']
    jq=event['jobQueue']
    jd=event['jobDefinition']
    co=event['containerOverrides']
    start(jn, jq, jd, co)