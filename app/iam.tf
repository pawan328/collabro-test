resource "aws_iam_role" "example" {
  name = "demo-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })
}

resource "aws_iam_role_policy" "insecure_policy" {
  name = "overly_permissive"
  role = aws_iam_role.example.name

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect   = "Allow",
        Action   = "*",               # <-- overly permissive
        Resource = "*"               # <-- overly permissive
      }
    ]
  })
}