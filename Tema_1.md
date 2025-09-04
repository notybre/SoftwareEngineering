# Тема 1. Работа с Git
Отчет по теме 1 выполнил:
- Брейер Роман Алексеевич 
- ИВТ-23-1

| Задание | Лаб_раб |
|---------|---------|
| Задание 1 | + |
| Задание 2 | + |
| Задание 3 | + |
| Задание 4 | + |
| Задание 5 | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |
| Задание 11 | + |
| Задание 12 | + |
| Задание 13 | + |
| Задание 14 | + |
| Задание 15 | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_1.PNG)

## Выводы
Git успешно установлен

## Лабораторная работа №2
### Настройка.

``` git
Roman@Computer MINGW64 ~ (master)
$ git config --global user.name "notybre"

Roman@Computer MINGW64 ~ (master)
$ git config --global user.email "romanbrejer3@gmail.com"

Roman@Computer MINGW64 ~ (master)
$ git config --global core.editor "code --wait"

```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_2.PNG)

## Выводы
Установлено имя и почта пользователя, успешна пройдена проверка конфига, в качестве эдитора коммитов устновлен VSCode

## Лабораторная работа №3
### Создание нового репозитория.

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering
$ git init
Initialized empty Git repository in A:/GIT/SoftwareEngineering/.git/
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_3.PNG)

## Выводы
Создан пустой репозиторий по указанному пути

## Лабораторная работа №4
### Подготовка файлов.

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git add proba.txt

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   proba.txt

```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_4.PNG)

## Выводы
Файл proba.txt подготовлен к коммиту

## Лабораторная работа №5
### Фиксация изменений.

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git commit -m "Первый коммит"
[main (root-commit) 7944bf3] Первый коммит
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 proba.txt

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git log -n 5
commit 7944bf3d79e9c00590d9b83366406f5d943be517 (HEAD -> main)
Author: notybre <romanbrejer3@gmail.com>
Date:   Thu Sep 4 15:47:05 2025 +0500

    Первый коммит

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git log --oneline
7944bf3 (HEAD -> main) Первый коммит

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git log --graph
* commit 7944bf3d79e9c00590d9b83366406f5d943be517 (HEAD -> main)
  Author: notybre <romanbrejer3@gmail.com>
  Date:   Thu Sep 4 15:47:05 2025 +0500

      Первый коммит

```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_5.PNG)

## Выводы
Коммит осуществляется командой git commit -m комментарий. Также есть несколько способов посмотреть лог коммитов: -n (кол-во), --oneline (в одну линию), --graph

## Лабораторная работа №6
### Подключение к удалённому репозиторию

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git remote add origin https://github.com/notybre/SoftwareEngineering

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git pull origin main
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (3/3), 933 bytes | 6.00 KiB/s, done.
From https://github.com/notybre/SoftwareEngineering
 * branch            main       -> FETCH_HEAD
 * [new branch]      main       -> origin/main
fatal: refusing to merge unrelated histories

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git stash
No local changes to save

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git stash apply
No stash entries found.

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git stash pop
No stash entries found.


```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_6.PNG)

## Выводы
С помощью git remote add можно связать локальный репозиторий гит с удаленным репозиторием, например GitHub. Также можно добавить все незафиксированные изменения в стэш, чтобы было удобно переключаться с одной ветки на другую с незафиксипованными изменениями

## Лабораторная работа №7
### Ветвление

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git branch TestBranch

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git checkout TestBranch
Switched to branch 'TestBranch'

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (TestBranch)
$ git switch TestBranch
Already on 'TestBranch'

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (TestBranch)
$ git merge faeture
merge: faeture - not something we can merge

```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_7.PNG)

## Выводы
Ветвление происходит с помощью команды git branch. Для работы непосредственно с ветками нужно провести checkout имя_ветки.

## Лабораторная работа №8
### Фетч

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (TestBranch)
$ git fetch https://github.com/notybre/SoftwareEngineering
From https://github.com/notybre/SoftwareEngineering
 * branch            HEAD       -> FETCH_HEAD

