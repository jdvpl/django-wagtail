!(function () {
  let e = document.createElement("script"),
    t = document.head || document.getElementsByTagName("head")[0];
  (e.src = window.location.origin + "/static/js/chatbot/rasa-webchat.js"),
    // Replace 1.x.x with the version that you want
    (e.async = !0),
    (e.onload = () => {
      window.WebChat.default(
        {
          socketUrl: "http://172.17.1.84:80",
          socketPath: "/socket.io/",
          title: "Consúltame",
          interval: "2000",
          initPayload: "Hola",
          storage: "session",
          // add other props here
        },
        null
      );
    }),
    t.insertBefore(e, t.firstChild);
})();
