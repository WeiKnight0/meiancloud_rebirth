document.addEventListener("DOMContentLoaded", function () {
  const successTarget = document.querySelector("[data-success-message][data-success-redirect]");
  if (!successTarget || successTarget.dataset.success !== "true") {
    return;
  }

  window.showToast(successTarget.dataset.successMessage, "success", {
    duration: 1200,
    onClose: function () {
      window.location.href = successTarget.dataset.successRedirect;
    },
  });
});