```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_8.PNG)

## Выводы
Фетч является предварительной операцией перед слиянием или преобразованием. Позволяет проверить конфликтность перед изменениями.

## Лабораторная работа №9
### Удаление файлов, веток, локальных и удаленных репозиториев.

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (TestBranch)
$ git rm proba.txt
rm 'proba.txt'

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git branch -d TestBranch
Deleted branch TestBranch (was 7944bf3).

```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_9.PNG)

## Выводы
Есть много способов удалить файл / ветку, в том числе: git rm --cached file.txt (удаляет файл только из индекса) и различие -d (безопасное удаление ветки - проверяет что ветка была слита перед удалением) и -D (принудительное удаление ветки)

## Лабораторная работа №10
### Отслеживание изменений в коммитах

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git log
commit 7944bf3d79e9c00590d9b83366406f5d943be517 (HEAD -> main)
Author: notybre <romanbrejer3@gmail.com>
Date:   Thu Sep 4 15:47:05 2025 +0500

    Первый коммит

Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git diff


```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_10.PNG)

## Выводы
Можно посмотреть изменения в коммитах с помощью git log и git diff коммит1 коммит2 (различия между коммитами). Также можно просматривать изменения с помощью GitHub Desktop.

## Лабораторная работа №11
### Возвращение файла к предыдущему состоянию.

``` git
Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git checkout main --testfile.txt
error: unknown option `testfile.txt'
usage: git checkout [<options>] <branch>
   or: git checkout [<options>] [<branch>] -- <file>...

    -b <branch>           create and checkout a new branch
    -B <branch>           create/reset and checkout a branch
    -l                    create reflog for new branch
    --[no-]guess          second guess 'git checkout <no-such-branch>' (default)
    --[no-]overlay        use overlay mode (default)
    -q, --[no-]quiet      suppress progress reporting
    --[no-]recurse-submodules[=<checkout>]
                          control recursive updating of submodules
    --[no-]progress       force progress reporting
    -m, --[no-]merge      perform a 3-way merge with the new branch
    --[no-]conflict <style>
                          conflict style (merge, diff3, or zdiff3)
    -d, --[no-]detach     detach HEAD at named commit
    -t, --[no-]track[=(direct|inherit)]
                          set branch tracking configuration
    -f, --[no-]force      force checkout (throw away local modifications)
    --[no-]orphan <new-branch>
                          new unborn branch
    --[no-]overwrite-ignore
                          update ignored files (default)
    --[no-]ignore-other-worktrees
                          do not check if another worktree is using this branch
    -2, --ours            checkout our version for unmerged files
    -3, --theirs          checkout their version for unmerged files
    -p, --[no-]patch      select hunks interactively
    -U, --unified <n>     generate diffs with <n> lines context
    --inter-hunk-context <n>
                          show context between diff hunks up to the specified nu
mber of lines
    --[no-]ignore-skip-worktree-bits
                          do not limit pathspecs to sparse entries only
    --[no-]pathspec-from-file <file>
                          read pathspec from file
    --[no-]pathspec-file-nul
                          with --pathspec-from-file, pathspec elements are separ
ated with NUL character


Roman@Computer MINGW64 /a/GIT/SoftwareEngineering (main)
$ git commit -m "Восстановление файла к предыдущему состоянию"
[main 79fb612] Восстановление файла к предыдущему состоянию
 1 file changed, 0 insertions(+), 0 deleti
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_11.PNG)

## Выводы
Команда git checkout main --path заменит текущую версию файла на состояние из указанного коммита

## Лабораторная работа №12
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_1.PNG)

## Выводы
Git успешно установлен

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_1.PNG)

## Выводы
Git успешно установлен

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_1.PNG)

## Выводы
Git успешно установлен

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_1.PNG)

## Выводы
Git успешно установлен

## Лабораторная работа №1
### Установка.

``` git
git --version
```
### Результат.
![Меню](https://github.com/notybre/SoftwareEngineering/blob/Tema_1/pic/Tema1_1.PNG)

## Выводы
Git успешно установлен



