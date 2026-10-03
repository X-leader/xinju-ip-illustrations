# 标准生图 Prompt 模板

每张图单独生成。含人物时同时输入唯一身份参考和所选风格母板，并在 Prompt 中明确分工：四视图只负责身份，风格母板只负责渲染，当前方案独立决定内容与构图。

## 风格路由

- 用户针对当前最新方案回复有效风格编号后，立即组装生图 Prompt；该编号同时表示采用方案和确认最终风格，不再询问第二次确认。未收到有效编号时停在方案阶段，提供三种选项，不自动采用手绘线稿。
- 用户回复 `1` 或明确选择手绘线稿：使用下方完整“手绘线稿”模板。
- 平涂插画：使用 `assets/style/flat-color-style-board.png` 与该风格文件中的“主色场与空间层次锁”“人物平涂转译锁”；首次生成直接完成单一主色调与克制的背景层次。
- 拼贴漫画：使用 `assets/style/collage-style-board.png`，并用该风格文件的渲染块替换手绘渲染块。
- 手绘线稿：使用 `assets/style/lineart-style-board.png`。三张母板都只能提供边缘、线面、材质、色场与阴影语言，不能提供场景内容或排布。

新增风格必须在同一个 Prompt 中按“画幅与参考图职责 → 构图锁（最高优先级）→ 内容锁 → 人物身份锁 → 渲染锁 → 最终文字检查”排序。构图与当前内容优先于风格文字规则。

所有风格都必须读取 `composition-lock.md`，并按当前画幅使用其中“生图 Prompt 构图锁定块”。16:9 使用完整块，其他画幅只替换布局坐标一句；一次 Prompt 只保留一种画幅的布局意图。该区域用于容纳完整视觉组，不要求宽高同时填满；不加入额外 QA 比例或修正比例。该文件是唯一占比来源，风格块不得另写一套数字。

组装 Prompt 前先做一次不展示给用户的布局预检：先摆放人物、主物件、输入输出、必须文字、箭头、动作线、注意符号、人物头发与鞋底、平涂硬边投影、接触阴影和拼贴裁切外缘，再列出完整视觉组最左、最右、最高和最低的真实元素；给人物、巨大主物件和必须文字分配互不冲突的区域，并确认所有元素都位于同一个安全框内。16:9 横版优先使用横向展开、低矮团块、浅对角线或环形关系；如果结构过高，先减少纵向堆叠，把人物移向侧面、斜侧或较低操作位，并收紧阴影与动作线，最后才整体缩放。若某个可选批注会成为孤立的边缘外点，直接省略或内移。Workflow 的输入输出与短标签优先嵌入中央处理物的入口、出口或紧贴其轮廓，不外挂卡片或牌子。“巨大”只描述物件相对迷你人物的尺度差，不表示物件相对画布铺满。

将预检结果压缩成 `Composition` 的 2–3 句具体摆放描述：人物在哪个接触点、最高与最低元素是什么、文字与箭头贴近哪个物件。给文字分配位置后再估计完整视觉组，不能先占满区域再在顶端或底端追加标签。保持场景自然宽高关系；普通结构与 Workflow 共用同一布局区域，无需加入另一套填满要求。

在最终 Prompt 前增加一个简短的 `Variation lock`：写明本图选用的动作族、表情族、人物朝向、人与物件的接触关系和构图骨架。与当前正文、短口播或可见对话中的近期配图比较；语义不要求重复时，五个变化轴中至少更换两项。禁止自动选择“侧面推巨大物件＋眯眼咬牙＋眼镜滑落＋左入右出”。

## 中文文字锁

- 组装 Prompt 前把文字分成 `Required exact Chinese text` 与 `Optional atmosphere notes`。前者必须逐字出现；后者可以省略，不能用近似字、乱码或擅自补词代替。
- 必须文字优先压缩成 2–6 个汉字的短词并横排；单处通常不超过 8 个汉字。超过 3 个汉字时不要竖排在窄标签、箭头或细长物件上。
- 单张默认只保留 3–5 处需要阅读的短标注；手绘线稿在内容确有必要时可增加，但总数仍不得超过其风格上限。重复含义合并成一处。
- 专有名词、产品名或用户指定原句属于必须文字，不得改写。长句无法稳定呈现时，在方案阶段先建议压缩；用户要求原文时保留原文，并把文字准确性列为硬性检查。
- Prompt 中逐项列出准确文本，使用中文引号包裹，不要求模型自行总结标签。没有必须文字时明确写 `No required exact text`。

