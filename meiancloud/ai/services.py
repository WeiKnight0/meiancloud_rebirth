import json
import uuid

import requests
import sseclient


bot_app_key = "CKYuxNxnwIdoawZYszTUSPaMzObOwYFiKijlZBmfrCcCBOCWgSwfNwIFjnpErNgqpZuEbSSkONIwbtszYZxnKoaEYMFEfUJtkTAZKdcXPcWBZAgzjkFzxwWoejhTrRoj"
visitor_biz_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, "meiancloud.localhost"))
streaming_throttle = 1


def sse_client(message: str, sid: str) -> str:
    req_data = {
        "content": message,
        "bot_app_key": bot_app_key,
        "visitor_biz_id": visitor_biz_id,
        "session_id": sid,
        "streaming_throttle": streaming_throttle,
    }
    resp = requests.post(
        "https://wss.lke.cloud.tencent.com/v1/qbot/chat/sse",
        data=json.dumps(req_data),
        stream=True,
        headers={"Accept": "text/event-stream"},
    )
    client = sseclient.SSEClient(resp)
    for event in client.events():
        data = json.loads(event.data)
        if event.event != "reply":
            continue
        payload = data["payload"]
        if payload["is_from_self"]:
            continue
        if payload["is_final"]:
            return payload["content"]
    return "获取失败"


def process_ai_message(message: str, session_id: str) -> str:
    assert isinstance(message, str)
    assert isinstance(session_id, str)
    return sse_client(message.lower(), session_id)
