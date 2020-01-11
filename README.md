# template-dockerfile-flask

詳細設定寫於：
[實作 Dockerfile + flask 教學 (附GitHub完整程式) | Max行銷誌](https://www.maxlist.xyz/2020/01/11/docker-flask/)


### step 1 - git clone
``` 
git clone https://github.com/hsuanchi/template-dockerfile-flask.git
```

### step 2 -  將 dockerfile 打包成 image

``` 
docker image build -t dockerfile_test .
```

### step 3 - 透過 image 產生隔離的執行環境 container

``` 
docker run -p 80: 8888 dockerfile_test
```

連線 0.0.0.0:80 或 127.0.0.1:80 ，就可以看到 Flask Dockerized 就表示成功囉！

