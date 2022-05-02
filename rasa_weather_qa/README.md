# 天气问答Demo

## 1.Requirements
+ python==3.7
+ rasa==1.10.12
+ mitie

需要下载total_word_feature_extractor_zh.dat文件，放在`../dat/`路径，或自行修改config.yml。

## 2. 启动action
>rasa run actions --port 5055 --actions actions --debug

![](./rasa_run_actions.png)

## 3. 启动shell
>rasa shell

![](./rasa_shell.png)

## 参考
+ https://github.com/rasahq/rasa
+ https://github.com/RasaHQ/rasa-demo