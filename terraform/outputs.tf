output "aws_region" {
  description = "AWS region used by the project"
  value       = var.aws_region
}

output "security_group_id" {
  description = "Student platform security group ID"
  value       = aws_security_group.student_platform.id
}

output "s3_bucket_name" {
  description = "Student records S3 bucket name"
  value       = aws_s3_bucket.student_records.bucket
}
