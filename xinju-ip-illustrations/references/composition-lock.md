# 统一构图与占比锁

本文件是手绘线稿、平涂插画和拼贴漫画唯一有效的构图来源。三种风格共享同一内容构图母版；风格文件只改变线条、色面、材质、背景与阴影，不另设占比或缩放规则。

本文件把构图规则分为两层：

- **生图指导**：首次 Prompt 使用一个刻意偏保守的生成目标和一组边界锚点，用来抵消模型自然放大主体的倾向，避免多个区间互相干扰。
- **生成后 QA**：用视觉重量、空白比例和风格一致性做精细验收，不把这些抽象测量重复塞进 Prompt。

## 生图指导

- 使用方案中确认的画幅；默认 16:9 横版，其他比例必须原生构图。
- 把当前活动人物、默认一个核心物件、必要输入输出、箭头、短标注，以及人物头发最高点、鞋底、投影、动作线、拼贴裁切边等最外侧可见元素视为一个完整视觉组；仅在第二个物件具有不可替代的因果职责时保留它。元素计数与细节预算执行 `composition-patterns.md`。
- 完整视觉组应当居中、清楚、容易阅读，不能偏压单侧，也不能缩成漂浮在中央的小图。首稿目标略小于最终期望，是生成偏置，不是要求成图必须显得小。
- 普通横版首稿只瞄准一个保守标称尺寸：完整视觉组约占画布 74% 宽、60% 高，边界大致落在 x=13%–87%、y=20%–80%。
- 横版 Workflow 首稿只瞄准一个保守标称尺寸：完整视觉组约占画布 76% 宽、60% 高，边界大致落在 x=12%–88%、y=20%–80%。
- 所有短标注、箭头端点、输入输出、动作线、头发尖端、鞋底、投影和拼贴外缘都必须收在同一个完整视觉组边界内；先布置全部元素，再用真正最外侧的四个锚点复核边界。不能用一条孤立文字、卡片、牌子、箭头、阴影或装饰边把外接范围顶到画布边缘。
- “巨大主物件”只表示它相对迷你人物巨大；相对画布仍应保持中等尺度和完整白边，绝不等于铺满画布。
- 四周都要有连续、可感知的负空间。允许区间、安静负空间和感知视觉重量只用于生成后 QA，不写进首次 Prompt。
- 所有元素不得贴边或裁切。若数字冲突，依次优先：不裁切 → 安全边距 → 平衡的视觉中心 → 近似主体尺寸。

## 三种风格一致性

同一内容生成多种风格时，先锁定一份内容构图母版，再分别渲染：

- 人物脚底、最高物件、最左输入和最右输出大致落在同一组构图坐标内。
- 人物、物件、文字、动作、接触关系、相对大小和信息方向保持一致。
- 平涂的硬边投影和拼贴的裁切边、叠纸阴影不能成为缩小核心视觉组的理由；线稿也不能因颜色轻而放大到贴边。

## 横版 Workflow

- 保持 3–5 个因果相连的节点、一条主路径和中央最大处理物；活动人物只操作决定性转换。
- 输入、输出、短标签和动作提示优先嵌入中央处理物的入口、出口或紧贴其轮廓，形成一个整合轮廓；不要在主物件之外悬挂独立卡片、牌子或醒目标记。确有必要外置时，它仍必须位于同一安全框内并计入完整视觉组边界。
- 完整流程宽度约占画布 80%–86%，同时保留清楚的四周留白。
- 横向延展不等于铺满全宽，也不能压成又矮又长的细条。
- 竖版不套用横向跨度，改用自上而下、S 形或错层纵向流程。

## 横版纵向呼吸

- 16:9 横版优先使用横向展开、低矮团块、浅对角线或环形构图，避免把人物、主物件、标签和输出连续向上堆叠。人物位于巨大物件顶部、悬挂在物件下方或跨坐环形结构时，也必须先检查真实最高点与最低点。
- 顶部和底部都要保留连续、安静、可感知的背景带。顶部不放孤立标题、箭头尖端、发梢或注意符号；底部不让鞋底、接触阴影、硬边投影、运动线或拼贴撕纸边压住画布边缘。
- 发现构图过高时，依次处理：减少纵向堆叠 → 把人物移动到物件侧面、斜侧或较低的操作位 → 将输入输出改为横向或紧贴主物件 → 收紧投影、箭头和动作线 → 最后才等比缩放完整视觉组。
- 上述调整用于首次构图设计，不得改变核心因果、人物决定性动作、物件身份或必须文字。目标是增加上下呼吸，同时保留横向存在感，不能把内容缩成中央小图。

## 中间尺度构图规则

中间尺度是三种风格的新默认，不是临时候选：它位于“几乎铺满画面”和“缩成中央小图”之间，让主体保持清晰存在感，同时给四周留出可感知的呼吸空间。

