# PyTree

利用 YAML 文件快捷地画树

## Install

pip install -e https://github.com/bwangelme/pytree

## Usage

```sh
$ curl https://raw.githubusercontent.com/bwangelme/pytree/master/examples/tree/tree.yaml -o /tmp/tree.yaml
$ pytree /tmp/tree.yaml
$ ls output/
round-table.gv     round-table.gv.png   # 在当前目录的 output 文件夹能够看到生成的图片以及 gv 源文件
```

目前用法较为简单，`l`指定节点的名称，`ch`指定节点的子节点。
