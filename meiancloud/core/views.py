from django.http import HttpRequest
from django.shortcuts import render

from .context import default_context


FINDMEIAN_TOPICS = [
    {
        "slug": "overview",
        "title": "梅庵概况",
        "subtitle": "从位置、命名到建筑身份，建立对梅庵的整体认识。",
        "hero_image": "core/findmeian/img/1/1.jpg",
        "images": [f"core/findmeian/img/1/{index}.jpg" for index in range(1, 6)],
        "image_captions": [
            "梅庵相关空间外观与展陈入口",
            "梅庵历史环境与校园空间关系",
            "梅庵参观环境示意",
            "梅庵图文资料展示",
            "梅庵相关展示细节",
        ],
        "tags": ["梅庵历史", "命名来源", "建筑空间", "校园文化"],
        "summary": "梅庵位于东南大学四牌楼校区西北角，紧邻六朝松，是校园中兼具历史建筑、文化记忆和红色教育价值的重要空间。",
        "paragraphs": [
            "梅庵位于东南大学四牌楼校区西北角，西临进香河，北近鸡笼山，周边环境与校园历史空间紧密相连。它并不只是一个普通建筑，而是东南大学历史文化记忆中的重要节点。",
            "梅庵之名与李瑞清有关。李瑞清字梅庵，曾任两江师范学堂监督，在教育改革、艺术教育和校园精神塑造方面具有重要影响。梅庵以其字号命名，也使建筑本身带有纪念教育先贤的意义。",
            "从早期茅屋到后来的砖混结构平房，梅庵的形态经历了演变，但其文化功能始终延续。它既承载教育人物纪念，也见证古琴教学、马克思主义传播和早期党团活动。",
        ],
        "facts": [
            "位置：东南大学四牌楼校区西北角，紧邻六朝松。",
            "命名：与李瑞清字“梅庵”有关。",
            "形态：早期为茅草屋，后改建为砖混结构平房。",
            "价值：兼具校园文化、历史建筑和红色教育意义。",
        ],
        "references": ["寒假社会实践调研报告_final.pdf", "./temp/meian.md"],
        "related": [
            {"slug": "history", "reason": "继续了解梅庵从初建到改建的历史脉络"},
            {"slug": "li-ruiqing", "reason": "解释“梅庵”命名背后的人物来源"},
            {"slug": "visit", "reason": "从知识了解延伸到实际参观"},
        ],
    },
    {
        "slug": "history",
        "title": "历史沿革",
        "subtitle": "梳理梅庵从建立、改建到成为文化教育空间的历史线索。",
        "hero_image": "core/findmeian/img/1/2.jpg",
        "images": [f"core/findmeian/img/1/{index}.jpg" for index in range(1, 6)],
        "image_captions": [
            "梅庵历史空间相关图片",
            "梅庵早期建筑与校园关系示意",
            "梅庵参观区域照片",
            "梅庵图文材料展示",
            "梅庵历史细节资料",
        ],
        "tags": ["历史沿革", "1915/1916", "1933", "文物保护"],
        "summary": "梅庵的历史可以从纪念李瑞清、校园文化空间、红色活动场所和文物保护单位几个层面展开。",
        "paragraphs": [
            "关于梅庵的初建时间，现有材料中存在 1915 年和 1916 年两种表述。较稳妥的展示方式，是说明其建立于南京高等师范学校早期阶段，并在资料来源处标注待核对事项。这样既能保留资料信息，也避免在尚未统一口径前给出过度确定的结论。",
            "早期梅庵以茅屋形态存在，周围环以梅树，具有朴素而鲜明的纪念意味。它并非孤立建筑，而是与两江师范学堂、南京高等师范学校和后来的东南大学历史脉络相连。",
            "1933 年，梅庵改建为砖混结构平房，建筑功能也随校园发展不断变化。它曾作为音乐教室使用，也与古琴教学、校园文化活动和革命历史记忆产生联系。",
            "从文化空间角度看，梅庵的历史沿革可以分成三层：第一层是纪念李瑞清的教育人物空间，第二层是校园文化和艺术活动空间，第三层是与早期党团活动和团二大相关的红色历史空间。",
            "后来，梅庵被列为南京市文物保护单位，并逐渐成为爱国主义教育和党史学习教育的重要场所。它的价值不只在建筑本身，也在于其背后的历史事件、人物关系和文化象征。",
        ],
        "timeline": [
            {"year": "1915/1916", "text": "梅庵初建，具体年份需结合权威文献进一步统一。"},
            {"year": "1922", "text": "中国社会主义青年团南京地委在梅庵成立。"},
            {"year": "1923", "text": "中国社会主义青年团第二次全国代表大会在梅庵召开。"},
            {"year": "1933", "text": "梅庵改建为砖混结构平房。"},
            {"year": "1992", "text": "梅庵被列为南京市文物保护单位。"},
        ],
        "facts": [
            "初建年份需统一核对，材料中有 1915/1916 两种表述。",
            "1933 年改建为砖混结构平房。",
            "梅庵见证了东南大学校园空间和教育传统的延续。",
            "1992 年被列为南京市文物保护单位。",
        ],
        "references": [
            "许启彬：《东南大学历史文化源流：百年梅庵的艺术传承与革命记忆》",
            "寒假社会实践调研报告_final.pdf",
            "./temp/meian.md",
        ],
        "related": [
            {"slug": "overview", "reason": "回到梅庵整体概况"},
            {"slug": "li-ruiqing", "reason": "历史沿革与李瑞清纪念关系紧密相关"},
            {"slug": "references", "reason": "查看年份和史料来源说明"},
        ],
    },
    {
        "slug": "li-ruiqing",
        "title": "李瑞清与命名",
        "subtitle": "理解“梅庵”名称背后的教育人物、艺术传统与校园精神。",
        "hero_image": "core/findmeian/img/2/1.jpg",
        "images": [f"core/findmeian/img/2/{index}.jpg" for index in range(1, 7)],
        "image_captions": [
            "李瑞清与梅庵主题展陈资料",
            "师道梅庵展陈图片",
            "李瑞清教育思想相关展示",
            "梅庵命名与人物关系资料",
            "校园精神与校训相关展示",
            "李瑞清艺术与教育贡献展示",
        ],
        "tags": ["李瑞清", "教育改革", "艺术成就", "命名来源"],
        "summary": "李瑞清是梅庵命名的文化源头，也是理解梅庵教育意义的重要人物。",
        "paragraphs": [
            "李瑞清字梅庵，号清道人，是中国近现代教育史和艺术史上的重要人物。理解梅庵，不能只从建筑本身入手，还需要理解李瑞清这一人物与东南大学早期教育传统之间的关系。",
            "在两江师范学堂任职期间，李瑞清积极推动学校改革。他强调教育救国，重视中西贯通、实践创新和人格培养，使学校逐渐形成严谨、朴素、重学术与重实践并行的精神气质。",
            "“嚼得菜根，做得大事”这一校训与李瑞清的教育理念密切相关。它强调艰苦、坚韧和担当，也使梅庵不仅具有纪念人物的意义，还和学校精神传统形成连接。",
            "李瑞清在书法、绘画、文学等方面同样有深厚造诣。相关材料提到，他主张“求篆于金”“求分于石”，重视从金石碑刻中追求书法根基，形成具有个人风格的艺术追求。",
            "因此，梅庵以李瑞清字号命名，并不只是命名上的纪念。它把教育传统、艺术精神和校园历史连接起来，使梅庵成为一个具有多重含义的文化空间。",
        ],
        "facts": [
            "李瑞清字梅庵，梅庵建筑名称与其字号有关。",
            "李瑞清曾任两江师范学堂监督。",
            "他重视教育改革和艺术教育。",
            "校训“嚼得菜根，做得大事”与其教育理念相关。",
        ],
        "references": [
            "邹自振、董瑞兰：《梅庵文学艺术成就及学术贡献》",
            "寒假社会实践调研报告_final.pdf",
            "./temp/meian.md",
        ],
        "related": [
            {"slug": "overview", "reason": "从人物回到梅庵整体认识"},
            {"slug": "history", "reason": "补充梅庵建立与改建背景"},
            {"slug": "exhibition", "reason": "查看展陈中与人物相关的图文资料"},
        ],
    },
    {
        "slug": "tuanerda",
        "title": "团二大专题",
        "subtitle": "聚焦中国社会主义青年团第二次全国代表大会与梅庵的关系。",
        "hero_image": "core/findmeian/img/4/1.jpg",
        "images": [f"core/findmeian/img/4/{index}.jpg" for index in range(1, 8)],
        "image_captions": [
            "团二大专题展陈图片",
            "会议场景相关展示资料",
            "团二大历史背景展示",
            "党团关系相关展陈内容",
            "团二大会议影响展示",
            "青年运动相关展示资料",
            "团二大专题展板细节",
        ],
        "tags": ["团二大", "1923", "青年运动", "党团关系"],
        "summary": "1923 年 8 月 20 日至 25 日，中国社会主义青年团第二次全国代表大会在梅庵召开，这是梅庵最重要的红色历史事件之一。",
        "paragraphs": [
            "1923 年 8 月 20 日至 25 日，中国社会主义青年团第二次全国代表大会在梅庵召开。这一事件使梅庵从校园历史建筑进一步成为中国青年运动史中的重要空间。",
            "团二大的召开有其明确历史背景。五四运动后，马克思主义在中国青年群体中广泛传播，青年组织快速发展，但也面临组织方向、革命任务和与党的关系等问题，需要通过全国性会议进一步明确。",
            "会议围绕青年团的组织建设、宣传教育、青年运动方向等问题展开讨论，并进一步明确团与党的关系。相关资料指出，团二大是唯一一次在高校召开的共青团全国代表大会，这使梅庵在中国青年运动史中具有独特地位。",
            "从梅庵知识展示角度看，团二大专题是整个网站最重要的红色文化内容。它可以把时间、地点、人物、会议议题、历史影响和青年运动延展内容组织起来，形成一条清晰的学习路径。",
            "如果后续继续深化，可以把本专题拆成更细的内容单元，例如“会议背景”“会议过程”“党团关系”“会议影响”“青年运动延展”。这样既能增强页面内容，也方便后续做检索和相关推荐。",
        ],
        "facts": [
            "召开时间：1923 年 8 月 20 日至 25 日。",
            "召开地点：东南大学梅庵。",
            "历史地位：唯一一次在高校召开的共青团全国代表大会。",
            "核心意义：明确青年团发展方向和党团关系。",
        ],
        "references": [
            "许启彬：《东南大学历史文化源流：百年梅庵的艺术传承与革命记忆》",
            "《东南大学：让红色火种代代相传》",
            "寒假社会实践调研报告_final.pdf",
        ],
        "related": [
            {"slug": "red-culture", "reason": "团二大与青年运动和红色文化直接相关"},
            {"slug": "exhibition", "reason": "查看与会议场景相关的展陈图片"},
            {"slug": "references", "reason": "了解团二大内容的资料来源"},
        ],
    },
    {
        "slug": "red-culture",
        "title": "红色文化与青年运动",
        "subtitle": "从梅庵看马克思主义传播、早期党团活动与青年思想启蒙。",
        "hero_image": "core/findmeian/img/3/1.jpg",
        "images": [f"core/findmeian/img/3/{index}.jpg" for index in range(1, 9)] + [
            f"core/findmeian/img/6/{index}.jpg" for index in range(1, 6)
        ],
        "image_captions": [
            "真理耀东南展陈图片",
            "马克思主义传播相关展示",
            "早期党团活动展示资料",
            "青年组织活动相关图片",
            "红色文化主题展陈细节",
            "青年运动资料展示",
            "南京早期党团活动资料",
            "梅庵红色文化展陈图片",
            "《中国青年》相关展示资料",
            "青年宣传工作延展资料",
            "青年运动相关图片",
            "革命传播主题展陈",
            "青年思想传播资料",
        ],
        "tags": ["红色文化", "马克思主义", "党团组织", "中国青年"],
        "summary": "梅庵是南京早期党团组织活动的重要场所，也是理解东南大学红色文化的重要入口。",
        "paragraphs": [
            "五四运动后，马克思主义在中国广泛传播，南京高等师范学校逐步成为江苏地区马克思主义传播中心和党团组织活动基地。梅庵在这一过程中成为重要的空间节点。",
            "1922 年 5 月，中国社会主义青年团南京地委在梅庵成立。梅庵因此不仅与校园文化有关，也与中国青年运动和早期革命组织活动密切相连。",
            "团二大之后，青年宣传工作继续推进。《中国青年》周刊的创办，体现了青年思想传播、政治教育和革命动员之间的关系。",
            "红色文化与青年运动专题可以帮助用户理解：梅庵的价值不是单一建筑价值，而是历史事件、青年群体、思想传播和教育功能共同构成的综合价值。",
        ],
        "facts": [
            "梅庵是南京早期党团组织活动的重要场所。",
            "1922 年中国社会主义青年团南京地委在此成立。",
            "梅庵与马克思主义传播和青年运动关系密切。",
            "《中国青年》可作为团二大之后的思想传播延展内容。",
        ],
        "references": [
            "寒假社会实践调研报告_final.pdf",
            "./temp/meian.md",
            "《东南大学：让红色火种代代相传》",
        ],
        "related": [
            {"slug": "tuanerda", "reason": "团二大是红色文化主线的核心事件"},
            {"slug": "history", "reason": "从革命活动回看梅庵历史空间演变"},
            {"slug": "references", "reason": "查看红色文化内容的来源依据"},
        ],
    },
    {
        "slug": "exhibition",
        "title": "展厅导览",
        "subtitle": "以展厅和图片为线索，让线上浏览更接近线下参观路径。",
        "hero_image": "core/findmeian/img/5/1.jpg",
        "images": [
            *[f"core/findmeian/img/1/{index}.jpg" for index in range(1, 6)],
            *[f"core/findmeian/img/2/{index}.jpg" for index in range(1, 7)],
            *[f"core/findmeian/img/5/{index}.jpg" for index in range(1, 5)],
        ],
        "image_captions": [
            "梅庵展陈入口与空间资料",
            "展厅环境相关图片",
            "梅庵参观空间图片",
            "图文展陈资料",
            "展厅细节资料",
            "师道梅庵展陈图片",
            "李瑞清主题展陈",
            "教育传统相关展示",
            "命名来源相关资料",
            "校训与校园精神展示",
            "人物专题展陈图片",
            "会议记录相关展示",
            "团二大会议资料图片",
            "青年运动相关展陈",
            "会议内容展示细节",
        ],
        "tags": ["展厅", "导览", "图文资料", "参观路径"],
        "summary": "展厅导览页负责把分散图片和说明文字组织起来，帮助用户形成接近线下参观的浏览体验。",
        "paragraphs": [
            "现有资料显示，梅庵内部展陈内容可以按展厅或空间进行组织。相比在一个长页面里集中展示，展厅导览页更适合承载图片、展板内容和参观路径。",
            "展厅导览的重点不是简单堆放图片，而是说明每一组图片对应什么主题、与哪些历史人物或事件相关，以及用户在线下参观时可以如何理解这些内容。",
            "当前页面先按照“梅庵概况、师道梅庵、真理耀东南、会议场景、会议记录、青年运动”等主题组织图片。后续如果能获得正式展厅名称，可以进一步替换为更权威的展厅目录。",
            "从用户体验角度看，展厅导览页承担线上预参观功能。用户在到访前可先了解主要内容，到访后也可通过该页回顾展陈信息。",
        ],
        "sections": [
            {"title": "梅庵概况", "text": "帮助用户建立位置、建筑和整体价值认知。"},
            {"title": "师道梅庵", "text": "围绕李瑞清、教育改革和梅庵命名展开。"},
            {"title": "真理耀东南", "text": "突出马克思主义传播和早期党团活动。"},
            {"title": "会议场景", "text": "聚焦团二大在梅庵召开的历史场景。"},
            {"title": "青年运动", "text": "展示团二大之后青年思想传播的延展内容。"},
        ],
        "facts": [
            "展厅内容适合按主题、空间和参观顺序组织。",
            "图片需要配合说明文字，避免只做相册。",
            "后续应补充展厅正式名称和展陈主题。",
            "该页可作为线上导览和线下参观之间的连接点。",
        ],
        "references": ["寒假社会实践调研报告_final.pdf", "团队线下调研图片资料"],
        "related": [
            {"slug": "overview", "reason": "从展厅回到梅庵整体介绍"},
            {"slug": "tuanerda", "reason": "展陈内容与团二大专题联系紧密"},
            {"slug": "visit", "reason": "结合线上展陈了解线下参观方式"},
        ],
    },
    {
        "slug": "visit",
        "title": "参观与预约",
        "subtitle": "集中回答用户最关心的开放、预约、讲解和参观体验问题。",
        "hero_image": "core/findmeian/img/1/3.jpg",
        "images": ["core/findmeian/img/1/3.jpg", "core/findmeian/img/1/4.jpg", "core/findmeian/img/1/5.jpg"],
        "image_captions": [
            "梅庵参观环境示意",
            "梅庵图文资料展示区域",
            "梅庵参观空间细节",
        ],
        "tags": ["参观", "预约", "讲解", "FAQ"],
        "summary": "调研反馈显示，用户非常关心梅庵是否开放、如何预约以及能体验哪些内容，因此需要独立页面承载参观服务信息。",
        "paragraphs": [
            "从问卷反馈看，用户对梅庵是否向公众开放、如何预约、参观时可以体验哪些内容非常感兴趣。这类信息虽然不完全属于历史知识，但直接影响用户能否走进梅庵。",
            "参观与预约页面应集中说明进入东南大学四牌楼校区、预约参观、讲解服务和注意事项。对于校外访客，这类内容尤其重要。",
            "当前可先提供基础说明，并提示用户关注相关官方渠道获取最新预约安排。后续如果获取到更准确的开放时间和讲解安排，可继续补充。",
            "根据现有 FAQ 信息，用户可关注相关微信公众号获取参观预约方式。实际开放时间、入校要求和讲解安排可能会变化，因此页面应强调以官方通知为准。",
        ],
        "visit_steps": [
            "确认东南大学四牌楼校区入校和梅庵开放要求。",
            "通过官方或讲解团渠道了解预约方式。",
            "按预约要求填写个人信息并等待审核或确认。",
            "到校后按照校园路线前往梅庵，参观时遵守场馆规定。",
        ],
        "facts": [
            "用户高度关注梅庵是否开放和如何预约。",
            "可结合 FAQ 页面提供更清晰的参观说明。",
            "讲解服务信息建议以官方渠道为准。",
            "参观提示应强调爱护文物和遵守场馆规定。",
        ],
        "references": ["寒假社会实践调研报告_final.pdf", "网站常见问题页面现有内容"],
        "related": [
            {"slug": "overview", "reason": "参观前先建立整体认知"},
            {"slug": "exhibition", "reason": "预约参观前了解展厅内容"},
            {"slug": "references", "reason": "查看信息来源与更新说明"},
        ],
    },
    {
        "slug": "references",
        "title": "资料与参考",
        "subtitle": "说明梅庵知识整理所依据的资料来源，增强内容可信度。",
        "hero_image": "core/findmeian/img/6/1.jpg",
        "images": ["core/findmeian/img/6/1.jpg", "core/findmeian/img/6/2.jpg"],
        "image_captions": ["青年运动相关资料图", "资料整理与展示示意图"],
        "tags": ["资料来源", "参考文献", "知识整理", "可信度"],
        "summary": "梅庵知识页面需要标明资料来源，避免只做无来源的展示文本。",
        "paragraphs": [
            "梅庵相关知识涉及历史人物、会议事件、建筑沿革和展陈内容。为了保证网站内容可信，应尽量标明资料来源，并区分文献资料、馆内展陈、访谈记录和团队整理内容。",
            "当前可参考的材料包括项目 PDF 调研报告、`temp/meian.md` 整理稿，以及报告中提到的相关文献。后续正式发布时，建议对建造年份、改建时间、题写者等细节继续核对。",
            "资料与参考页的作用，是让用户知道网站内容不是随意拼接，而是经过收集、筛选和整理的知识系统。",
        ],
        "facts": [
            "内容整理参考了 temp 目录下的调研报告和 meian.md。",
            "建造年份存在 1915/1916 两种表述，需要统一核对。",
            "权威来源标注可以提升网站可信度。",
            "该页可作为后续知识库建设的来源说明。",
        ],
        "references": [
            "许启彬：《东南大学历史文化源流：百年梅庵的艺术传承与革命记忆》，《东南文化》，2023(05):124-133。",
            "仲点石、徐春宏、黄涌：《寻迹梅庵》，《档案与建设》，2023(09):78-80。",
            "邹自振、董瑞兰：《梅庵文学艺术成就及学术贡献——纪念李瑞清逝世100周年》，《东南文化》，2023(05):115-123。",
            "《东南大学：让红色火种代代相传》，《群众》，2023(17):54-55。",
            "寒假社会实践调研报告_final.pdf。",
        ],
        "related": [
            {"slug": "history", "reason": "历史沿革中存在需核对的年份信息"},
            {"slug": "tuanerda", "reason": "团二大专题需要权威史料支撑"},
            {"slug": "li-ruiqing", "reason": "人物专题需要结合文献与展陈来源"},
        ],
    },
]


