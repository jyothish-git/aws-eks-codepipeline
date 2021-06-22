# aws-eks-codepipeline

## EKS cluster creation Workflow:
```
CodeCommit => CodePipeline => CodeBuild => EKS Deployment
```
```
CodeCommit => Storing the terraform code + CodeBuild scripts
CodePipeline => CodePipeline trigger automatically when it detect a git tag push. CloudWatch event rule is configured for watching the repository changes.
CodeBuild => CodePipeline invoke CodeBuild and CodeBuild perform the EKS cluster setup using Terraform.CodeBuild checkout the respective Git tag and execute the tf commands for EKS infra provisioning.
```

##  Aws App Mesh is used for observability:

```
1. App Mesh controller deployed in EKS
2. Deployed App mesh resources in EKS
3. Deployed a sample nginx app in EKS.
```