## 精简活动角色锁定块

```text
Recurring active personal IP character required:
Use Image 1, `assets/ip/active-ip-four-view.png`, only for the current identity geometry defined in `character-ip.md`: compact approximately 1:3 miniature-human proportion, enlarged head without infant anatomy, recorded hairstyle, face, optional glasses, clothing silhouettes, footwear, accessories and identity colors. Use Image 2, the selected style board, only for rendering language. Never copy either reference's sample pose, layout, object, background arrangement or expression. Never mix in any inactive or default character identity.
Preserve a readable action-linked mouth whenever the face is visible. Keep exactly one head, one torso, two arms, two hands, two legs and two feet with coherent joints; natural occlusion is allowed. Translate hair, glasses, skin and clothing completely into the selected style. No reference-sheet 3D material, infant chibi, anime, mascot, black blob, elongated adult body, sparse spikes, floating hair or extra limbs.
For hand-drawn line-art mode, use a black-and-white character with one restrained light warm peach skin-tone fill plus only the 1–2 localized identity colors listed in `character-ip.md`: fill all visible face, ears, neck, arms and hands completely with one flat, matte, even light warm peach tone while preserving black contours; translate the recorded hairstyle with controlled directional hatching; render glasses only if the current profile includes them; simplify clothing and footwear without changing their silhouettes. No unfilled paper-white skin gaps, blush, gradients, highlights, soft 3D shading, glossy hair or realistic material. Do not import Xinju-specific blue jeans, glasses or hair into another active identity.
```

## 手绘线稿单张正文或短口播静态配图标准模板

