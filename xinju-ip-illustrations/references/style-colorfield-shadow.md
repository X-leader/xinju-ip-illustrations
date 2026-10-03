# 平涂插画

选择“平涂插画”时使用；兼容“色场影构”“几何色场硬影”“几何扁平”或“硬边光影”等旧称。

## 定义

以当前活动人物的怪诞动作隐喻和大留白构图为骨架，用单一主色场、概括几何色面与有明确物理来源的硬边投影完成视觉呈现。风格只改变渲染，不改变内容、IP、动作、文字和构图。

## 生成输入

- 同时输入唯一活动身份参考 `assets/ip/active-ip-four-view.png` 与风格母板 `assets/style/flat-color-style-board.png`。活动母板只锁人物身份；风格母板只锁前景人物与物件的几何色面、边缘和硬边投影，不得复制其示例姿势、局部物件、排布或背景明暗。背景执行下方“主色场与空间层次锁”，母板背景不具约束力。
- 参考图的柔和 3D 明暗、发丝高光、空气感皮肤、写实布褶、牛仔纹理和立体鞋面细节不属于身份特征，禁止带入平涂结果。

## 渲染规则

- 在 Prompt 中先选择并写明一个确定的背景主色名称与近似 HEX 值；整张画布以这一主色铺底。允许在同一色相家族内加入宽而柔和的中心提亮、平缓径向明暗过渡和轻微边缘压暗，为主体提供初版式空间层次。
- 背景仍应读作简洁的设计色场，而不是写实环境。禁止高反差聚光、舞台光圈、明显天空或地平线、局部彩色光源和抢夺主体的暗角；柔和中心光与轻微暗角本身不是缺陷。
- 人物和物件由少量大几何色面、清楚轮廓和克制切面构成，几乎不使用外轮廓线。
- 核心物件优先由少量大色面建立一个清楚轮廓，只保留与动作、接触和输入输出有关的功能切面；禁止用大量小色块模拟按钮、螺丝、面板、接口或内部机械。
- 人物必须和主物件共享完全相同的几何平涂语言：不能把线稿人物、黑边贴纸人物或带白色排线的手绘人物叠在平涂场景里。
- 前景人物和物件用相邻色块的明度、冷暖和遮挡区分结构，不使用光滑 3D 材质；背景允许上述克制的柔和明暗过渡。
- 只允许由可见主体产生的硬边投影。投影必须与物件连接、方向一致，并表达重量、动作方向或空间关系。
- 硬边投影作为独立扁平色块叠在背景之上；背景的柔和中心提亮只负责空间层次，不能替代主体真实接触产生的硬边投影。
- 保留轻微手工裁切的不规则感，避免企业矢量素材感。
- 完整视觉组严格执行 `composition-lock.md`；平涂色块和硬边投影不得成为缩小、放大或偏移共享构图的理由。
- 中文批注保持少、短、手写；可用黑、红、橙、蓝或适配背景的高对比色。
- 本模式优先在首次生成同时锁定内容、构图、前景渲染和背景层次，不预设“生成后再压平背景”的步骤。柔和中心提亮、同色相明暗过渡和轻微暗角应直接保留；只有背景光影强到抢夺主体、削弱文字可读性或形成写实场景时才触发修正。

## 主色场与空间层次锁

每次平涂插画都在渲染块开头原样加入：

```text
Dominant background field with gentle spatial depth — establish in the first generation:
Choose one dominant background color and state both its plain-language name and approximate HEX value. Fill the full canvas with that color family before placing foreground elements. Allow a broad soft center lift, a smooth low-contrast radial tonal transition and gentle edge darkening within the same hue family, similar to restrained editorial studio depth. Keep the transition calm and subordinate to the subject; do not force edge-to-center uniformity and do not schedule a later flattening edit merely because this soft depth is visible. Do not derive the pose, expression, composition or objects from any previous illustration. Use the current content brief and these flat-color rules.

Avoid a hard spotlight circle, high-contrast vignette, dramatic stage lighting, realistic room illumination, horizon, sky, atmospheric scenery, multicolor glow, decorative background polygon or any background effect that competes with the foreground. Cast shadows remain separate crisp flat shapes visibly attached to foreground objects and should coexist with, not be replaced by, the soft background depth.
```

