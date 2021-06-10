# batch_stuff
stress-ng in a container for testing things in aws batch

I didn't have an ML / BigData image since I have like, 0 skills in that area and I needed to have something that would just -run- in Batch. 

So, I built a small container that is alpine based and just runs `stress-ng` and you can submit the jobs via Lambda

How To Use:
  - create a batch CE
  - create a queue
  - create your job def (feel free to use the one provided just needs an image URI)
  - deploy the lambda (make sure you have the right perms)
  - Build the dockerfile and push to ECR (this is where you get the URI for the job def)
  - configure a test event that looks like the one in the repo 
  - fill out those keys with the data in question
  - submit 

As an aside, you might want to change the compute defined the job def, I leave that up to y'all 

Lambda needs to be deployed and has to have a role that allow it to submit jobs, at minimum. 
Since I was lazy, my role gives it full Batch access. 

The lambda is written such that it takes a simple JSON object as input to the lambda handler, the variable names should be all self-explanatory. 
So, there's simple-lambda-event that has the outline for what gets passed to the lambda. 

The code is small, lambda handler maps some vars, and then submits the job via a function that just calls the batch API. 

More detail about the request structure can be found here: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/batch.html#Batch.Client.submit_job


for detail on what flags can be used with stress-ng, see here: https://manpages.ubuntu.com/manpages/artful/man1/stress-ng.1.html

useful for testing different job defintiion parameters, like container overrides, etc. 
