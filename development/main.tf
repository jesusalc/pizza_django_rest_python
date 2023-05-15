provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "development" {
  ami           = "ami-0c94855ba95c574c8"
  instance_type = "t2.micro"

  tags = {
    Name = "development-instance"
  }
}


