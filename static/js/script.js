document.addEventListener("DOMContentLoaded", function (event) {
    setTimeout(() => {
        const iframe = document.getElementById("id_content_iframe");
        const iWindow = iframe.contentWindow;
        const iDocument = iWindow.document;
        const element = iDocument.getElementsByClassName('note-editor')[0];
        element.style = "width:100%"
    }, 1000);

});