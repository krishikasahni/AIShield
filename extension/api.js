async function predictComment(text) {

    return new Promise((resolve) => {

        chrome.runtime.sendMessage(
            {
                type: "predict",
                text: text
            },
            (response) => {
		console.log("Response from background:", response);
		console.log("Runtime error:", chrome.runtime.lastError);
                resolve(response);
            }
        );

    });

}