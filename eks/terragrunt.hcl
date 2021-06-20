generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF
provider "aws" {
  region = "us-west-2"
}
EOF
}
remote_state {
  backend = "s3"
  config = {
    encrypt        = true
    bucket         = "eks-tf-state-management"
    key            = "eks/prod/terraform.tfstate"
    region         = "us-west-2"
    dynamodb_table = "eks-tf-state-lock"
  }
  generate = {
    path      = "backend.tf"
    if_exists = "overwrite_terragrunt"
  }
}