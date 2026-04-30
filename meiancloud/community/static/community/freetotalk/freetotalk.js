async function parseJsonResponse(response) {
  let data = {};
  try {
    data = await response.json();
  } catch (error) {
    throw new Error("服务器返回了无法解析的响应");
  }

  if (!response.ok || !data.success) {
    throw new Error(data.error || "请求失败，请稍后重试");
  }

  return data;
}

function setButtonLoading(button, isLoading) {
  if (!button) {
    return;
  }

  button.disabled = isLoading;
  if (isLoading) {
    button.dataset.originalText = button.textContent;
    button.textContent = "提交中...";
  } else if (button.dataset.originalText) {
    button.textContent = button.dataset.originalText;
    delete button.dataset.originalText;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  const page = document.querySelector(".freetotalk-container");
  if (!page) {
    return;
  }

  const csrfToken = page.dataset.csrfToken;
  const commentCreateUrl = page.dataset.commentCreateUrl;

  document.querySelectorAll(".delete-comment-btn").forEach((button) => {
    button.addEventListener("click", async function () {
      const commentId = button.dataset.commentId;
      const confirmed = await window.showConfirm({
        title: "删除评论",
        message: "确定要删除这条评论吗？删除后无法恢复。",
        confirmText: "删除",
        cancelText: "取消",
        type: "danger",
      });
      if (!confirmed) {
        return;
      }

      setButtonLoading(button, true);
      try {
        const response = await fetch(`/api/comments/${commentId}/`, {
          method: "DELETE",
          headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/json",
          },
        });
        await parseJsonResponse(response);
        document.querySelector(`.comment-item[data-comment-id="${commentId}"]`)?.remove();
        document.querySelector(`.reply-item[data-comment-id="${commentId}"]`)?.remove();
        window.showToast("评论删除成功", "success");
      } catch (error) {
        window.showToast(`删除失败: ${error.message}`, "error");
      } finally {
        setButtonLoading(button, false);
      }
    });
  });

  document.getElementById("id_comment-form")?.addEventListener("submit", async function (event) {
    event.preventDefault();
    const submitButton = this.querySelector("button[type='submit']");
    const formData = new FormData(this);

    setButtonLoading(submitButton, true);
    try {
      const response = await fetch(commentCreateUrl, {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
        },
      });
      await parseJsonResponse(response);
      window.showToast("提交评论成功！请等待审核通过。", "success", {
        onClose: function () {
          window.location.reload();
        },
      });
    } catch (error) {
      window.showToast(`提交评论失败！${error.message}`, "error");
    } finally {
      setButtonLoading(submitButton, false);
    }
  });

  document.querySelectorAll(".reply-form").forEach((form) => {
    form.addEventListener("submit", async function (event) {
      event.preventDefault();
      const submitButton = form.querySelector("button[type='submit']");
      const formData = new FormData(form);
      const commentId = formData.get("comment_id");

      setButtonLoading(submitButton, true);
      try {
        const response = await fetch(`/api/comments/${commentId}/replies/`, {
          method: "POST",
          body: formData,
          headers: {
            "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
          },
        });
        await parseJsonResponse(response);
        window.showToast("提交回复成功！请等待审核通过。", "success", {
          onClose: function () {
            window.location.reload();
          },
        });
      } catch (error) {
        window.showToast(`提交回复失败！${error.message}`, "error");
      } finally {
        setButtonLoading(submitButton, false);
      }
    });
  });

  document.querySelectorAll(".reply-button").forEach((button) => {
    button.addEventListener("click", function () {
      const replies = document.getElementById(`replies-${button.dataset.commentId}`);
      if (!replies) {
        return;
      }
      const isVisible = replies.style.display === "block";
      replies.style.display = isVisible ? "none" : "block";
      button.textContent = isVisible ? "展开回复" : "收起回复";
    });
  });
});