```text
Generate one standalone static illustration for Chinese article text or a short spoken script in the confirmed canvas format.

Canvas:
{已确认的画幅，例如 16:9 horizontal、9:16 portrait 或 1:1 square；必须原生构图，不以其他比例裁切代替}

Reference image roles:
Image 1 is the sole identity reference. Image 2 is a style-only board. Copy no pose, object, layout, annotation or composition from either image.

Unified composition lock — highest priority:
{使用 composition-lock.md 的“生图 Prompt 构图锁定块”；只保留当前画幅的布局句，不在其他段落重复构图数字}

Theme:
{正文或短口播配图主题}

Core idea:
{一张图只表达的核心判断、状态或隐喻}

Structure type:
{Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core physical action:
{角色正在拉、扛、塞、捞、压、称、缝、剪、拧、守、推、接、拆、标记、回收或操作什么}

Action-linked expression and body distortion:
{根据物理动作明确眼睛、眉毛、嘴、眼镜角度、脖子、四肢和重心如何变化。只要脸部可见，就必须写明并画出可读的嘴形，不得省略。表情必须与动作因果一致，可夸张怪诞，但不能改变身份特征。}

Composition:
{角色位置、默认一个相对迷你人物巨大的核心物件、尺度反差、信息流向，以及完整视觉组如何以低矮、横向有存在感的方式收拢至画面中央并保留上下安静背景带；这里不重复尺寸数字。只有第二个物件承担不可替代的因果职责时才加入}

Essential object plan:
Core object: {一个轮廓清楚且去掉文字后仍可识别的物件；普通概念物件保留 2–4 处有效细节，产品、工作台、节点编辑器或系统局部保留 4–6 处有效细节}
Decisive action: {活动人物只执行一个造成核心变化的动作}
Compact input or state group: {没有则写 None}
Compact output group: {没有则写 None；有必要辅助物时优先把输出并入主物件}
Supporting prop: {没有则写 None；最多一个}
Meaningful detail plan: {分别写身份细节、操作细节、叙事细节；不适用时写 None，不为凑数增加零件}
Material or structural cue: {最多一组克制且统一的材质或结构特征；没有则写 None}

Chinese handwritten labels:
Required exact Chinese text: {必须逐字准确的标注词；没有则写 No required exact text}
Optional atmosphere notes: {可省略的短批注}
Render required text exactly as listed, preferably horizontal. Never invent, paraphrase or approximate Chinese characters. Omit an optional note rather than render it incorrectly. Do not place more than 3 Chinese characters vertically on a narrow label, arrow or elongated object.

Recurring personal IP character required:
{原样加入上方“精简角色锁定块”，不要再次扩写人物描述}

Visual DNA:
Pure white background. Extremely minimal black hand-drawn line art with thin-to-medium, slightly wobbly pen strokes. Lots of untouched white space. The active character is black-and-white line art with one flat light warm peach skin-tone fill plus only 1–2 localized identity colors defined in `character-ip.md`: all visible face, ears, neck, arms and hands use the same even matte skin color; hair, optional glasses, clothing and shoes preserve the current identity anchors without photographic or 3D material. Objects remain predominantly black-and-white; sparse red, orange, and blue handwritten Chinese annotations provide semantic accents. Clean, absurd editorial product-sketch feeling. No blush, skin gradients, soft 3D shading, realistic material, shadows, paper texture, gray background, realistic UI, commercial vector style, PPT infographic, polished mascot poster, or children's illustration.

Color use:
Use black for main line art, text, structural objects and the darkest identity anchors. Fill the active character's visible face, ears, neck, arms and hands completely with one restrained light warm peach tone while keeping black contours crisp. The skin fill must be flat, matte and even; do not let it spill into eyes, glasses, hair, clothing, objects or background. Preserve only the 1–2 localized clothing or accessory colors defined in `character-ip.md`, using light same-color and paper-white sketch hatching; keep all other clothing areas paper-white. No unfilled skin gaps, blush, airbrushed skin, highlights, shadows, volume gradients, glossy hair or realistic fabric texture. Orange marks the main flow, movement or path. Red marks key warnings, problems, tension or results. Blue marks secondary notes, feedback or system state. Never import identity colors from an inactive character.

Composition constraints:
One image explains only one core structure. The active character performs the decisive action without overpowering the oversized object or core structure. “Oversized” means oversized relative to the miniature character, not relative to the canvas. Humor comes from scale mismatch, serious work, and action-linked physical distortion—not decorative cuteness.
Apply the readable-detail budget from `composition-patterns.md`. Use at most four visible roles: the active character, one core object, one compact input/state group, and one compact output group or necessary supporting prop. Show one decisive action only. Keep one recognizable outer silhouette and direct contact point, but do not reduce the object to a generic box, disc, button set or text-dependent card. Use 2–4 meaningful details for an ordinary conceptual object, or 4–6 for a product, workbench, node editor or system detail. Details may only establish object identity, character operation and causal narrative; preserve at most one restrained material or structural cue family. Do not turn parallel concepts into separate machines or equal-weight islands. The viewer must notice the character's action and causal change first, then recognize a second layer of designed object detail.

Anatomy integrity — hard requirement:
Exactly one head, one torso, two arms, two hands, two legs and two feet unless a part is naturally hidden by valid occlusion. Every visible limb must connect through coherent joints. No extra, duplicated, branched, detached, merged or floating hands, arms, legs or feet.

Avoid:
No reference-sheet 3D material, infant chibi, anime, mascot, black-blob body, missing mouth, identity drift, extra limbs, decorative character, over-detailed machine, repeated panels or bolts, exposed internal machinery, formal flowchart, UI cards, detached external labels or signboards, large title, watermark, unreadable text, edge-hugging, cropping, one-sided balance or scattered equal-weight islands.

Final exact-text check:
Render every item under `Required exact Chinese text` exactly once and exactly as written. Omit optional notes if uncertain. Change no required wording.
```

## 定向迭代短句

角色不一致：

```text
Keep the confirmed content and composition unchanged. Reapply Image 1 only for the active identity and Image 2 only for the selected rendering style. Restore only the identity anchors defined in `character-ip.md`, preserve coherent anatomy and the action-linked mouth, remove reference-sheet 3D or photographic material, and remove every inactive-character trait. Do not copy either reference's pose, object or layout.
```

手绘线稿人物颜色或材质不统一：

```text
Keep all content, composition, identity, action, expression, objects and labels unchanged. Redraw only the active character's color treatment in hand-drawn line-art mode. Fill all visible face, ears, neck, arms and hands completely with one flat, matte, even light warm peach skin tone while preserving crisp black contours. Remove paper-white skin gaps, blush, gradients, highlights and shadows. Restore the hairstyle, optional glasses, clothing silhouettes and only the 1–2 localized identity colors defined in `character-ip.md`. Remove soft 3D shading, glossy strand highlights, airbrushed skin, realistic fabric texture and every inactive-character trait.
```

