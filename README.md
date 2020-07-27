# bds_ds1_project

This repo contains the code and files for the DS 1 project for BDS group.

### Group members

* Caren Munai
* Matt Kimuyu
* Oscar Omurwa
* David Gitonga

### Git installation

Macbook should already have Git available through Terminal. To check if you already have Git installed in Windows, launch the Command Prompt window and type the command below. If Git is installed the system will report back the Git version. If not click [Git for Windows](https://git-scm.com/download/win) to install.

```sh
git --version
```

### Repository setup

To get all the project files on your local machine, we need to clone the project. Using Command Prompt/Teminal, go to your class folder where you store all your class notes and run the git clone command below. This will create a new project folder and clone the project files to it. You will need to use your GitHub credentials to authenticate this request.

```sh
git clone https://github.com/dgitts/bds_ds1_project.git
```

From here, we will assume all commands ran are being ran from the project folder.

### Adding project features

Using Command Prompt, go into the bds_ds1_project folder and fetch the most up to date code from GitHub using the command below. Everytime you begin working on a new feature, it is recommended that you pull in the most recent code from your repo.

```sh
git pull
```

Create a new feature branch, in the example below we are are creating a new branch called sqlite_database which we intend to add a sqlite database to our project

```sh
git checkout -b feature/sqlite_database
```

### Saving changes

After you have worked on your feature and it is now complete, you are now ready to save the changes in Git. You can optionally use the Git status command to show you what files were updated. This is a final review step to make sure you intend to save all the changes.

```sh
git status
```


Next, we tell Git that we want to include all our updates in the next commit. The '.' means all so we are adding all changes.

```sh
git add .
```

Git add doesn't really affect the repository in any significant way—changes are not actually recorded until you run git commit.
So we type our git commit command with the -m message flag and enter a short descriptive message (in double quotes for Windows systems) describing our changes.

```sh
git commit -m "added sqlite database"
```

Next, we will push our changes to the GitHub repository

```sh
git push -u origin feature/sqlite_database
```

In the command above we set -u flag to tell Git to create the feature/sqlite_database branch in the GitHub repository. In Git "origin" is shorthand for the remote repository that a project was originally cloned from.

### Video Tutorial

See [GitHub Basics](https://drive.google.com/file/d/1FIS6uwfCjfkoKXXURyTPXyxMFzUm3lFs/view?usp=sharing) video tutorial.
