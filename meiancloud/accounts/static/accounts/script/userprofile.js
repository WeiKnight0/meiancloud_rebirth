async function parseAccountResponse(response) {
  let data = {};
  try {
    data = await response.json();
  } catch (error) {
    throw new Error("服务器返回了无法解析的响应");
  }

  if (!response.ok || !data.success) {
    throw new Error(data.error || "请求失败，请重试");
  }

  return data;
}

document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("password-modal");
  const deleteButton = document.getElementById("delete-button");
  const cancelButton = document.getElementById("cancel-button");
  const confirmButton = document.getElementById("confirm-button");
  const passwordInput = document.getElementById("password-input");

  if (!modal || !deleteButton || !cancelButton || !confirmButton || !passwordInput) {
    return;
  }

  deleteButton.addEventListener("click", function () {
    modal.style.display = "block";
  });

  cancelButton.addEventListener("click", function () {
    modal.style.display = "none";
    passwordInput.value = "";
  });

  confirmButton.addEventListener("click", async function () {
    const password = passwordInput.value.trim();
    if (!password) {
      window.showToast("请输入密码！", "warning");
      return;
    }

    confirmButton.disabled = true;
    try {
      const formData = new FormData();
      formData.append("csrfmiddlewaretoken", modal.dataset.csrfToken);
      formData.append("password", password);

      const response = await fetch(modal.dataset.deleteAccountUrl, {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": modal.dataset.csrfToken,
        },
      });
      await parseAccountResponse(response);
      window.showToast("注销成功！", "success", {
        duration: 1200,
        onClose: function () {
          window.location.href = modal.dataset.redirectUrl;
        },
      });
    } catch (error) {
      window.showToast(error.message || "请求失败，请重试！", "error");
    } finally {
      confirmButton.disabled = false;
    }
  });
});
