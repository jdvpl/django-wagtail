let loadLocalConfig = () => {
  if (localStorage.getItem("contrast") == "true") {
    document.documentElement.classList.add("hight-contrast");
  } else {
    document.documentElement.classList.remove("hight-contrast");
  }
  fontSizes(parseInt(localStorage.getItem("fontsize")));
};

let hightContrastHandler = () => {
  if (localStorage.getItem("contrast") !== null) {
    if (localStorage.getItem("contrast") === "true") {
      document.documentElement.classList.remove("hight-contrast");
      localStorage.setItem("contrast", false);
    } else {
      document.documentElement.classList.add("hight-contrast");
      localStorage.setItem("contrast", true);
    }
  } else if (localStorage.getItem("contrast") === null) {
    document.documentElement.classList.add("hight-contrast");
    localStorage.setItem("contrast", true);
  }
};

let removeClass = () => {
  var el = document.querySelector('html[class*="font-size-"]');
  if (el !== null) {
    for (let i = el.classList.length - 1; i >= 0; i--) {
      const className = el.classList[i];
      if (className.startsWith("font-size-")) {
        el.classList.remove(className);
      }
    }
  }
};

let fontSizes = (size) => {
  removeClass();
  switch (size) {
    case -3:
      document.documentElement.classList.add("font-size-xx-small");
      break;
    case -2:
      document.documentElement.classList.add("font-size-x-small");
      break;
    case -1:
      document.documentElement.classList.add("font-size-small");
      break;
    case 3:
      document.documentElement.classList.add("font-size-xx-large");
      break;
    case 2:
      document.documentElement.classList.add("font-size-x-large");
      break;
    case 1:
      document.documentElement.classList.add("font-size-large");
      break;
    default:
      removeClass();
  }
};

let reduceFontSizeHandler = () => {
  var size = 0;
  if (localStorage.getItem("fontsize") !== null) {
    size = parseInt(localStorage.getItem("fontsize"));
    if (size > -2) {
      localStorage.setItem("fontsize", size - 1);
      size = parseInt(localStorage.getItem("fontsize"));
    }
  } else if (localStorage.getItem("fontsize") === null) {
    size = -1;
    localStorage.setItem("fontsize", -1);
  }
  fontSizes(size);
};

let increaseFontSizeHandler = () => {
  var size = 0;
  if (localStorage.getItem("fontsize") !== null) {
    size = parseInt(localStorage.getItem("fontsize"));
    if (size < 2) {
      localStorage.setItem("fontsize", size + 1);
      size = parseInt(localStorage.getItem("fontsize"));
    }
  } else if (localStorage.getItem("fontsize") === null) {
    size = 1;
    localStorage.setItem("fontsize", 1);
  }
  fontSizes(size);
};

let normalFontSizeHandler = () => {
  var size = 0;
  if (localStorage.getItem("fontsize") !== null) {
    localStorage.setItem("fontsize", 0);
  } else if (localStorage.getItem("fontsize") === null) {
    localStorage.setItem("fontsize", 0);
  }
  fontSizes(size);
};

// Function to add event listener
const contrast = document.getElementById("contrast");
contrast.addEventListener("click", hightContrastHandler, false);

const reducefontsize = document.getElementById("reducefontsize");
reducefontsize.addEventListener("click", reduceFontSizeHandler, false);

const increasefontsize = document.getElementById("increasefontsize");
increasefontsize.addEventListener("click", increaseFontSizeHandler, false);

const normalfontsize = document.getElementById("normalfontsize");
normalfontsize.addEventListener("click", normalFontSizeHandler, false);

loadLocalConfig();
