# flask-pluginkit-isso

Isso评论插件

### 安装

`pip install git+https://github.com/flask-pluginkit/flask-pluginkit-isso@master`

### 使用

- requirements.txt包含`git+https://github.com/flask-pluginkit/flask-pluginkit-isso@master`

- 插件配置(定义在应用程序的config，或者初始化PluginManager传入)：

    - ISSO_API：必选，isso服务的接口地址

    - ISSO_JS：可选，js文件地址，默认是`ISSO_API/js/embed.min.js`

    - ISSO_AVATAR：可选，显示svg头像，默认false

    - ISSO_GRAVATAR：可选，显示gravatar头像，默认true（与上者不要同时为true，否则会显示两个头像）

    - ISSO_REPLY_NOTIFICATIONS：可选，开启评论回复功能，默认true（注：仍需要勾选允许回复才会真的发送评论回复邮件）

    - ISSO_REQUIRE_AUTHOR：可选，评论时要求填写昵称

- 模板配置：

    - 在需要显示评论的地方引用：     `{{ emit_tep("isso_content", title="这里是评论页面标题，默认为空") }}`

    - 在需要显示评论的页面js处引用： `{{ emit_tep("isso_script") }}`

### 注意：

`不兼容Flask-PluginKit<3`

### 示例

`python demo.py`
