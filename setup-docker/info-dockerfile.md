# Dockerfileについて
Seki-Labのlingam-1プロジェクトをクローンする.

## dockerの環境
ubuntu 22.04
git 2.34.1

## 仕様
- gitのインストール  
- ローカルのカレントディレクトリにある`.ssh`をubuntuの`/root/.ssh`にコピー．このとき権限をchmod600としている．（所有者に読み書きの権限を付与)  
- 


`RUN git clone git@github.com:tcu-seki-lab/lingam-1.git`の部分でクローンはできるが`.git`がない場合がある．
そのときは以下の手順を踏む  

```sh
# bash

# クローン先のディレクトリまで行く
cd /usr/local/Lingam-1/

# クローンしたフォルダを削除する
rm -rf lingam-1

# 再度クローンする
git clone git@github.com:tcu-seki-lab/lingam-1.git

```