# Xinju IP 配图 Skill

把中文正文或短口播中的观点、流程、状态和隐喻，转化为由迷你人物 IP 亲自参与的正文配图。

![Xinju IP 四视图](xinju-ip-illustrations/assets/ip/xinju-ip-four-view.png)

## 核心能力

- 默认使用 Xinju 迷你人物 IP。
- 支持手绘线稿、平涂插画、拼贴漫画三种渲染风格。
- 正文配图采用“方案说明 → 选择风格 → 确认后生图”的两阶段流程。
- 支持把用户明确上传并获授权的真人照片转成迷你人物 IP。
- 支持把用户已有的完整人物 IP 直接设为活动人物。
- 新人物直接覆盖当前活动人物，不维护历史人物列表。
- 用户说“恢复 Xinju”时，可恢复内置默认人物。
- 默认生成 16:9 横版正文配图，也可按用户指定画幅原生构图。

## 三种风格

### 1. 手绘线稿

![手绘线稿风格母板](xinju-ip-illustrations/assets/style/lineart-style-board.png)

纯白背景、黑色手绘细线、浅暖肤色、少量身份色与红橙蓝批注。

### 2. 平涂插画

![平涂插画风格母板](xinju-ip-illustrations/assets/style/flat-color-style-board.png)

单一主色场、几何平涂造型、克制的空间明暗与硬边投影。

### 3. 拼贴漫画

![拼贴漫画风格母板](xinju-ip-illustrations/assets/style/collage-style-board.png)

有色纸面、半调纸偶、手工裁切质感与少量中文批注。

## 安装

克隆仓库：

```bash
git clone https://github.com/X-leader/xinju-ip-illustrations.git
cd xinju-ip-illustrations
```

复制 Skill 到 Codex Skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R ./xinju-ip-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

也可以在 Codex 中直接请求：

```text
请从 https://github.com/X-leader/xinju-ip-illustrations
安装 xinju-ip-illustrations Skill。
```

## 使用方法

### 为正文设计配图

```text
使用 $xinju-ip-illustrations，为下面这段中文正文设计配图：

<粘贴正文>
```

Skill 会先输出配图方案和三种风格选项。确认方案与风格后，才会逐张生成图片。

### 上传真人照片并替换人物

```text
使用 $xinju-ip-illustrations，
用我上传的真人照片生成迷你人物 IP，并直接替换活动人物。
```

只应上传用户本人或已经获得授权的人物照片。原始照片不会成为本仓库的公开资产。

### 上传已有人物 IP

```text
使用 $xinju-ip-illustrations，
把我上传的完整人物 IP 直接设为活动人物。
```

### 恢复默认 Xinju

```text
使用 $xinju-ip-illustrations，恢复 Xinju。
```

更多可复制的调用方式见 [`examples/prompts.md`](examples/prompts.md)。

## 更新提示

重新复制仓库中的 Skill 会把活动人物恢复为仓库自带的 Xinju。已经设置自定义人物的用户，应在更新前自行备份：

```text
xinju-ip-illustrations/assets/ip/active-ip-four-view.png
xinju-ip-illustrations/references/character-ip.md
```

## 隐私

- 仓库只包含内置 Xinju 母板和公开风格资产。
- 原始真人照片、私人 IP、测试人物档案和测试输出不得提交到仓库。
- 人物替换只修改用户本地安装目录中的当前活动母板与档案。
- Skill 不提供人物历史列表，也不会自动保存上一位人物。

## 项目结构

```text
.
├── README.md
├── LICENSE
├── NOTICE.md
├── THIRD_PARTY_NOTICES.md
├── examples/
│   └── prompts.md
├── tools/
│   └── verify_release.py
└── xinju-ip-illustrations/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── references/
    └── scripts/
```

## 许可证

Skill 规则、脚本和普通文档采用 [MIT License](LICENSE)。Xinju 人物母板、角色形象和品牌资产不包含在 MIT 授权范围内，使用规则见 [`NOTICE.md`](NOTICE.md) 和 [`assets/ip/ASSET_LICENSE.md`](xinju-ip-illustrations/assets/ip/ASSET_LICENSE.md)。

## 致谢与来源

本项目的早期工作流设计、正文配图方法和部分规则组织方式基于或参考了 Ian 创建的 [Ian Xiaohei Illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) 与 [Ian Xiaohei Scenes](https://github.com/helloianneo/ian-xiaohei-scenes)。原项目采用 MIT License。

本项目已针对 Xinju 人物 IP、三种渲染风格、活动人物替换、构图控制、物件预算、中文方案确认与自动 QA 流程进行了修改和扩展。完整第三方声明见 [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md)。
