import reflex as rx


class StyleTestState(rx.State):
    is_submitting: bool = False
    demo_name: str = ""
    demo_email: str = ""
    saved_records: list[dict[str, str]] = [
        {
            "name": "HK-BGP-Standard",
            "status": "active",
            "ip": "103.28.112.5",
            "type": "BGP optimized",
        },
        {
            "name": "JP-Tokyo-Direct",
            "status": "pending",
            "ip": "185.19.22.4",
            "type": "Direct routing",
        },
    ]

    @rx.event
    async def submit_demo(self, form_data: dict):
        self.is_submitting = True
        yield
        import asyncio

        await asyncio.sleep(0.5)
        name = form_data.get("name", "").strip()
        email = form_data.get("email", "").strip()
        if name and email:
            self.saved_records.append(
                {
                    "name": name,
                    "status": "active",
                    "ip": f"103.28.201.{len(self.saved_records) + 40}",
                    "type": "Dynamic Sandbox Node",
                }
            )
            self.demo_name = ""
            self.demo_email = ""
            self.is_submitting = False
            yield rx.toast(
                title="Success / 提交成功",
                description="The mock server is provisioned into your list. / 模拟服务器已开通。",
                duration=4000,
                close_button=True,
            )
        else:
            self.is_submitting = False
            yield rx.toast(
                title="Error / 错误",
                description="Name and email are required. / 请填写所有必需字段。",
                duration=4000,
                close_button=True,
            )
