// Khai báo id
const d_click = document.getElementById("d_click");
const i_click = document.getElementById("i_click");
const int_doc = document.getElementById("int-doc");
const int_img = document.getElementById("int-img");
const content = document.getElementById("typing-area");
const dropArea = document.querySelector(".drag-area");

// typing-area
content.addEventListener("click", function (event) {
  event.preventDefault();
  if (content.textContent.trim() === "Nhập nội dung ở đây...") {
    content.textContent = "";
  }
});

// doc-area

d_click.addEventListener("click", () => {
  int_doc.click();
});

int_doc.addEventListener("change", function () {
  const file = this.files[0];
  showFile_doc(file);
});

function showFile_doc(file) {
  const reader = new FileReader();

  reader.onload = function () {
    const contents = reader.result;
    content.innerHTML = contents;
  };

  reader.readAsText(file);
}

// img-area

i_click.addEventListener("click", () => {
  int_img.click();
});

int_img.addEventListener("change", function () {
  const file = this.files[0];
  showFile_img(file);
});

dropArea.addEventListener("drop", function (event) {
  event.preventDefault();
  const file = event.dataTransfer.files[0];
  showFile_img(file);
});

function showFile_img(file) {
  const fileType = file.type;
  const ValidExtensions = ["image/jpeg", "image/jpg", "image/png"];
  if (ValidExtensions.includes(fileType)) {
    const fileReader = new FileReader();
    fileReader.onload = () => {
      const fileUrl = fileReader.result; // Data URL of the image
      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/dangbai');
      xhr.setRequestHeader('Content-Type', 'application/json');
      xhr.onload = () => {
        // Handle response from Flask server
        if (xhr.status === 200) {
          console.log('Image uploaded successfully');
          // cap nhat thong tin trang thai 
        } else {
          console.error('Failed to upload image:', xhr.statusText);
        }
      };
      xhr.send(JSON.stringify({ imageUrl: fileUrl })); // Send data URL in JSON format
    };
  
    fileReader.readAsDataURL(file);
  }
}
