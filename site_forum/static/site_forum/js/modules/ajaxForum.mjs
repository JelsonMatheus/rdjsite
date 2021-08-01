function createUrl(urlString, params) {
    const paramsString = Object.entries(params)
        .map(([k, v]) => `${k}=${v}`).join("&");

    if(paramsString)
        return urlString + "?" + paramsString;

    return urlString;
}

const ajaxForum = {
    getTopicoById: async (id) => {
        const url = createUrl("/ajax/topicos/", {'pk': id});
        const response = await fetch(url);
        return await response.json();
    },

    getRespostaById: async (id) => {
        const url = createUrl("/ajax/respostas/", {'pk': id});
        const response = await fetch(url);
        return await response.json();
    }
};

export { ajaxForum };

