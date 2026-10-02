# 拼贴漫画

选择“拼贴漫画”时使用；兼容“纸偶批注拼贴”“拼贴风格”“半调纸拼贴”或“纸偶”等旧称。这里的“漫画”指单幅编辑式拼贴，不生成多格分镜或对白气泡。若用户明确要求 Google Flow 动画提示词或拼贴动画，改用相应拼贴动画 Skill。

## 定义

保留本 Skill 的怪诞动作隐喻、活动 IP、巨大物件、大留白和中文手写批注，把人物与物件转换成具有半调印刷、手工裁切、纸片关节和叠纸阴影的编辑式纸拼贴。

## 生成输入

- 同时输入唯一活动身份参考 `assets/ip/active-ip-four-view.png` 与风格母板 `assets/style/collage-style-board.png`。活动母板只锁人物身份；风格母板只锁纸片、半调、裁切边与叠纸阴影，不得复制其示例姿势、局部物件或排布。

## 背景纸场

- 使用一种强烈、平坦、连续的有色纸面，如墨绿、深紫、焦橙、钴蓝或灰粉。
- 背景只保留细微均匀的无涂层纸张颗粒；不使用渐变、场景透视、装饰碎片或拼接色块。
- 完整拼贴视觉组严格执行 `composition-lock.md`；裁切边、半调密度和叠纸阴影不得成为缩小、放大或偏移共享构图的理由。

## 活动人物半调纸偶

- 人物身份轮廓只执行 `character-ip.md`；风格母板只提供纸偶转译。人物存在眼镜时才转换为独立纸层；头发转换为少量相连纸片层，但不得改变当前档案中的原有轮廓。
- 人物由头部、躯干、双臂和双腿等少量独立纸片构成，关节处自然重叠并有轻微纸片阴影。
- 面部、皮肤和服装暗部使用可见黑色半调网点；服装身份色按 `character-ip.md` 转译为半调印刷。
- 发型使用一块主纸片与少量相连发束层，数量和轮廓服从当前人物档案；不得变成光滑圆盔或满头漂浮碎纸。只有当前人物佩戴眼镜时才增加独立眼镜纸层。
- 整体使用略不均匀的奶油白手工裁切边和柔和低透明投影；允许轻微套印错位，但不能影响身份与动作。

## 物件与批注

- 巨大物件由 3–5 组大卡纸构成，优先形成一个清楚的整体轮廓，只保留动作接触点和必要功能结构；不要用碎小纸片模拟螺丝、面板、接口、线缆或内部机械。
- 依靠遮挡、叠层、切边和局部投影表达结构，不使用 3D 高光。
- 保留 3–5 处中文手写短词。黑色用于主体说明，红色用于问题或压力，橙色用于动作与流程，蓝色用于系统或补充状态。
- 深色背景上可为文字增加极细奶油白底边，但不能变成标签卡、标题条或按钮。

## Prompt 渲染块

```text
Selected style: Editorial Collage Comic / 拼贴漫画.

Use one strong, flat, continuous colored paper field with subtle uniform uncoated paper grain. Render the oversized metaphor object from 3–5 large colored-cardstock groups that form one immediately readable silhouette, with crisp scissor-cut edges, warm-cream keylines, restrained printed patterns, visible paper thickness and soft local stacking shadows. Keep only the decisive contact point and necessary functional structure; do not simulate bolts, panels, ports, cables or internal machinery with small scraps.

Render the active identity defined in `character-ip.md` as an articulated editorial paper puppet. Use separate but anatomically coherent head, torso, arm and leg paper pieces; visible black halftone dots on skin and clothing shadows; the current profile's 2–4 identity colors as halftone print; one main hair piece plus a few connected layers matching the recorded hairstyle; an independent glasses layer only when the active character wears glasses; slightly uneven warm-cream cut borders; subtle joint overlaps, ink misregistration and low-opacity paper shadows. Translate all identity-sheet 3D or photographic material into paper, ink and halftone treatment while preserving the current action, expression and contact. Copy no pose, object or layout from the style board, and never mix in the inactive Xinju backup identity.

Include 3–5 short, correctly written Chinese handwritten notes close to their corresponding objects, using black, red, orange and blue semantically. Keep one metaphor, one giant object by default, a second object only for an irreplaceable causal role, and an action-led expression. Execute the shared `composition-lock.md` without changing the locked coordinates, scale or margins. Select pose, expression, object relationship and spatial topology from the current meaning rather than any previous image.

No photoreal face, plain line-art sticker character, dense scrapbook, vintage newspaper collage, random torn scraps, background gradient, glossy 3D, corporate vector style, PPT layout, multi-panel comic, speech bubble, title banner, extra limbs, extra characters, watermark or unreadable text.
```
