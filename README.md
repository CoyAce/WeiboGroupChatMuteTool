# WeiboGroupChatMuteTool

支持对微博群开启禁言和取消禁言。

## 配置说明

* id:：微博群的唯一标识
* source：用户的唯一标识
* cookie：用于对source进行校验，判断用户是否登录

## 配置获取方法

使用Chrome访问<https://api.weibo.com/chat>，在请求参数和cookie中获取。  
具体操作:  
1. 为按F12检查页面元素，找到Network选项，在浏览器中查看需要管理的群的消息，筛选出query_messages.json请求
2. 复制url中的id参数和source参数，替换config.json中对应的项。  
<img src="https://github.com/CoyAce/WeiboGroupChatMuteTool/blob/main/param.png" width="50%">
4. 复制cookie中的SUB参数和SUBP参数，用;连接，替换config.json中对应的项.  
<img src="https://github.com/CoyAce/WeiboGroupChatMuteTool/blob/main/cookie.png" width="50%">

## 使用方法
* 开启群禁言 python main.py 1  
* 关闭群禁言 python main.py 4  
