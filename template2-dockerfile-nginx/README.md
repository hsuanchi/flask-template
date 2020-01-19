## template1 dockerfile+nginx+ssl

詳細設定寫於：
[實作 Dockerfile + nginx + ssl 教學 (附GitHub完整程式) | Max行銷誌](https://www.maxlist.xyz/2020/01/19/docker-nginx/)

### step 1 - git clone
``` 
git clone https://github.com/hsuanchi/template-docker-flask.git
cd template2-dockerfile-nginx
```

### step 2 -  將 dockerfile 打包成 image

``` 
docker image build -t docker_nginx_ssl .
```

### step 3 - 透過 image 產生隔離的執行環境 container

``` 
docker run -p 80:80 -p 443:443 docker_nginx_ssl
```

瀏覽 http://localhost/ 如果有看到 helloworld \
瀏覽 https://localhost/ 會看到瀏覽器提示不安全 ( 因為是使用自簽憑證 ) 就代表成功囉！
