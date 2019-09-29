# PyTree

利用 YAML 文件快捷地画树

## Install

请使用 Python 3 及以上版本

```sh
pip3 install -e 'git+https://github.com/bwangelme/pytree#egg=pytree'
```

## Usage

```sh
$ curl https://raw.githubusercontent.com/bwangelme/pytree/master/examples/tree/tree.yaml -o tree.yaml
$ pytree tree.yaml
$ ls output/
round-table.gv     round-table.gv.png   # 在当前目录的 output 文件夹能够看到生成的图片以及 gv 源文件
```

目前用法较为简单，`l`指定节点的名称，`ch`指定节点的子节点。