表情与动作脱节：

```text
Keep the composition and identity unchanged. Redesign only the facial expression and body language so they are a direct physical consequence of the action. Push the eyes, eyebrows, mouth, glasses angle, neck, limbs, and center of gravity into a clearer, stranger caricature without making the character cute.
```

人体结构错误：

```text
Keep the confirmed content, composition, style, identity, action and expression unchanged. Correct only the anatomy: exactly one head, one torso, two arms, two hands, two legs and two feet, allowing only natural occlusion. Connect every visible hand to one arm, every foot to one leg and every limb to the torso through coherent joints. Remove any extra, duplicated, branched, detached, merged or floating limb without changing the action.
```

角色太装饰：

```text
Keep the core meaning and sparse layout, but make the miniature IP physically perform the conceptual action. The idea should become visible through what the character is pulling, carrying, repairing, sorting, or operating—not through a diagram beside him.
```

物件过于简单：

```text
Keep the confirmed meaning, character identity, decisive action, contact point, labels, composition scale and selected style unchanged. Enrich only the core object until it is recognizable without relying on text. Preserve one outer silhouette and add only missing meaningful details: object-identity cues, the character's operation point, the causal input/output or state change, plus at most one restrained material or structural cue family. Use 2–4 meaningful details for an ordinary conceptual object, or 4–6 for a product, workbench, node editor or system detail. Add no new object, character, action, label, detached card or decorative machinery. The action and causal change must remain the first read.
```

物件过度复杂：

```text
Keep the confirmed meaning, character identity, decisive action, contact point, labels, composition scale and selected style unchanged. Simplify only the objects by following the deletion ladder in `composition-patterns.md`: remove decorative internals; merge repeated gauges, modules and states; merge input/output symbols; remove the supporting prop; remove every secondary action. Preserve one clear outer silhouette, the identity cue, operation point, causal detail and at most one restrained material or structural cue family. Retain 2–4 meaningful details for an ordinary conceptual object, or 4–6 for a product, workbench, node editor or system detail; do not collapse the object into a generic icon. If it remains a compound machine, replace it with a clearer object that preserves the same causal meaning and remains recognizable without text. Keep at most four visible roles in total. The character's action and causal change must read before object internals. Add nothing new.
```

构图偏向一侧、过满或主体太小：

```text
Use only for this observed visible defect: {具体受损元素及可见后果，不能只写比例偏差}. Keep meaning, objects, exact text, identity, action and rendering unchanged. Make only the uniform scaling or translation needed to resolve the defect while preserving the complete group's aspect ratio, contact and internal relative positions. Use the original composition envelope from `composition-lock.md`; do not introduce a new width/height target or try to fill both dimensions exactly. Preserve the character's existing pose, expression, line quality, colors and material. Show all required elements clearly with calm background on every side. Add nothing.
```

Workflow 横向关系不清或铺得过满：

```text
Use only when the workflow's causal path is visibly broken or required elements are cropped or unreadable. Keep the confirmed workflow meaning, objects, labels, character identity, action, expression, and rendering style unchanged. Restore the broken relation within the shared layout envelope in `composition-lock.md`. Keep 3–5 causally connected nodes, make the central processing object largest, keep input and output smaller, use one dominant path, and let the active character operate only the decisive transformation. Do not rescale a readable intact workflow merely to match a percentage.
```

关键中文错误：

```text
Keep all visuals unchanged. Correct only the required exact Chinese text to the following strings, character for character: {逐项列出正确文字}. Prefer short horizontal placement with enough empty space. Do not paraphrase, add or approximate any character. Optional notes may be removed rather than rendered incorrectly.
```

当同一初稿同时存在构图、文字或其他多个硬缺陷时，不逐项连续编辑。把已确认缺陷合并到一次修正 Prompt：先列出“必须保持”的 2–3 个初稿优势，再逐项列出全部“必须修复”的硬缺陷；只调用一次 image_gen 修正。宽高百分比单独越界和人物轻微 3D 质感是软偏差，禁止加入合并修正 Prompt。
