variable "aws_region" {
  description = "AWS region for the project"
  type        = string
  default     = "ap-south-1"
}

variable "my_ip_cidr" {
  description = "Your public IP address in CIDR format for SSH access"
  type        = string
}
