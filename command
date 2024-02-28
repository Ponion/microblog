# 下述命令都依赖环境变量FLASK_APP，配置在.env中
# 运行项目
flask run
#同python，只是可以直接进入到当前应用的上下文
flask shell
# 初始化迁移数据库
flask db init
# 生成迁移脚本
flask db migrate
# 迁移数据库（除sqlite其他数据库需要手动创建）
flask db upgrade
# 删除上次迁移
flask db downgrade
