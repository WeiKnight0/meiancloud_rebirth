async function showLogoutDialog() {
  const confirmed = await window.showConfirm({
    title: "退出登录",
    message: "你确定要退出登录吗？",
    confirmText: "退出",
    cancelText: "取消",
    type: "warning",
  });
  if (confirmed) {
    document.getElementById("logout-form")?.submit();
  }
}

function showToast(message, type = "info", options = {}) {
  let container = document.querySelector(".toast-container");
  if (!container) {
    container = document.createElement("div");
    container.className = "toast-container";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;
  toast.textContent = message;
  container.appendChild(toast);

  window.setTimeout(() => {
    toast.classList.add("toast-visible");
  }, 0);

  const duration = options.duration || 2500;
  window.setTimeout(() => {
    toast.classList.remove("toast-visible");
    window.setTimeout(() => {
      toast.remove();
      options.onClose?.();
    }, 250);
  }, duration);
}

window.showToast = showToast;

function showConfirm(options = {}) {
  return new Promise((resolve) => {
    const overlay = document.createElement("div");
    overlay.className = "confirm-overlay";

    const dialog = document.createElement("div");
    dialog.className = `confirm-dialog confirm-${options.type || "info"}`;
    dialog.setAttribute("role", "dialog");
    dialog.setAttribute("aria-modal", "true");

    const title = document.createElement("h2");
    title.textContent = options.title || "请确认";

    const message = document.createElement("p");
    message.textContent = options.message || "确认执行此操作吗？";

    const actions = document.createElement("div");
    actions.className = "confirm-actions";

    const cancelButton = document.createElement("button");
    cancelButton.type = "button";
    cancelButton.className = "confirm-cancel";
    cancelButton.textContent = options.cancelText || "取消";

    const confirmButton = document.createElement("button");
    confirmButton.type = "button";
    confirmButton.className = "confirm-submit";
    confirmButton.textContent = options.confirmText || "确认";

    function close(result) {
      overlay.classList.remove("confirm-visible");
      window.setTimeout(() => {
        overlay.remove();
        resolve(result);
      }, 180);
    }

    cancelButton.addEventListener("click", function () {
      close(false);
    });

    confirmButton.addEventListener("click", function () {
      close(true);
    });

    overlay.addEventListener("click", function (event) {
      if (event.target === overlay) {
        close(false);
      }
    });

    document.addEventListener("keydown", function handleEscape(event) {
      if (event.key === "Escape") {
        document.removeEventListener("keydown", handleEscape);
        close(false);
      }
    });

    actions.append(cancelButton, confirmButton);
    dialog.append(title, message, actions);
    overlay.appendChild(dialog);
    document.body.appendChild(overlay);

    window.setTimeout(() => {
      overlay.classList.add("confirm-visible");
      confirmButton.focus();
    }, 0);
  });
}

window.showConfirm = showConfirm;

function shouldTransitionLink(link, event) {
  if (event.defaultPrevented || event.button !== 0) {
    return false;
  }

  if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
    return false;
  }

  if (link.dataset.noTransition !== undefined || link.target || link.hasAttribute("download")) {
    return false;
  }

  const href = link.getAttribute("href");
  if (!href || href === "#") {
    return false;
  }

  const normalizedHref = href.trim().toLowerCase();
  if (normalizedHref.startsWith("javascript:") || normalizedHref.startsWith("mailto:") || normalizedHref.startsWith("tel:")) {
    return false;
  }

  const url = new URL(link.href, window.location.href);
  if (url.origin !== window.location.origin) {
    return false;
  }

  const currentPath = `${window.location.pathname}${window.location.search}`;
  const targetPath = `${url.pathname}${url.search}`;
  if (currentPath === targetPath && url.hash) {
    return false;
  }

  if (url.href === window.location.href) {
    return false;
  }

  return true;
}

document.addEventListener("DOMContentLoaded", function () {
  const content = document.querySelector(".content");
  if (content) {
    content.classList.add("fade-in");
  }

  document.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", function (event) {
      if (!content || !shouldTransitionLink(link, event)) {
        return;
      }

      event.preventDefault();
      content.classList.remove("fade-in");
      content.classList.add("fade-out");

      const targetHref = link.href;
      window.setTimeout(() => {
        window.location.href = targetHref;
      }, 500);

      window.setTimeout(() => {
        if (window.location.href !== targetHref) {
          content.classList.remove("fade-out");
          content.classList.add("fade-in");
        }
      }, 900);
    });
  });
});

window.onpageshow = function (event) {
  if (event.persisted) {
    document.querySelector(".content")?.classList.add("fade-in");
  }
};
