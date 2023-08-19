Version control tutorial from both class and 

**git init** 
starts up a repository and creates hidden folder .git

**git status** 
'on branch master' 

 **git status**
very similar is 
**git show**
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
**git commit -m "insert messaege here"**

```git push origin new_branch```

****************************
git remote -v 
shows remote repository
git remote add origin "http://192.168.1.5/git-server"

git remote -h 

git remote  - v 
now shows the server 
===================
**git push origin master**  

**git checkout -b new_branch**
creates new branch

**git push origin new_branch**
pushes file to the new branch

why?  **git add .** 
because
add * means add all files in the current directory, except for files whose name begin with a dot. This is your shell functionality and Git only ever receives a list of files.

add . has no special meaning in your shell, and thus Git adds the entire directory recursively, which is almost the same, but including files whose names begin with a dot.

on a separate note, you write code with either 3 tilde to open and close, or you use 3 backticks 
~~~
sudo su
~~~
just testing joplin, which uses markdown.
```
print("hello world")

```
```git checkout  -b new_branch```

```git checkout -b BRANCH_NAME``` creates a new branch and checks out the new branch while ```git branch BRANCH_NAME``` creates a new branch but leaves you on the same branch.

In other words ```git checkout -b BRANCH_NAME ```does the following for you.

```git branch BRANCH_NAME```    # create a new branch
```git switch BRANCH_NAME ```   # then switch to the new branch

```git status``` to see which branch ur on 

```git checkout master```  to switch to master

```git merge newbranch```  ---if you do from the master, it gets the new content from new branch to master
 

```git branch --list``` shows all the branches

```git branch -d```    deletes the branch 

revert to an older change 

```git reset  --hard ed2cab37 ``` you put the sha of the commit ID

and then 

```git pull origin master ```


=======================================
 ```git remote add origin  https://github.com/ale-rabb200/``` 
 ```git remote add origin webaddrerss``` 
aggiunge un repo remoto, i will then need to clone that into my folder. make it local


Shows URLs of remote repositories

```git remote -v```


origin	https://github.com/ale-rabb200/ (fetch)
origin	https://github.com/ale-rabb200/ (push)


in sostanza add. aggiunge tutti i file nella staging area. 
poi commit -m "messaggio"

```
git log
``` 
== commit history 
```
git log -2
```





```git rm --cached filename ```
 removes from staging area only, not your drive

```git commit --amend  ```??????





adding an origin point 

```
git remote add origin https://github.com/ale-rabb200/programming-2.git
```


```git clone https://github.com/ale-rabb200/programming-2.git```



sposta al main branch. 
~~~
 git branch -M main 
~~~

