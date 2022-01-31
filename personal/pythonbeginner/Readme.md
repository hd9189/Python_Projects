4.3 Setup Git & Github
a) Create "CPP" repository in Github

b) Create "README.md" inside "C++" folder
C:\>echo "# C++" >> README.md

c) Follow the command to submit the code to github
Add ".gitignore" inside "C++" folder
.gitignore

C:\>cd [C++_folder]
C:\>git init
C:\>git add .
C:\>git config user.name [github_username]
C:\>git config user.email [github_email]
C:\>git commit -m "first commit"
C:\>git branch -M main
C:\>git remote add origin https://github.com/[github_username]/cpp.git
C:\>git push -u origin main