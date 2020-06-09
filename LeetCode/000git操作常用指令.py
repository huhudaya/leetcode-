# 001git操作常用指令.py
查看分支：git branch

创建分支：git branch name

切换分支：git checkout name

创建+切换分支：git checkout –b name

合并某分支到当前分支：git merge name

删除分支：git branch –d name




在临时需要起一个分支，当时当前分支内容还不提交的时候，可以使用Git还提供了一个stash功能，可以把当前工作现场 ”隐藏起来”，等以后恢复现场后继续工作
git stash 将当前的工作现场隐藏起来


八、多人协作

当你从远程库克隆时候，实际上Git自动把本地的master分支和远程的master分支对应起来了
并且远程库的默认名称是origin
	1.要查看远程库的信息 使用 git remote

	2.要查看远程库的详细信息 使用 git remote –v

推送分支就是把该分支上所有本地提交到远程库中，推送时，要指定本地分支，这样，Git就会把该分支推送到远程库对应的远程分支上
：使用命令 git push origin master


# 推送分支 dev
git push origin dev
# 推送冲突
当大家都推送分支的时候，会发生失败
由上面可知：推送失败，因为我的小伙伴最新提交的和我试图推送的有冲突，解决的办法也很简单
上面已经提示我们，先用git pull把最新的提交从origin/dev抓下来，然后在本地合并，解决冲突，再推送。


因此：多人协作工作模式一般是这样的：

首先，可以试图用git push origin branch-name推送自己的修改.
如果推送失败，则因为远程分支比你的本地更新早，需要先用git pull试图合并。
如果合并有冲突，则需要解决冲突，并在本地提交。再用git push origin branch-name推送。 




1.git clone ip.git    clone项目(master分支)
2.git branch     查看分支
3.git checkout dev    切换分支到dev
4.git add .   更改好代码先提交到dev上
5.git commit -m "提交dev"   将更改的代码提交到本地
6.git push    将更改的代码提交到远程仓库(这里是dev)
----------------------以上是正常的git开发使用,下面是如何将dev合并到master---------------------------
7.git checkout master    切换分支到master
8.git status   如果是有提交信息会看到(看图1)
9.git add .    此时将更改的文件add到本地master仓库里
10.git commit -m "提交到master"   将本地更改的信息提交到master本地仓库
11.git push   将更改的代码提交到远程仓库(这里是master)
12.git checkout dev      master提交完成后就可以在切换回dev进行开发了。