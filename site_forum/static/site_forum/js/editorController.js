import { ajaxForum } from "./modules/ajaxForum.mjs";

const simplemde = new SimpleMDE({ 
    element: document.querySelector("#topicoForm textarea") ,
    spellChecker: false,
    hideIcons: ["image"],
    status: false,
    forceSync: true,
});

const simplemdeResponder = new SimpleMDE({ 
    element: document.querySelector("#respostaForm textarea") ,
    spellChecker: false,
    hideIcons: ["image"],
    status: false,
    forceSync: true,
});

const urlCreateRespostaCache = document.getElementById("respostaForm").action;

(function markdownToHTMLPosts() {
    document.querySelectorAll(".markdown").forEach(element => {
        element.innerHTML = simplemde.options.previewRender(element.innerText);
    });
})();


window.activeForms =  function activeForms(element) {
    const forms = document.querySelectorAll(".offcanvas-body>form");
    const action = element.getAttribute("data-form-action");
    forms.forEach(form => form.style.display = "none");

    switch(action) {
        case "RESPONDER":
            activeFormResponder(element.getAttribute("data-resposta-id"));
            break;
        case "EDITAR_RESPOSTA":
            activeFormResponder(element.getAttribute("data-resposta-id"), false);
            break;
        case "EDITAR_TOPICO":
            activeFormEditTopico();
            break;
        default:
            console.error("Form action não implementada!");
    }
}

function activeFormEditTopico() {
    const form = document.getElementById("topicoForm");    
    const idTopico = document.getElementById("inputTopico").value;
    
    ajaxForum.getTopicoById(idTopico).then(json => {
        simplemde.value(json.data[0].texto);
        document.getElementById("inputTitulo").value = json.data[0].titulo;
    });

    form.style.display = "block";
}

function activeFormResponder(resposta_id, create=true) {
    const form = document.getElementById("respostaForm");

    if(create) {
        form.action = urlCreateRespostaCache;
        document.getElementById("inputResposta").value = resposta_id;
    } else {
        ajaxForum.getRespostaById(resposta_id).then(json => {
            form.action = urlCreateRespostaCache + `${resposta_id}/`;
            simplemdeResponder.value(json.data[0].texto);
            document.getElementById("inputResposta").value = json.data[0].parent__id;
            console.log(json.data[0].parent)
        });
    }

    form.style.display = "block";
}