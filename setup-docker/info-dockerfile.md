# Dockerfileについて
Seki-Labのlingam-1プロジェクトをクローンする.

## dockerの環境
ubuntu 22.04
git 2.34.1

## 仕様
- gitのインストール  
- ローカルのカレントディレクトリにある`.ssh`をubuntuの`/root/.ssh`にコピー．このとき権限をchmod600としている．（所有者に読み書きの権限を付与)  
- `/usr/local/Lingam-1/`に`lingam-1`リポジトリをクローン

## 動作方法
1. docker にgithub環境を構築する
2. sshキー作成用コンテナの準備
3. dockerfileの準備
4. コンテナイメージの作成
5. コンテナの作成

1~3は別資料で説明

4,5のみを行えば可能
```sh
# cmd or terminal

# Dockerfileと.sshディレクトリを配置

$ ls -a
# カレントディレクトリに.ssh/  Dockerfile <--この二つのファイルがあればok

# Dockerファイルからイメージ作成
# $ docker build -t イメージ名 . 
docker build -t lingam-1 .  

# Dockerコンテナの作成
# docker run -it --name コンテナ名 イメージ名
docker run -it --name lingam-1-container lingam-1

```


`RUN git clone git@github.com:tcu-seki-lab/lingam-1.git`の部分でクローンはできるが`.git`がない場合がある．
そのときは以下の手順を踏む  

```sh
# bash

# クローン先のディレクトリまで行く
cd /usr/local/Lingam-1/

# クローンしたフォルダを削除する
rm -rf /usr/local/Lingam-1/lingam-1

# 再度クローンする
git clone git@github.com:tcu-seki-lab/lingam-1.git

```