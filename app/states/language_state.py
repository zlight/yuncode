import reflex as rx


class LanguageState(rx.State):
    language: str = "en"  # "en" or "zh"

    @rx.event
    def toggle_language(self):
        self.language = "zh" if self.language == "en" else "en"

    @rx.event
    def set_language(self, lang: str):
        self.language = lang

    @rx.var
    def is_zh(self) -> bool:
        return self.language == "zh"

    def _t(self, en: str, zh: str) -> str:
        return zh if self.language == "zh" else en

    # Navigation Translations
    @rx.var
    def nav_home(self) -> str:
        return "首页" if self.language == "zh" else "Home"

    @rx.var
    def nav_products(self) -> str:
        return "云产品" if self.language == "zh" else "Products"

    @rx.var
    def nav_light_server(self) -> str:
        return "轻量服务器" if self.language == "zh" else "Light Server"

    @rx.var
    def nav_network(self) -> str:
        return "网络节点" if self.language == "zh" else "Network"

    @rx.var
    def nav_pricing(self) -> str:
        return "价格方案" if self.language == "zh" else "Pricing"

    @rx.var
    def nav_trust(self) -> str:
        return "服务保证" if self.language == "zh" else "Trust"

    @rx.var
    def nav_faq(self) -> str:
        return "常见问题" if self.language == "zh" else "FAQ"

    @rx.var
    def nav_login(self) -> str:
        return "登录" if self.language == "zh" else "Log In"

    @rx.var
    def nav_signup(self) -> str:
        return "立即注册" if self.language == "zh" else "Sign up"

    # Hero Section Translations
    @rx.var
    def hero_badge(self) -> str:
        return "全新轻量级云服务器" if self.language == "zh" else "Light Server"

    @rx.var
    def hero_title_highlight(self) -> str:
        return "AkileCloud" if self.language == "zh" else "AkileCloud "

    @rx.var
    def hero_title_suffix(self) -> str:
        return (
            " 全球大带宽流媒体解锁高防 VPS"
            if self.language == "zh"
            else "Large Bandwidth Streaming Unlocked VPS"
        )

    @rx.var
    def hero_desc(self) -> str:
        return (
            "专业全球大带宽云服务商，专注于提供超低延迟、精品 BGP 路由及原生 IP 级别流媒体解锁方案。"
            if self.language == "zh"
            else "A cloud service provider specializing in Global high-bandwidth solutions."
        )

    @rx.var
    def hero_feature1(self) -> str:
        return (
            "全球大带宽优质节点"
            if self.language == "zh"
            else "Global High-Bandwidth Nodes"
        )

    @rx.var
    def hero_feature2(self) -> str:
        return (
            "原生 IP 流媒体全面解锁"
            if self.language == "zh"
            else "Native IP Streaming Unlock"
        )

    @rx.var
    def hero_feature3(self) -> str:
        return (
            "BGP 优化精品回国网络"
            if self.language == "zh"
            else "BGP-Optimized Routes"
        )

    @rx.var
    def hero_btn_overview(self) -> str:
        return "产品概览" if self.language == "zh" else "Overview"

    @rx.var
    def hero_btn_telegram(self) -> str:
        return "加入电报群" if self.language == "zh" else "Telegram Group"

    @rx.var
    def hero_streaming(self) -> str:
        return "流媒体全解锁" if self.language == "zh" else "Streaming unlocked"

    @rx.var
    def hero_pops(self) -> str:
        return (
            "全球 100+ 边缘节点"
            if self.language == "zh"
            else "100+ PoPs worldwide"
        )

    @rx.var
    def lang_toggle_label(self) -> str:
        return "EN" if self.language == "zh" else "中文"

    # ==================== Products Section ====================
    @rx.var
    def products_badge(self) -> str:
        return self._t("Products", "云产品")

    @rx.var
    def products_title_prefix(self) -> str:
        return self._t("Cloud services for ", "为每种场景打造的 ")

    @rx.var
    def products_title_highlight(self) -> str:
        return self._t("every scenario", "云端服务")

    @rx.var
    def products_desc(self) -> str:
        return self._t(
            "From streaming-unlocked light servers to enterprise-grade dedicated hardware — one platform, one console, one bill.",
            "从流媒体解锁的轻量服务器到企业级独立硬件——一个平台、一个控制台、一份账单。",
        )

    @rx.var
    def products_cta_details(self) -> str:
        return self._t("View details", "查看详情")

    @rx.var
    def products_cta_explore(self) -> str:
        return self._t("Explore", "查看详情")

    @rx.var
    def products_list(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {
                    "icon": "zap",
                    "tag": "热门",
                    "tag_color": "blue",
                    "title": "轻量云服务器",
                    "desc": "入门级流媒体解锁 VPS,适合个人使用、隧道与轻量应用。",
                    "spec1": "1-4 vCPU · 1-8 GB 内存",
                    "spec2": "500 Mbps – 1 Gbps",
                    "spec3": "原生 IP · 流媒体解锁",
                    "cta": "查看详情",
                },
                {
                    "icon": "server",
                    "tag": "推荐",
                    "tag_color": "emerald",
                    "title": "商业云服务器",
                    "desc": "均衡性能,BGP 优化路由,适合生产工作负载。",
                    "spec1": "4-16 vCPU · 8-32 GB 内存",
                    "spec2": "2 Gbps – 5 Gbps",
                    "spec3": "SSD NVMe · 20 Gbps 高防",
                    "cta": "查看详情",
                },
                {
                    "icon": "cpu",
                    "tag": "高性能",
                    "tag_color": "purple",
                    "title": "企业级计算",
                    "desc": "AMD EPYC 独享核心,面向低延迟服务与集群。",
                    "spec1": "8-64 vCPU · 32-256 GB 内存",
                    "spec2": "5 Gbps – 10 Gbps",
                    "spec3": "独享 CPU · 私有网络",
                    "cta": "查看详情",
                },
                {
                    "icon": "hard-drive",
                    "tag": "裸金属",
                    "tag_color": "amber",
                    "title": "独立服务器",
                    "desc": "完全托管的物理服务器,支持自定义硬件配置。",
                    "spec1": "至强 / EPYC · 最高 1 TB 内存",
                    "spec2": "10 Gbps 不限量选项",
                    "spec3": "IPMI · 自定义系统 · RAID",
                    "cta": "查看详情",
                },
                {
                    "icon": "radio-tower",
                    "tag": "流媒体",
                    "tag_color": "rose",
                    "title": "流媒体解锁 VPS",
                    "desc": "原生 IP 解锁 Netflix、Disney+、HBO、TikTok 等平台。",
                    "spec1": "2-8 vCPU · 4-16 GB 内存",
                    "spec2": "1 Gbps – 3 Gbps",
                    "spec3": "原生 IP · 全区域解锁",
                    "cta": "查看详情",
                },
                {
                    "icon": "shield-check",
                    "tag": "高安全",
                    "tag_color": "cyan",
                    "title": "云高防服务",
                    "desc": "企业级 DDoS 防护高达 200 Gbps,支持 L7 缓解。",
                    "spec1": "4-16 vCPU · 8-32 GB 内存",
                    "spec2": "防护 100-200 Gbps",
                    "spec3": "L3/L4/L7 缓解 · WAF",
                    "cta": "查看详情",
                },
            ]
        return [
            {
                "icon": "zap",
                "tag": "Popular",
                "tag_color": "blue",
                "title": "Light Cloud Server",
                "desc": "Entry-grade streaming-unlocked VPS for personal use, tunnels and light apps.",
                "spec1": "1-4 vCPU · 1-8 GB RAM",
                "spec2": "500 Mbps – 1 Gbps",
                "spec3": "Native IP · Streaming Unlock",
                "cta": "Explore",
            },
            {
                "icon": "server",
                "tag": "Recommended",
                "tag_color": "emerald",
                "title": "Business Cloud Server",
                "desc": "Balanced performance, BGP-optimized routes for production workloads.",
                "spec1": "4-16 vCPU · 8-32 GB RAM",
                "spec2": "2 Gbps – 5 Gbps",
                "spec3": "SSD NVMe · DDoS 20 Gbps",
                "cta": "Explore",
            },
            {
                "icon": "cpu",
                "tag": "High Performance",
                "tag_color": "purple",
                "title": "Enterprise Compute",
                "desc": "AMD EPYC dedicated cores for latency-sensitive services and clusters.",
                "spec1": "8-64 vCPU · 32-256 GB RAM",
                "spec2": "5 Gbps – 10 Gbps",
                "spec3": "Dedicated CPU · Private Net",
                "cta": "Explore",
            },
            {
                "icon": "hard-drive",
                "tag": "Bare Metal",
                "tag_color": "amber",
                "title": "Dedicated Servers",
                "desc": "Fully-managed physical machines with custom hardware configurations.",
                "spec1": "Xeon / EPYC · up to 1 TB RAM",
                "spec2": "10 Gbps unmetered options",
                "spec3": "IPMI · Custom OS · RAID",
                "cta": "Explore",
            },
            {
                "icon": "radio-tower",
                "tag": "Streaming",
                "tag_color": "rose",
                "title": "Streaming Unlock VPS",
                "desc": "Native IPs unlocking Netflix, Disney+, HBO, TikTok and more.",
                "spec1": "2-8 vCPU · 4-16 GB RAM",
                "spec2": "1 Gbps – 3 Gbps",
                "spec3": "Native IP · Full Region Unlock",
                "cta": "Explore",
            },
            {
                "icon": "shield-check",
                "tag": "Secure",
                "tag_color": "cyan",
                "title": "Anti-DDoS Cloud",
                "desc": "Enterprise DDoS protection up to 200 Gbps with L7 mitigation.",
                "spec1": "4-16 vCPU · 8-32 GB RAM",
                "spec2": "Protected 100-200 Gbps",
                "spec3": "L3/L4/L7 Mitigation · WAF",
                "cta": "Explore",
            },
        ]

    # ==================== Nodes Section ====================
    @rx.var
    def nodes_badge(self) -> str:
        return self._t("Global Network", "全球网络")

    @rx.var
    def nodes_title_prefix(self) -> str:
        return self._t("Global backbone with ", "全球骨干网 · ")

    @rx.var
    def nodes_title_highlight(self) -> str:
        return self._t("BGP-optimized routes", "BGP 优化路由")

    @rx.var
    def nodes_desc(self) -> str:
        return self._t(
            "Distributed nodes across Asia, Europe and North America — direct peering, premium transit, low latency.",
            "覆盖亚洲、欧洲和北美的分布式节点——直连对等、优质中转、超低延迟。",
        )

    @rx.var
    def nodes_stat_pops(self) -> str:
        return self._t("Global PoPs", "全球边缘节点")

    @rx.var
    def nodes_stat_peak(self) -> str:
        return self._t("Peak per Node", "单节点峰值")

    @rx.var
    def nodes_stat_latency(self) -> str:
        return self._t("Intra-Asia Latency", "亚洲内延迟")

    @rx.var
    def nodes_stat_ddos(self) -> str:
        return self._t("DDoS Mitigation", "DDoS 防护")

    @rx.var
    def nodes_live_status(self) -> str:
        return self._t("Live network status", "实时网络状态")

    @rx.var
    def nodes_updated(self) -> str:
        return self._t("Updated 5s ago", "5 秒前更新")

    @rx.var
    def nodes_col_region(self) -> str:
        return self._t("Region", "区域")

    @rx.var
    def nodes_col_bandwidth(self) -> str:
        return self._t("Bandwidth", "带宽")

    @rx.var
    def nodes_col_latency(self) -> str:
        return self._t("Latency", "延迟")

    @rx.var
    def nodes_col_line(self) -> str:
        return self._t("Line", "线路")

    @rx.var
    def nodes_col_load(self) -> str:
        return self._t("Load", "负载")

    @rx.var
    def nodes_col_status(self) -> str:
        return self._t("Status", "状态")

    @rx.var
    def nodes_status_online(self) -> str:
        return self._t("Online", "在线")

    @rx.var
    def nodes_list(self) -> list[dict[str, str]]:
        regions_zh = {
            "Los Angeles": "洛杉矶",
            "Tokyo": "东京",
            "Hong Kong": "香港",
            "Singapore": "新加坡",
            "Frankfurt": "法兰克福",
            "London": "伦敦",
            "Seoul": "首尔",
            "Taipei": "台北",
        }
        base = [
            {
                "flag": "🇺🇸",
                "region": "Los Angeles",
                "code": "USBGP",
                "bandwidth": "10 Gbps",
                "latency": "142 ms",
                "line": "CN2 GIA · 4837",
                "load": "62",
            },
            {
                "flag": "🇯🇵",
                "region": "Tokyo",
                "code": "JPBGP",
                "bandwidth": "10 Gbps",
                "latency": "48 ms",
                "line": "IIJ · SoftBank BGP",
                "load": "71",
            },
            {
                "flag": "🇭🇰",
                "region": "Hong Kong",
                "code": "HKBGP",
                "bandwidth": "5 Gbps",
                "latency": "28 ms",
                "line": "HKIX · CN2 GIA",
                "load": "55",
            },
            {
                "flag": "🇸🇬",
                "region": "Singapore",
                "code": "SGBGP",
                "bandwidth": "5 Gbps",
                "latency": "62 ms",
                "line": "NTT · Telstra",
                "load": "44",
            },
            {
                "flag": "🇩🇪",
                "region": "Frankfurt",
                "code": "DEBGP",
                "bandwidth": "10 Gbps",
                "latency": "182 ms",
                "line": "DE-CIX · Cogent",
                "load": "38",
            },
            {
                "flag": "🇬🇧",
                "region": "London",
                "code": "UKBGP",
                "bandwidth": "5 Gbps",
                "latency": "195 ms",
                "line": "LINX · Level3",
                "load": "41",
            },
            {
                "flag": "🇰🇷",
                "region": "Seoul",
                "code": "KRBGP",
                "bandwidth": "3 Gbps",
                "latency": "52 ms",
                "line": "KT · LG U+",
                "load": "48",
            },
            {
                "flag": "🇹🇼",
                "region": "Taipei",
                "code": "TWBGP",
                "bandwidth": "3 Gbps",
                "latency": "55 ms",
                "line": "HINET · TWGATE",
                "load": "50",
            },
        ]
        if self.language == "zh":
            for n in base:
                n["region"] = regions_zh.get(n["region"], n["region"])
        return base

    # ==================== Pricing Section ====================
    @rx.var
    def pricing_badge(self) -> str:
        return self._t("Pricing", "价格方案")

    @rx.var
    def pricing_title_prefix(self) -> str:
        return self._t("Simple pricing, ", "简明定价, ")

    @rx.var
    def pricing_title_highlight(self) -> str:
        return self._t("scale as you grow", "随业务成长")

    @rx.var
    def pricing_desc(self) -> str:
        return self._t(
            "All plans include native IP, streaming unlock, DDoS protection and 24/7 monitoring.",
            "所有方案均包含原生 IP、流媒体解锁、DDoS 防护与 7×24 小时监控。",
        )

    @rx.var
    def pricing_cycle_monthly(self) -> str:
        return self._t("Monthly", "按月")

    @rx.var
    def pricing_cycle_quarterly(self) -> str:
        return self._t("Quarterly", "按季")

    @rx.var
    def pricing_cycle_yearly(self) -> str:
        return self._t("Yearly", "按年")

    @rx.var
    def pricing_compare(self) -> str:
        return self._t("Compare plans", "方案对比")

    @rx.var
    def pricing_exit_compare(self) -> str:
        return self._t("Exit compare", "退出对比")

    @rx.var
    def pricing_buy_now(self) -> str:
        return self._t("Buy Now", "立即购买")

    @rx.var
    def pricing_get_started(self) -> str:
        return self._t("Get Started", "开始使用")

    @rx.var
    def pricing_add_compare(self) -> str:
        return self._t("Add to compare", "加入对比")

    @rx.var
    def pricing_selected_compare(self) -> str:
        return self._t("Selected for compare", "已加入对比")

    @rx.var
    def pricing_compare_now(self) -> str:
        return self._t("Compare now", "立即对比")

    @rx.var
    def pricing_plans_selected(self) -> str:
        return self._t("plan(s) selected", "个方案已选择")

    @rx.var
    def pricing_footer_note(self) -> str:
        return self._t(
            "All prices in USD. Custom enterprise plans available on request.",
            "所有价格以美元计价。企业定制方案可另行咨询。",
        )

    @rx.var
    def pricing_contact_sales(self) -> str:
        return self._t("Contact sales", "联系销售")

    @rx.var
    def pricing_plans(self) -> list[dict[str, str | float | bool]]:
        if self.language == "zh":
            return [
                {
                    "id": "starter",
                    "name": "入门版",
                    "tag": "",
                    "desc": "适合个人项目与轻量隧道。",
                    "price": 5.99,
                    "vcpu": "1 vCPU",
                    "ram": "1 GB 内存",
                    "disk": "20 GB NVMe",
                    "bandwidth": "500 Mbps",
                    "traffic": "500 GB / 月",
                    "features": "原生 IP · IPv6 · 快照 · 流媒体解锁",
                    "highlight": False,
                },
                {
                    "id": "standard",
                    "name": "标准版",
                    "tag": "最受欢迎",
                    "desc": "均衡型 VPS,适合网站与小型应用。",
                    "price": 12.99,
                    "vcpu": "2 vCPU",
                    "ram": "4 GB 内存",
                    "disk": "60 GB NVMe",
                    "bandwidth": "1 Gbps",
                    "traffic": "2 TB / 月",
                    "features": "原生 IP · 流媒体解锁 · 每日备份 · 20 Gbps 高防",
                    "highlight": True,
                },
                {
                    "id": "pro",
                    "name": "专业版",
                    "tag": "推荐",
                    "desc": "生产级计算,搭配优质路由。",
                    "price": 29.99,
                    "vcpu": "4 vCPU",
                    "ram": "8 GB 内存",
                    "disk": "120 GB NVMe",
                    "bandwidth": "2 Gbps",
                    "traffic": "5 TB / 月",
                    "features": "CN2 GIA · 原生 IP · 优先支持 · 50 Gbps 高防",
                    "highlight": False,
                },
                {
                    "id": "business",
                    "name": "企业版",
                    "tag": "高性能",
                    "desc": "独享核心,面向企业级工作负载。",
                    "price": 69.99,
                    "vcpu": "8 vCPU",
                    "ram": "16 GB 内存",
                    "disk": "240 GB NVMe",
                    "bandwidth": "5 Gbps",
                    "traffic": "10 TB / 月",
                    "features": "独享 CPU · 私有网络 · 7×24 支持 · 100 Gbps 高防",
                    "highlight": False,
                },
            ]
        return [
            {
                "id": "starter",
                "name": "Starter",
                "tag": "",
                "desc": "For side projects and personal tunnels.",
                "price": 5.99,
                "vcpu": "1 vCPU",
                "ram": "1 GB RAM",
                "disk": "20 GB NVMe",
                "bandwidth": "500 Mbps",
                "traffic": "500 GB / mo",
                "features": "Native IP · IPv6 · Snapshot · Streaming Unlock",
                "highlight": False,
            },
            {
                "id": "standard",
                "name": "Standard",
                "tag": "Most Popular",
                "desc": "Balanced VPS for websites and small apps.",
                "price": 12.99,
                "vcpu": "2 vCPU",
                "ram": "4 GB RAM",
                "disk": "60 GB NVMe",
                "bandwidth": "1 Gbps",
                "traffic": "2 TB / mo",
                "features": "Native IP · Streaming Unlock · Daily Backup · DDoS 20 Gbps",
                "highlight": True,
            },
            {
                "id": "pro",
                "name": "Professional",
                "tag": "Recommended",
                "desc": "Production-grade compute with premium routes.",
                "price": 29.99,
                "vcpu": "4 vCPU",
                "ram": "8 GB RAM",
                "disk": "120 GB NVMe",
                "bandwidth": "2 Gbps",
                "traffic": "5 TB / mo",
                "features": "CN2 GIA · Native IP · Priority Support · DDoS 50 Gbps",
                "highlight": False,
            },
            {
                "id": "business",
                "name": "Business",
                "tag": "High Perf",
                "desc": "Dedicated cores for enterprise workloads.",
                "price": 69.99,
                "vcpu": "8 vCPU",
                "ram": "16 GB RAM",
                "disk": "240 GB NVMe",
                "bandwidth": "5 Gbps",
                "traffic": "10 TB / mo",
                "features": "Dedicated CPU · Private Net · 24/7 Support · DDoS 100 Gbps",
                "highlight": False,
            },
        ]

    # ==================== Metrics / Trust Section ====================
    @rx.var
    def metrics_badge(self) -> str:
        return self._t("Trusted at Scale", "值得信赖")

    @rx.var
    def metrics_title_prefix(self) -> str:
        return self._t("Numbers that ", "用数据 ")

    @rx.var
    def metrics_title_highlight(self) -> str:
        return self._t("speak for themselves", "说话")

    @rx.var
    def metrics_desc(self) -> str:
        return self._t(
            "Proven performance and reliability, backed by real customers and real infrastructure.",
            "由真实客户与基础设施验证的性能与可靠性。",
        )

    @rx.var
    def guarantees_badge(self) -> str:
        return self._t("Service Guarantees", "服务保证")

    @rx.var
    def guarantees_title_prefix(self) -> str:
        return self._t("Enterprise-grade ", "企业级 ")

    @rx.var
    def guarantees_title_highlight(self) -> str:
        return self._t("guarantees", "服务保证")

    @rx.var
    def guarantees_desc(self) -> str:
        return self._t(
            "Every plan includes the operational guarantees typically reserved for premium enterprise contracts.",
            "所有方案均包含通常仅企业合约才享有的运营保障。",
        )

    @rx.var
    def metrics_list(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {
                    "icon": "trending-up",
                    "value": "99.99%",
                    "label": "SLA 可用性",
                    "desc": "月度可用性保证,财务背书 SLA。",
                },
                {
                    "icon": "users",
                    "value": "50,000+",
                    "label": "活跃客户",
                    "desc": "受到全球开发者、主播与企业信赖。",
                },
                {
                    "icon": "server",
                    "value": "20,000+",
                    "label": "已部署服务器",
                    "desc": "承载全球骨干网上的生产工作负载。",
                },
                {
                    "icon": "clock",
                    "value": "< 60s",
                    "label": "开通时间",
                    "desc": "从下单到系统就绪的即时部署。",
                },
                {
                    "icon": "headphones",
                    "value": "24/7",
                    "label": "专家支持",
                    "desc": "各方案均配备双语工程师随时待命。",
                },
                {
                    "icon": "shield",
                    "value": "200 Gbps",
                    "label": "DDoS 防护",
                    "desc": "企业级 L3/L4/L7 过滤保护。",
                },
            ]
        return [
            {
                "icon": "trending-up",
                "value": "99.99%",
                "label": "SLA Uptime",
                "desc": "Guaranteed monthly availability with financial-backed SLA.",
            },
            {
                "icon": "users",
                "value": "50,000+",
                "label": "Active Customers",
                "desc": "Trusted by developers, streamers and enterprises worldwide.",
            },
            {
                "icon": "server",
                "value": "20,000+",
                "label": "Deployed Servers",
                "desc": "Running production workloads across our global backbone.",
            },
            {
                "icon": "clock",
                "value": "< 60s",
                "label": "Provisioning Time",
                "desc": "Instant deployment from checkout to fully-booted OS.",
            },
            {
                "icon": "headphones",
                "value": "24/7",
                "label": "Expert Support",
                "desc": "Bilingual engineers on-call for every plan tier.",
            },
            {
                "icon": "shield",
                "value": "200 Gbps",
                "label": "DDoS Mitigation",
                "desc": "Enterprise-grade protection with L3/L4/L7 filtering.",
            },
        ]

    @rx.var
    def guarantees_list(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {
                    "icon": "shield-check",
                    "title": "SLA 可用性保证",
                    "desc": "99.99% 可用性承诺,超出承诺的宕机自动补偿账户信用额度。",
                    "tag": "可靠性",
                },
                {
                    "icon": "refresh-ccw",
                    "title": "7 天无理由退款",
                    "desc": "任意方案 7 天内可全额退款,无隐藏费用,无需理由。",
                    "tag": "保障",
                },
                {
                    "icon": "lock",
                    "title": "数据主权",
                    "desc": "数据留在您选择的地区,静态 AES-256 加密,传输 TLS 1.3。",
                    "tag": "隐私",
                },
                {
                    "icon": "life-buoy",
                    "title": "7×24 专家支持",
                    "desc": "工单、聊天与电报直接联系高级工程师,平均首次响应 < 5 分钟。",
                    "tag": "支持",
                },
                {
                    "icon": "activity",
                    "title": "实时监控",
                    "desc": "实时仪表盘展示 CPU、网络、磁盘指标、告警与历史图表。",
                    "tag": "可观测",
                },
                {
                    "icon": "git-branch",
                    "title": "一键快照",
                    "desc": "即时快照与每日自动备份,秒级回滚,无需中断服务。",
                    "tag": "备份",
                },
            ]
        return [
            {
                "icon": "shield-check",
                "title": "SLA-Backed Uptime",
                "desc": "99.99% availability guarantee with automatic credit compensation for any downtime beyond commitment.",
                "tag": "Reliability",
            },
            {
                "icon": "refresh-ccw",
                "title": "7-Day Money Back",
                "desc": "Try any plan risk-free. Full refund within 7 days, no questions asked, no hidden fees.",
                "tag": "Guarantee",
            },
            {
                "icon": "lock",
                "title": "Data Sovereignty",
                "desc": "Your data stays in your chosen region. Encrypted at rest with AES-256 and in transit with TLS 1.3.",
                "tag": "Privacy",
            },
            {
                "icon": "life-buoy",
                "title": "24/7 Expert Support",
                "desc": "Direct access to senior engineers via ticket, chat and Telegram — average first response under 5 minutes.",
                "tag": "Support",
            },
            {
                "icon": "activity",
                "title": "Real-time Monitoring",
                "desc": "Live dashboard with CPU, network, disk metrics, alerts and historical graphs at every layer.",
                "tag": "Observability",
            },
            {
                "icon": "git-branch",
                "title": "One-click Snapshots",
                "desc": "Instant snapshots and automated daily backups. Roll back in seconds without service interruption.",
                "tag": "Backup",
            },
        ]

    # ==================== Login Page Translations ====================
    @rx.var
    def login_title(self) -> str:
        return self._t("Log in to your Account", "登录您的账户")

    @rx.var
    def login_subtitle(self) -> str:
        return self._t(
            "Welcome back! Select method to log in.", "欢迎回来！选择登录方式。"
        )

    @rx.var
    def login_placeholder_email(self) -> str:
        return self._t("Enter your email", "输入您的电子邮箱")

    @rx.var
    def login_placeholder_password(self) -> str:
        return self._t("Enter your password", "输入您的密码")

    @rx.var
    def login_remember(self) -> str:
        return self._t("Remember password", "记住密码")

    @rx.var
    def login_forgot(self) -> str:
        return self._t("Forgot password", "忘记密码")

    @rx.var
    def login_btn_submit(self) -> str:
        return self._t("Log In", "登录")

    @rx.var
    def login_btn_logging_in(self) -> str:
        return self._t("Logging in...", "登录中...")

    @rx.var
    def login_or(self) -> str:
        return self._t("Or", "或")

    @rx.var
    def login_telegram(self) -> str:
        return self._t("Telegram login", "Telegram 登录")

    @rx.var
    def login_no_account(self) -> str:
        return self._t(
            "Don't have an account? Register now", "还没有账户？立即注册"
        )

    # ==================== Register Page Translations ====================
    @rx.var
    def register_title(self) -> str:
        return self._t("Sign up AkileCloud", "注册 AkileCloud")

    @rx.var
    def register_subtitle(self) -> str:
        return self._t("Sign up AkileCloud", "注册 AkileCloud")

    @rx.var
    def register_placeholder_username(self) -> str:
        return self._t("Enter your username", "输入您的用户名")

    @rx.var
    def register_placeholder_email(self) -> str:
        return self._t("Enter your email", "输入您的电子邮箱")

    @rx.var
    def register_placeholder_captcha(self) -> str:
        return self._t("Enter the captcha", "输入验证码")

    @rx.var
    def register_btn_captcha(self) -> str:
        return self._t("Send Captcha", "发送验证码")

    @rx.var
    def register_placeholder_password(self) -> str:
        return self._t("Enter your password", "输入您的密码")

    @rx.var
    def register_placeholder_confirm(self) -> str:
        return self._t("Repeat your password", "确认您的密码")

    @rx.var
    def register_placeholder_invitation(self) -> str:
        return self._t("Enter invitation code (optional)", "输入邀请码（可选）")

    @rx.var
    def register_btn_submit(self) -> str:
        return self._t("Sign up", "注册")

    @rx.var
    def register_btn_submitting(self) -> str:
        return self._t("Signing up...", "注册中...")

    @rx.var
    def register_has_account(self) -> str:
        return self._t(
            "Already have an account? Log in now", "已有账户？立即登录"
        )

    # ==================== FAQ Section ====================
    @rx.var
    def faq_badge(self) -> str:
        return self._t("FAQ", "常见问题")

    @rx.var
    def faq_title_prefix(self) -> str:
        return self._t("Frequently asked ", "常见 ")

    @rx.var
    def faq_title_highlight(self) -> str:
        return self._t("questions", "问题解答")

    @rx.var
    def faq_desc(self) -> str:
        return self._t(
            "Answers to the most common questions about our cloud services, network and support.",
            "关于我们的云服务、网络与支持,常见问题一次解答。",
        )

    @rx.var
    def faq_still_questions(self) -> str:
        return self._t("Still have questions?", "还有其他问题?")

    @rx.var
    def faq_help_desc(self) -> str:
        return self._t(
            "Our team is here to help you 24/7. Choose your preferred channel.",
            "我们的团队 7×24 小时为您服务,请选择您偏好的渠道。",
        )

    @rx.var
    def faq_list(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {
                    "id": "faq-1",
                    "q": "「流媒体解锁」到底意味着什么?",
                    "a": "每台 AkileCloud VPS 都为其地区配置原生住宅级 IP。这意味着 Netflix、Disney+、HBO Max、TikTok、ChatGPT 与 BBC iPlayer 等服务会将其识别为合法本地用户,并提供完整地区目录——无代理阻断,无地理限制。",
                },
                {
                    "id": "faq-2",
                    "q": "付款后多长时间可以开通?",
                    "a": "全自动开通。付款确认后,您的 VPS 将在 60 秒内完成部署与启动,并可通过 SSH/RDP 访问。您将立即通过邮件与控制台收到凭据。",
                },
                {
                    "id": "faq-3",
                    "q": "之后可以升级或降级方案吗?",
                    "a": "可以。您可以随时在控制台通过简单重启进行垂直扩展(增加 vCPU / 内存 / 磁盘)。流量与带宽上限也可无停机即时提升。",
                },
                {
                    "id": "faq-4",
                    "q": "支持自定义 ISO / 操作系统吗?",
                    "a": "完全支持。我们提供 Ubuntu、Debian、CentOS、Rocky、AlmaLinux、Windows Server 2019/2022 与 FreeBSD。您也可以上传自己的 ISO 完全掌控。",
                },
                {
                    "id": "faq-5",
                    "q": "退款政策是怎样的?",
                    "a": "所有月付方案提供 7 天无理由退款保障。若不满意,请在激活后 7 天内提交工单,我们将全额退款——无需理由。",
                },
                {
                    "id": "faq-6",
                    "q": "DDoS 防护如何工作?",
                    "a": "所有服务器均免费提供 20 Gbps 缓解。企业与商业方案获 100–200 Gbps 防护,支持自动 L3/L4 清洗与可选 L7 WAF。攻击透明吸收——服务持续在线。",
                },
                {
                    "id": "faq-7",
                    "q": "接受哪些支付方式?",
                    "a": "信用卡 / 借记卡 (Visa、Mastercard、Amex)、PayPal、支付宝、微信支付、USDT (TRC-20 / ERC-20),年度企业合约支持银行电汇。",
                },
                {
                    "id": "faq-8",
                    "q": "有自动化 API 吗?",
                    "a": "有。我们的 REST API 与 Terraform provider 覆盖控制台所有操作——创建/销毁服务器、快照、防火墙规则、DNS。适合 CI/CD 与基础设施即代码工作流。",
                },
            ]
        return [
            {
                "id": "faq-1",
                "q": "What does 'streaming unlock' actually mean?",
                "a": "Every AkileCloud VPS ships with a native residential-class IP for its region. This means services like Netflix, Disney+, HBO Max, TikTok, ChatGPT and BBC iPlayer detect the IP as a legitimate local user and serve full regional catalogs — no proxy blocks, no geo restrictions.",
            },
            {
                "id": "faq-2",
                "q": "How fast is provisioning after payment?",
                "a": "Automated. Once payment is confirmed, your VPS is provisioned, booted and ready via SSH/RDP in under 60 seconds. You'll receive credentials by email and in the console immediately.",
            },
            {
                "id": "faq-3",
                "q": "Can I upgrade or downgrade my plan later?",
                "a": "Yes. You can vertically scale (more vCPU / RAM / disk) at any time from the console with a simple reboot. Traffic and bandwidth caps can be increased instantly without downtime.",
            },
            {
                "id": "faq-4",
                "q": "Do you support custom ISO / operating systems?",
                "a": "Absolutely. We ship with Ubuntu, Debian, CentOS, Rocky, AlmaLinux, Windows Server 2019/2022 and FreeBSD. You can also upload your own ISO for full control.",
            },
            {
                "id": "faq-5",
                "q": "What is your refund policy?",
                "a": "We offer a 7-day money-back guarantee on all monthly plans. If you're not satisfied for any reason, open a ticket within 7 days of activation and receive a full refund — no questions asked.",
            },
            {
                "id": "faq-6",
                "q": "How does DDoS protection work?",
                "a": "All servers include free 20 Gbps mitigation. Business and Enterprise plans get 100–200 Gbps protection with automatic L3/L4 scrubbing and optional L7 WAF. Attacks are absorbed transparently — your service stays online.",
            },
            {
                "id": "faq-7",
                "q": "Which payment methods do you accept?",
                "a": "Credit / debit cards (Visa, Mastercard, Amex), PayPal, Alipay, WeChat Pay, USDT (TRC-20 / ERC-20) and bank wire for annual enterprise contracts.",
            },
            {
                "id": "faq-8",
                "q": "Is there an API for automation?",
                "a": "Yes. Our REST API and Terraform provider expose every console operation — create/destroy servers, snapshots, firewall rules, DNS. Perfect for CI/CD and infra-as-code workflows.",
            },
        ]

    @rx.var
    def support_channels(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {
                    "icon": "message-circle",
                    "title": "在线聊天",
                    "desc": "平均响应 < 2 分钟",
                    "action": "开始聊天",
                },
                {
                    "icon": "send",
                    "title": "电报群",
                    "desc": "社区与优先支持",
                    "action": "加入群组",
                },
                {
                    "icon": "mail",
                    "title": "邮箱",
                    "desc": "support@akilecloud.com",
                    "action": "发送邮件",
                },
                {
                    "icon": "book-open",
                    "title": "文档",
                    "desc": "指南、API 参考、教程",
                    "action": "阅读文档",
                },
            ]
        return [
            {
                "icon": "message-circle",
                "title": "Live Chat",
                "desc": "Avg. response < 2 min",
                "action": "Start chat",
            },
            {
                "icon": "send",
                "title": "Telegram",
                "desc": "Community & priority support",
                "action": "Join group",
            },
            {
                "icon": "mail",
                "title": "Email",
                "desc": "support@akilecloud.com",
                "action": "Send email",
            },
            {
                "icon": "book-open",
                "title": "Documentation",
                "desc": "Guides, API reference, tutorials",
                "action": "Read docs",
            },
        ]

    # ==================== CTA Section ====================
    @rx.var
    def cta_badge(self) -> str:
        return self._t("Ready when you are", "随时为您准备")

    @rx.var
    def cta_title_prefix(self) -> str:
        return self._t("Deploy your first server in ", "部署您的首台服务器,")

    @rx.var
    def cta_title_highlight(self) -> str:
        return self._t("under 60 seconds", "仅需 60 秒")

    @rx.var
    def cta_desc(self) -> str:
        return self._t(
            "Join 50,000+ developers and businesses running production workloads on AkileCloud. No credit card required to start.",
            "加入 50,000+ 开发者与企业,在 AkileCloud 上运行生产工作负载。无需信用卡即可开始。",
        )

    @rx.var
    def cta_btn_primary(self) -> str:
        return self._t("Get Started Free", "免费开始")

    @rx.var
    def cta_btn_secondary(self) -> str:
        return self._t("Read Documentation", "查看文档")

    @rx.var
    def cta_check1(self) -> str:
        return self._t("7-day money back", "7 天退款")

    @rx.var
    def cta_check2(self) -> str:
        return self._t("Cancel anytime", "随时取消")

    @rx.var
    def cta_check3(self) -> str:
        return self._t("Instant provisioning", "即时开通")

    @rx.var
    def cta_check4(self) -> str:
        return self._t("24/7 support", "7×24 支持")

    # ==================== Footer Section ====================
    @rx.var
    def footer_desc(self) -> str:
        return self._t(
            "Global high-bandwidth cloud services with streaming-unlocked native IPs. Built for developers, streamers and enterprises.",
            "全球大带宽云服务,原生 IP 流媒体解锁。为开发者、主播与企业打造。",
        )

    @rx.var
    def footer_addr(self) -> str:
        return self._t("Global · 100+ PoPs", "全球 · 100+ 边缘节点")

    @rx.var
    def footer_all_operational(self) -> str:
        return self._t("All systems operational", "全部系统运行正常")

    @rx.var
    def footer_status_page(self) -> str:
        return self._t("Status page", "状态页")

    @rx.var
    def footer_payments_accepted(self) -> str:
        return self._t("Payments accepted:", "支持支付方式:")

    @rx.var
    def footer_copy(self) -> str:
        return self._t(
            "© 2025 AkileCloud Technology Ltd. All rights reserved.",
            "© 2025 AkileCloud Technology Ltd. 版权所有。",
        )

    @rx.var
    def footer_col_products(self) -> str:
        return self._t("Products", "产品")

    @rx.var
    def footer_col_network(self) -> str:
        return self._t("Network", "网络")

    @rx.var
    def footer_col_resources(self) -> str:
        return self._t("Resources", "资源")

    @rx.var
    def footer_col_company(self) -> str:
        return self._t("Company", "公司")

    @rx.var
    def footer_products_links(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {"label": "云服务器", "href": "#products"},
                {"label": "轻量服务器", "href": "#products"},
                {"label": "独立服务器", "href": "#products"},
                {"label": "流媒体解锁", "href": "#products"},
                {"label": "云高防", "href": "#products"},
                {"label": "企业计算", "href": "#products"},
            ]
        return [
            {"label": "Cloud Servers", "href": "#products"},
            {"label": "Light Server", "href": "#products"},
            {"label": "Dedicated Servers", "href": "#products"},
            {"label": "Streaming Unlock", "href": "#products"},
            {"label": "Anti-DDoS Cloud", "href": "#products"},
            {"label": "Enterprise Compute", "href": "#products"},
        ]

    @rx.var
    def footer_network_links(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {"label": "全球节点", "href": "#nodes"},
                {"label": "BGP 路由", "href": "#nodes"},
                {"label": "DDoS 防护", "href": "#trust"},
                {"label": "网络状态", "href": "#"},
                {"label": "IP 工具", "href": "#"},
                {"label": "Looking Glass", "href": "#"},
            ]
        return [
            {"label": "Global Nodes", "href": "#nodes"},
            {"label": "BGP Routes", "href": "#nodes"},
            {"label": "DDoS Protection", "href": "#trust"},
            {"label": "Network Status", "href": "#"},
            {"label": "IP Tools", "href": "#"},
            {"label": "Looking Glass", "href": "#"},
        ]

    @rx.var
    def footer_resources_links(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {"label": "文档", "href": "#"},
                {"label": "API 参考", "href": "#"},
                {"label": "教程", "href": "#"},
                {"label": "博客", "href": "#"},
                {"label": "常见问题", "href": "#faq"},
                {"label": "社区", "href": "#"},
            ]
        return [
            {"label": "Documentation", "href": "#"},
            {"label": "API Reference", "href": "#"},
            {"label": "Tutorials", "href": "#"},
            {"label": "Blog", "href": "#"},
            {"label": "FAQ", "href": "#faq"},
            {"label": "Community", "href": "#"},
        ]

    @rx.var
    def footer_company_links(self) -> list[dict[str, str]]:
        if self.language == "zh":
            return [
                {"label": "关于我们", "href": "#"},
                {"label": "联系", "href": "#"},
                {"label": "招聘", "href": "#"},
                {"label": "服务条款", "href": "#"},
                {"label": "隐私政策", "href": "#"},
                {"label": "SLA", "href": "#"},
            ]
        return [
            {"label": "About Us", "href": "#"},
            {"label": "Contact", "href": "#"},
            {"label": "Careers", "href": "#"},
            {"label": "Terms of Service", "href": "#"},
            {"label": "Privacy Policy", "href": "#"},
            {"label": "SLA", "href": "#"},
        ]

    @rx.var
    def footer_legal_privacy(self) -> str:
        return self._t("Privacy", "隐私")

    @rx.var
    def footer_legal_terms(self) -> str:
        return self._t("Terms", "条款")

    @rx.var
    def footer_legal_cookies(self) -> str:
        return self._t("Cookies", "Cookie")

    @rx.var
    def footer_legal_aup(self) -> str:
        return self._t("Acceptable Use", "使用规范")