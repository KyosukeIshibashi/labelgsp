Labelgsp
=================

Overview
-----------------

#### Description

robot grasping についてのアノテーションツール

#### Requirement

pyqt5, pillow

#### Usage

```
python3 labelgsp.py [dir_name]
```

create rectangle: BoundingBoxを作成

remove rectangle: カーソルを当てると黄色くひかり、押すとBoundingBoxを削除

next/previous image: 次/前の画像に移る(このとき保存されていなくても警告が出ないので注意)

save image: 画像を保存
