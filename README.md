# upmon -- мониторинг доступности компьютеров с веб интерфейсом, написанный на питоне 3.x
# upmon -- uptime monitor in python 3.x with web interface

Если хотите использовать upmon, просто скачайте последнюю версию: [http://upmon.ru/download](http://upmon.ru/download)
If you want to use upmon, simply download the latest version from [http://upmon.ru/download](http://upmon.ru/download)

- Основная информация: <http://upmon.ru/>
- Ошибки: <https://github.com/ademaro/upmon/issues>
- Исходные коды: <https://github.com/ademaro/upmon>
- Документация для разработчиков: <https://github.com/ademaro/upmon/wiki>

- General info: <http://upmon.ru/>
- Issue tracking and bug reporting: <https://github.com/ademaro/upmon/issues>
- Mainline source code: <https://github.com/ademaro/upmon>
- Developer documentation: <https://github.com/ademaro/upmon/wiki>

## Development

**Get the source (for building):**

    git clone --recursive https://github.com/ademaro/upmon.git
    git remote add upstream https://github.com/ademaro/upmon.git

**Get the source (for contributing):**

If you want to contribute to the project you will have to [make a fork](http://help.github.com/forking/). Then do this:

    git clone --recursive git@github.com:MyUsername/upmon.git
    git remote add upstream https://github.com/ademaro/upmon.git

**Start upmon deamon:**

    python upmon.sh


### Refreshing your clone

Since upmon is made up of a main repository as well as a few sub-repositories (git submodules) a simple `git pull` is not sufficient to update your source tree clone. Use the `update.sh` shell script for this:

    ./update.sh

It will fetch updates from the upstream repository (upmon/upmon). Then you should merge the branches you want to use, for example something like so:

    git merge upstream/master

You can use it to update from your own repository by calling it like this:

    ./update.sh origin

### Contributing

The main upmon source tree is hosted on git (a popular [DVCS](http://en.wikipedia.org/wiki/Distributed_revision_control)), thus you should create a fork of the repository in which you perform development. See <http://help.github.com/forking/>.

We prefer that you send a [*pull request* here on GitHub](http://help.github.com/pull-requests/) which will then be merged into the official main line repository. You need to sign the Kod CLA to be able to contribute (see below).

Also, in your first contribution, add yourself to the end of `AUTHORS.md` (which of course is optional).


#### Creating and submitting a patch

As mentioned earlier in this article, we prefer that you send a [*pull request*](http://help.github.com/pull-requests/) on GitHub.

1. Create a fork of the upstream repository by visiting <https://github.com/upmon/upmon/fork>. If you feel unsecure, here's a great guide: <http://help.github.com/forking/> 

2. Clone of your repository: `git clone https://yourusername@github.com/yourusername/upmon.git`

3. This is important: Create a so-called *topic branch*: `git checkout -tb name-of-my-patch` where "name-of-my-patch" is a short but descriptive name of the patch you're about to create. Don't worry about the perfect name though -- you can change this name at any time later on.

4. Hack! Make your changes, additions, etc and commit them.

5. Send a pull request to the upstream repository's owner by visiting your repository's site at github (i.e. https://github.com/yourusername/upmon) and press the "Pull Request" button. Here's a good guide on pull requests: <http://help.github.com/pull-requests/>

**Use one topic branch per feature** -- don't mix different kinds of patches in the same branch. Instead, merge them all together into your master branch (or develop everything in your master and then cherry-pick-and-merge into the different topic branches). Git provides for an extremely flexible workflow, which in many ways causes more confusion than it helps you when new to collaborative software development. The guides provided by GitHub at <http://help.github.com/> are a really good starting point and reference.
If you are fixing a ticket, a convenient way to name the branch is to use the URL slug from the bug tracker, like this: `git checkout -tb 53-feature-manually-select-language`.


For a list of contributors, please see [AUTHORS](https://github.com/upmon/upmon/blob/master/AUTHORS.md) and <https://github.com/upmon/upmon/contributors>

