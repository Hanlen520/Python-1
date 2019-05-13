import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # Flask-SQLAlchemy配置
    # 从DATABASE_URL环境变量中获取数据库URL
    # 如果没有定义, 将其配置为basedir变量表示的应用顶级目录下的一个名为app.db的文件路径
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    # 用于设置数据发生变更之后是否发送信号给应用
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ...
    LANGUAGES = ['en', 'es']


    # 通过电子邮件发送错误信息
    # 电子邮件的配置变量包括服务器和端口，启用加密连接的布尔标记以及可选的用户名和密码
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['Crisimple@163.com']

    # 用户动态分页配置：以表示每页展示的数据列表长度
    POSTS_PER_PAGE = 10


    # 将Elasticsearch集成到本应用是展现Flask魅力
    # ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