- 量化对象始终是人物、主物件、输入输出、路径、箭头、所有短标注、人物头发与鞋底、投影、动作线和拼贴外缘组成的完整视觉组。不要只量人物，也不要用白色像素比例代替负空间判断；线稿物件内部可能含有大量白色。
- 普通横版以约 76%–84% 宽为默认区间；横版 Workflow 以约 80%–86% 宽为默认区间。两者的高度均可参考约 58%–68%。
- 左右各保留约 8% 连续白边或背景区，上下各保留约 16%–20%。留白必须分布在四周，不能全部集中在一侧；顶部与底部都应形成可直接看见的连续背景带。
- 尺度调整必须作用于完整视觉组，并保持人物、物件、文字、箭头、动作、接触关系和内部相对坐标不变；不得逐个移动节点来拼凑边距。
- 修正前先比较当前宽度与 QA 允许区间；需要修正时，在 Prompt 中写明当前估算值、相对缩放方向和一个标称目标。普通横版修正到约 80% 宽、64% 高，横版 Workflow 修正到约 83% 宽、64% 高；不要把整个允许区间和多套下限一起写回修正 Prompt。只写“缩小一点”或“增加留白”也不够。
- 已有过满版本和过度缩小版本都只作为尺度边界参考。编辑时从当前最佳版本出发，不在较差版本上继续缩放或补救。
- 普通横版高于约 84%、Workflow 高于约 86%，或低于各自参考下限时，先标记为“尺度观察项”，不能仅凭百分比判定失败。只有同时出现贴边、裁切、明显空间压迫、明显偏心、四周留白断裂，或小到动作与文字难以阅读时，才属于需要修正的构图硬缺陷。
- 若一次修正跨过目标区间、把主体缩成中央小图，或虽增加留白却削弱动作、文字可读性和记忆点，则判定为过度修正；按最佳版本保护规则回退。
- 宽度、高度和四边留白无法同时精确命中时，继续执行既有优先级：不裁切 → 安全边距 → 平衡的视觉中心 → 近似主体尺寸。不要为了追逐单个百分比破坏内容。

## 生图 Prompt 构图锁定块

每次生图都把下列内容放在画幅与参考图职责之后、内容锁之前，使构图成为最高优先级：

```text
Unified composition lock — highest priority and mandatory for every style:
Treat the active character, the core object, arrows, input/output, short labels, hair tips, soles, cast shadows, motion marks and collage cut edges as one complete visual group. Keep the group centered, substantial and easy to read, without pushing it toward one side.

Use one conservative first-pass generation target, not a range. This smaller target compensates for the model's tendency to enlarge the subject; it is not the final QA target. For a standard horizontal composition, place the complete visual group at about 74% of canvas width and 60% of canvas height, approximately inside x=13%–87% and y=20%–80%. For a horizontal Workflow, use about 76% width and 60% height, approximately inside x=12%–88% and y=20%–80%.

Lay out every label, arrow tip, motion mark, input, output, hair tip, sole, shadow and collage edge before checking the four outermost anchors, then keep all of them inside the same group boundary. In a Workflow, integrate input/output symbols and short labels into the central machine's inlet, outlet or immediate silhouette; do not add detached external cards, signboards or attention marks. “Giant object” means giant relative to the miniature character, never giant relative to the canvas.

Preserve clear continuous whitespace on all four sides, with visibly calm uninterrupted background bands above and below the complete group. Prefer a horizontally distributed, low-slung arrangement for 16:9. If the plan becomes too tall, reduce vertical stacking and move the character toward a side, diagonal or lower operating position before scaling the whole group. Crop nothing, keep every element away from the canvas edge, do not shrink the scene into a small central icon, and do not flatten it into a thin strip.

For the same content rendered in multiple styles, preserve approximately the same composition coordinates, relative scale, action, contact, labels and information direction. Style may change only line, color planes, material, background and shadow.

If any numerical requirements conflict, prioritize: no cropping, safe margins, balanced visual center, then approximate size.
```

## 生成后 QA 指标

以下数值只用于生成后观察与比较，不是自动触发修正的硬阈值，也不原样加入生图 Prompt：

- 感知视觉重量建议保持约 55%–60%；低于约 50% 视为主体过轻，高于约 60% 视为画面过满。
- 安静负空间不得少于约 35%，并检查是否全部堆在同一侧。
- 普通构图宽度参考 76%–84%；横版 Workflow 宽度参考 80%–86%；高度可参考约 58%–68%。高度百分比单独越界永远不触发修正；只要没有贴边、裁切、明显压迫或失衡，就接受初稿。
- 检查左右、上下是否明显失衡，顶部与底部是否都保留连续背景带，以及是否出现贴边、裁切、纵向堆叠压迫或中央小图。
- 同一内容的三种风格应保持相近的内容坐标、整体尺寸和上下留白。
- 构图修正后同时对比修正前后版本：修正版必须更接近目标区间，且不能从“过满”直接跳成“过小”。若偏差方向反转且绝对偏差没有明显下降，视为修正失败。

QA 时先检查不裁切与安全边距，再检查是否存在肉眼可见的空间压迫或失衡，最后才记录近似尺寸和视觉重量。任何宽高百分比偏差本身都属于软偏差；只有出现贴边、裁切、明显中央小图、单侧压迫或阅读受损时才触发修正。不要为追逐单一百分比破坏动作、人物质感、身份或叙事关系。