def _topic_map():
    return {topic["slug"]: topic for topic in FINDMEIAN_TOPICS}


def _related_topics(topic):
    topics = _topic_map()
    related = []
    for item in topic.get("related", []):
        slug = item["slug"] if isinstance(item, dict) else item
        if slug in topics:
            related.append(
                {
                    "topic": topics[slug],
                    "reason": item.get("reason", "与当前专题内容相关")
                    if isinstance(item, dict)
                    else "与当前专题内容相关",
                }
            )
    return related


def index(request: HttpRequest):
    # 首页仅渲染静态内容，公共信息通过 default_context 注入。
    return render(request, "core/index.html", default_context(request))


def findmeian(request: HttpRequest):
    context = default_context(request)
    context["topics"] = FINDMEIAN_TOPICS
    context["featured_topic"] = _topic_map()["tuanerda"]
    return render(request, "core/findmeian.html", context)


def findmeian_topic(request: HttpRequest, slug: str):
    topics = _topic_map()
    topic = topics.get(slug)
    if topic is None:
        from django.http import Http404

        raise Http404("Meian topic not found")
    context = default_context(request)
    context["topic"] = topic
    captions = topic.get("image_captions", [])
    context["image_items"] = [
        {
            "path": image,
            "caption": captions[index] if index < len(captions) else "梅庵专题图文资料",
        }
        for index, image in enumerate(topic.get("images", []))
    ]
    context["related_topics"] = _related_topics(topic)
    return render(request, "core/findmeian_topic.html", context)


def about(request: HttpRequest):
    return render(request, "core/about.html", default_context(request))


def question_view(request: HttpRequest):
    return render(request, "core/question.html", default_context(request))


def user_agreement(request: HttpRequest):
    return render(request, "core/user-agreement.html", default_context(request))


def login_prompt_view(request: HttpRequest):
    return render(request, "core/login_prompt.html", context=default_context(request))
