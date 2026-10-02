# 使用示例

## 1. 直接生成正文配图

适用于文章、短口播和单句观点。新安装默认使用 Xinju；如果已经替换过人物，则自动使用当前活动人物。

```text
使用 $xinju-ip-illustrations，为下面这段内容生成正文配图：

<粘贴文章、短口播或观点句>
```

Skill 会先输出配图方案和三种风格。确认方案后回复：

```text
确认，选择 1。
```

风格编号：

```text
1：手绘线稿
2：平涂插画
3：拼贴漫画
```

## 2. 更换或恢复人物 IP

更换人物只更新活动人物，不会同时生成正文配图。

### 真人照片生成新 IP

```text
使用 $xinju-ip-illustrations，用我上传的真人照片生成迷你人物 IP，并直接替换活动人物。
```

### 使用已有的人物 IP

```text
使用 $xinju-ip-illustrations，把我上传的人物 IP 直接设为活动人物，不重新设计。
```

### 查看当前人物

```text
使用 $xinju-ip-illustrations，展示当前活动人物。
```

### 恢复默认 Xinju

```text
使用 $xinju-ip-illustrations，恢复 Xinju。
```

> Skill 同时只保留一个活动人物。新人物会直接覆盖当前人物；恢复 Xinju 后，后续配图重新使用内置 Xinju。