## 人物平涂转译锁

每次平涂插画含人物时，在“主色场与空间层次锁”之后原样加入：

```text
Flat-character translation lock — identity without reference-style leakage:
Use the active character sheet only for the identity geometry defined in `character-ip.md`; use the flat-color style board only for rendering language. Copy no pose, object, layout or background arrangement from either reference. Never mix in the inactive Xinju backup identity.

Translate that identity completely into the same flat geometric language as the scene objects. Do not copy the reference sheet's soft 3D modeling, glossy strand highlights, airbrushed skin or shadows, realistic clothing folds, denim texture, dimensional sneaker detail, studio lighting or white model-sheet background. Build the layered hair from 4–7 connected dark flat planes with no individual glossy strands. Build the glasses as one clean oversized dark flat frame shape. Build skin, T-shirt, jeans, shoes, hands and facial features from broad opaque color shapes with only 1–2 necessary structural facets; simplify ankle stacking and chunky shoe volume without losing their silhouettes. Separate forms through adjacent color, value contrast and occlusion; use almost no enclosing black outline. Keep the required visible mouth readable as a simple flat mark whose shape follows the action.

The active character and every oversized object must look authored by the same illustrator, with matching edge language, faceting, palette logic and hard-shadow direction. Reject any result where the character reads as a hand-drawn sticker, outlined cartoon or imported line-art layer on top of a flat-color scene.
```

## 单次生成顺序

在同一个 Prompt 中依次写：

1. 构图锁：在画幅与参考图职责之后，按当前画幅加入 `composition-lock.md` 的生图 Prompt 构图锁定块。
2. 内容锁：核心判断、一个隐喻、默认一个巨大主物件、活动人物的决定性动作、动作驱动表情、必要文字；第二个物件仅在具有不可替代的因果职责时加入。
3. 渲染锁：先加入“主色场与空间层次锁”，再原样加入“人物平涂转译锁”，并写几何色面、综合色彩与硬边投影。
4. 最终检查：当前内容、动作去重、构图锁和本文件的文字渲染规则全部通过。

## Prompt 渲染块

```text
Selected style: Flat Color Illustration / 平涂插画.

Start with the full `Dominant background field with gentle spatial depth` lock above, then include the full `Flat-character translation lock`. Render on one full-bleed dominant color family with a broad soft center lift, smooth low-contrast tonal transition and gentle edge darkening. Build the active character and oversized metaphor object from broad flat geometric color planes, clear silhouettes, restrained faceting and almost no outlines. Use a controlled high-contrast foreground palette appropriate to the scene. Add hard-edged cast shadows only as separate crisp shapes that visibly originate from foreground objects and help explain weight, force or direction. Preserve slight hand-cut irregularity.

Keep the current content and the shared `composition-lock.md` mandatory: one metaphor, one dominant giant object by default, a second object only for an irreplaceable causal role, the active character performing the decisive action without overpowering the core structure, and sparse correctly written Chinese handwritten notes. Select pose, expression, object relationship and spatial topology from the current meaning rather than any previous image.

No hand-drawn or heavily outlined character, no white hair hatching, no scratch texture, no line-art sticker effect, no decorative background polygons, unrelated shadows, hard spotlight circle, high-contrast vignette, dramatic stage lighting, realistic room light, glossy 3D, dense UI, corporate vector-stock styling, title banner or watermark. Complete the intended soft background depth in the first generation; preserve a tasteful initial center lift and do not schedule a later flattening edit unless the background actually overpowers the subject or harms readability.
```
