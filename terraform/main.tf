resource "aws_instance" "app_server" {
  ami                    = "ami-06067086cf86c58e6" 
  instance_type          = "t3.micro"
  key_name               = "my-ec2-key"
  vpc_security_group_ids = [aws_security_group.app_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y python3 git
              pip3 install flask
              EOF

  tags = {
    Name = "flask-app-server"
  }
}