MonburanBlog
======================
##写这个博客的动机
嘛，之前的博客一直在用wordpress，有一天突然手贱更新了自己的主题，自己之前改的一些配置啥的页没有了。<br />
然后莫名其妙来了股火，就备份了wp的数据回滚硬盘，重新搭wp。<br />
悲剧的是重新搭好的wp不知道为啥导入不了数据，然后就没有然后了。<br />
于是乎自己用django写一个blog的想法就冒出来了。<br />
中间把大二学过的js和css捡了捡。<br />
断断续续写了半个多月，后边又有点事情停了几天没动。<br />
其实中间改的最多的不是bug，而是界面__(:з」∠)__<br />
总之拖了将近一个月才把东西架到服务器上。<br />

##功能

富文本编辑，代码高亮，文章发布，标签分类(标签云)，多说评论，后台管理

##说明
基于<b>django</b>框架<br />

后台采用<b>django-admin-bootstrap</b>美化<br />(可能在未来版本中取消)
后台编辑器采用<b>ckeditor</b>符文本编辑器<br />
评论系统采用<b>多说</b><br />
代码高亮采用<b>highlight</b>，配色采用<b>solarized-dark</b><br/>
标签云采用修改过<b>jqcloud</b><br />
图标采用<b>Font Awesome</b><br />
推荐使用uwsgi+nginx+mysql部署<br />

ps:这么看感觉好多东西都不是我自己写的似得

#更新
ver20160914：后台功能修改，添加批量设置文章为草稿或者发布状态。处理了部分问题页面。修改了部分界面样式处理了部分问题页面。修改了部分界面样式。(个人认为这个可以作为正式第一版了)<br />
ver20160918：修复可以在标签或分类里可以查看草稿状态文章的问题，添加过滤器，根据创建时间和状态进行过滤，管理界面中添加分类和标签的文章统计。<br />
