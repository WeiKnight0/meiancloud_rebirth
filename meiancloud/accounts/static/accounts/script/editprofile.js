document.addEventListener("DOMContentLoaded", function () {
  const imageInput = document.getElementById("id_image");
  const currentImage = document.getElementById("current-image");

  if (!imageInput || !currentImage) {
    return;
  }

  imageInput.addEventListener("change", function (event) {
    const file = event.target.files[0];
    if (!file) {
      return;
    }

    const reader = new FileReader();
    reader.onload = function (loadEvent) {
      currentImage.src = loadEvent.target.result;
    };
    reader.readAsDataURL(file);
  });
});
