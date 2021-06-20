terraform {
  backend "s3" {
    bucket = "eks-tf-state-management"
    key    = "eks/prod/terraform.tfstate"
    region = "us-west-2"
    dynamodb_table = "eks-tf-state-lock"
  }
}