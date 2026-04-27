import json
import logging

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .services.ai_client import process_ai_message


logger = logging.getLogger(__name__)


@require_POST
@csrf_exempt
def chat_api(request):
    """处理聊天API请求"""
    try:
        data = json.loads(request.body.decode("utf-8"))
        user_message = data.get("message", "").strip()
        session_id = data.get("session_id", "")
        if not user_message:
            return JsonResponse({"error": "消息内容不能为空"}, status=400)

        logger.info("收到消息: %s, 会话ID: %s", user_message, session_id)
        ai_reply = process_ai_message(user_message, session_id)
        return JsonResponse(
            {"reply": ai_reply, "session_id": session_id, "status": "success"}
        )
    except json.JSONDecodeError:
        return JsonResponse({"error": "无效的JSON格式！请联系管理员处理"}, status=400)
    except Exception as exc:
        logger.error("处理消息时出错: %s", exc)
        return JsonResponse({"error": "服务器内部错误！请联系管理员处理"}, status=500)
