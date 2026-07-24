async function predictComment(text) {

    return new Promise((resolve) => {

        chrome.runtime.sendMessage(
            {
                type: "predict",
                text: text
            },
            (response) => {
                resolve(response);
            }
        );

    });

}