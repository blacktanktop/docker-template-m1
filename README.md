# docker-template-m1
研究コード開発環境の構築用のDockerfileやdocker-compose.ymlや.devcotainerのファイルとサンプルコード。

## 解説
[くろたんく雑記帳](https://blacktanktop.hatenablog.com/entry/2021/12/24/145145)に書いた。

## 実行方法

```
docker-compose build
docker-compose run app python -m rdkit_MolToGridImage
```
./dataに実行結果の画像が保存される。

![MolToGridImage](https://user-images.githubusercontent.com/7370243/147322497-8389f307-f771-4324-8aa3-fe57e464b6df.png)
