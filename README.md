MonburanBlog
======================
##写这个博客的动机
嘛，之前的博客一直在用wordpress，有一天突然手贱更新了自己的主题，自己之前改的一些配置啥的页没有了。<br />
然后莫名其妙来了股火，就备份了wp的数据回滚硬盘，重新搭wp。<br />
悲剧的是重新搭好的wp不知道为啥导入不了数据，然后就没有然后了。<br />
于是乎自己用django写一个blog的想法就冒出来了。<br />
中间把大二学过的js和css捡了捡。<br />
断断续续写了半个多月，后边又有点事情停了几天没动。<br />
其实中间改的最多的不是bug，而是界面_(:з」∠)_<br />
总之拖了将近一个月才把东西架到服务器上。<br />

##功能

富文本编辑，代码高亮，文章发布，标签分类，多说评论，后台管理

##说明
基于django框架<br />

后台采用django-admin-bootstrap美化<br />
后台编辑器采用ckeditor符文本编辑器<br />
评论系统采用多说<br />
代码高亮采用highlight，配色采用solarized-dark<br/>
标签云采用jqcloud<br />
图标采用Font Awesome<br />
使用uwsgi+nginx部署<br />

ps:这么看感觉好多东西都不是我自己写的似得
