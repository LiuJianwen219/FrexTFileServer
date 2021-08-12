# FrexTFileServer
FrexT 系统的文件服务



```shell
# 导出所有的依赖
pip freeze > requirements.txt
# 依赖恢复
pip install -r requirements.txt
```

```shell
# 使用uwsgi进行部署，单机多进程多线程
source venv
uwsgi --ini FrexTFileServer.ini
cat /FrexT/FrexTFileServer.log
uwsgi --stop /FrexT/FrexTFileServer.pid
```
