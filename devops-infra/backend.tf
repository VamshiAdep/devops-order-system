terraform {
  backend "s3" {
    bucket         = "vamshi-devops-tf-state"
    key            = "devops-infra/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}